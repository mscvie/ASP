from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO
from mongoengine import connect
from dotenv import load_dotenv
import os
from session_manager import session_manager
from socketio_instance import socketio

from routes import register_routes

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database connection
connection = connect(db='your_db_name', host=os.getenv("MONGO_URL"))

# Register routes
register_routes(app)

# Initialize SocketIO with the Flask app
socketio.init_app(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    global chat_socket
    chat_socket = request.sid

@socketio.on('add-user')
def handle_add_user(data):
    try:
      user_id = data
      #online_users[user_id] = request.sid
      session_manager.add_user(user_id, request.sid)

    except KeyError as e:
        print(f"Error: Missing key 'userId' in data: {str(e)}")
   

@socketio.on('send-msg')
def handle_send_msg(data):
    to_user_id = data['to']
    msg = data['msg']
    send_user_socket = session_manager.get_socket_sid(to_user_id)
    if send_user_socket:
        socketio.emit('msg-recieve', msg, room=send_user_socket)


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    print(f"Server started on {port}")
    socketio.run(app, host="0.0.0.0", port=port)
