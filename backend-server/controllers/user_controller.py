from flask import jsonify, request
import json
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User  # Import the User model from models/user_model.py
from session_manager import session_manager
from socketio_instance import socketio

def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"msg": "Incorrect Username or Password", "status": False}), 400
        
        user.password = None  # Remove password from response for security
        # Transform the JSON to valid frontend format
        transformed_json = transform_json(user.to_json())

        return jsonify({"status": True, "user": transformed_json}), 200
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500

def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if User.objects(username=username).first():
            return jsonify({"msg": "Username already used", "status": False}), 400
        
        if User.objects(email=email).first():
            return jsonify({"msg": "Email already used", "status": False}), 400
        
        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)
        user.save()
        
        user.password = None  # Remove password from response for security
        # Transform the JSON to valid frontend format
        transformed_json = transform_json(user.to_json())

        return jsonify({"status": True, "user": transformed_json}), 201
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500
    
# Function to transform the JSON - strange format created in python mongoose
def transform_json(input_json):
    input_json = json.loads(input_json)
    output_json = input_json.copy()
    output_json["_id"] = input_json["_id"]["$oid"]
    return output_json

def get_all_users(id):
    try:
        users = User.objects.filter(id__ne=ObjectId(id)).only('email', 'username', 'avatarImage')
        users_list = [{"_id": str(user.id), "email": user.email, "username": user.username, "avatarImage": user.avatarImage} for user in users]
        return jsonify(users_list), 200
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500

def set_avatar(id):
    try:
        data = request.get_json()
        avatar_image = data.get('image')
        
        user = User.objects(id=id).first()
        if not user:
            return jsonify({"msg": "User not found", "status": False}), 404
        
        user.avatarImage = avatar_image
        user.isAvatarImageSet = True
        user.save()
        
        return jsonify({"isSet": user.isAvatarImageSet, "image": user.avatarImage}), 200
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500

def log_out(id):
    try:
        socket_sid = session_manager.remove_user(id)  # Get and remove the Socket.IO session ID
        print(socket_sid)
        if socket_sid:
            socketio.emit('disconnect-me', room=socket_sid)
            #socketio.disconnect(sid=socket_sid)   # Disconnect the user from SocketIO
        return jsonify({"status": "success", "message": "Logged out successfully"}), 200
    except Exception as ex:
        return jsonify({"msg": str(ex)}), 500
