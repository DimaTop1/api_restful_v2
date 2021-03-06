from users import User
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp




def authenticate(username, password):
    user = User.find_by_username(username)
    if user and (user.password == password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)