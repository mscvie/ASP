from flask import Blueprint
from controllers.user_controller import login, register, get_all_users, set_avatar, log_out

auth_blueprint = Blueprint('auth', __name__)

auth_blueprint.route('/login', methods=['POST'])(login)
auth_blueprint.route('/register', methods=['POST'])(register)
auth_blueprint.route('/allusers/<id>', methods=['GET'])(get_all_users)
auth_blueprint.route('/setavatar/<id>', methods=['POST'])(set_avatar)
auth_blueprint.route('/logout/<id>', methods=['GET'])(log_out)
