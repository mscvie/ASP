from flask_socketio import SocketIO

# socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000", logger=True, engineio_logger=True)
socketio = SocketIO(cors_allowed_origins="*", logger=True, engineio_logger=True)
