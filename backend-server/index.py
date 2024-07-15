from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO
from mongoengine import connect
from dotenv import load_dotenv
import os

from routes import register_routes

load_dotenv()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000", logger=True, engineio_logger=True)

# Database connection
connect(db='your_db_name', host=os.getenv("MONGO_URL"))

# Register routes
register_routes(app)

# Define onlineUsers here
global online_users
online_users = {}

@socketio.on('connect')
def handle_connect():
    global chat_socket
    chat_socket = request.sid

# @socketio.on('add-user')
# def handle_add_user(data):
#     user_id = data['userId']
#     online_users[user_id] = request.sid


@socketio.on('add-user')
def handle_add_user(data):
    try:
      print(f"printing the data: \n{data}\n\n {request.sid}")
      user_id = data
      online_users[user_id] = request.sid
      print(f"User {user_id} connected with SID {request.sid}")

    except KeyError as e:
        print(f"Error: Missing key 'userId' in data: {str(e)}")
   

@socketio.on('send-msg')
def handle_send_msg(data):
    to_user_id = data['to']
    msg = data['msg']
    send_user_socket = online_users.get(to_user_id)
    if send_user_socket:
        socketio.emit('msg-recieve', msg, room=send_user_socket)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    print(f"Server started on {port}")
    socketio.run(app, host="0.0.0.0", port=port)
