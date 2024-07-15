from flask import Blueprint
from controllers.message_controller import add_message, get_messages

message_blueprint = Blueprint('message', __name__)

message_blueprint.route('/addmsg', methods=['POST'])(add_message)
message_blueprint.route('/getmsg', methods=['POST'])(get_messages)


