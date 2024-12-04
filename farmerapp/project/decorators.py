from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from enum import Enum

class Role(Enum):
    ADMIN = 'admin'
    SUPERUSER = 'superuser'
    VIEWER = 'viewer'

def role_required(roles=None):
    # If no roles are provided, allow access to users with any role
    if roles is None:
        roles = []

    if isinstance(roles, Role):
        roles = [roles]

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                user = get_jwt_identity()
                user_roles = set(user.get('roles', []))
                
                if Role.SUPERUSER.value in user_roles:
                    return f(*args, **kwargs)
                
                if not roles:
                    return f(*args, **kwargs)
            
                if not any(role.value in user_roles for role in roles):
                    return jsonify({"error": "Access denied"}), 403
                
                return f(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": "Login required", "Exception caught": str(e)}), 401
        return decorated_function
    return decorator
