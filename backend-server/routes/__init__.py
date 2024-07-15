from flask import Blueprint
from .auth_routes import auth_blueprint
from .message_routes import message_blueprint

# Initialize and register all blueprints here
def register_routes(app):
    app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
    app.register_blueprint(message_blueprint, url_prefix="/api/messages")
