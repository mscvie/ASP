class SessionManager:
    def __init__(self):
        self.online_users = {}  # Mapping of user_id to Socket.IO session ID

    def add_user(self, user_id, socket_sid):
        self.online_users[user_id] = socket_sid

    def remove_user(self, user_id):
        return self.online_users.pop(user_id, None)

    def get_socket_sid(self, user_id):
        return self.online_users.get(user_id)

# Instantiate a global session manager
session_manager = SessionManager()
