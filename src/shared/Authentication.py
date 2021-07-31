from functools import wraps
import jwt, os, json
from flask import request, Response, g
from src.models.user import User

SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class Auth:
    """
    Auth Class
    """
    @staticmethod
    def decode_token(token):
        re = {'data': {}, 'error': {}}
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        re['data'] = decoded
        return re

    @staticmethod
    def auth_required(func):
        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if 'access_token' not in request.headers:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({
                        'error':
                        'You dont have the credential to use this API'
                    }),
                    status=403)

            access_token = request.headers.get('access_token')
            data = Auth.decode_token(access_token)

            user = User.get_one_user(data['data']['user_id'])

            if not user:
                return Response(mimetype='application/json',
                                response=json.dumps(
                                    {'error': 'User is not found'}),
                                status=403)
            g.user = {'id': user.id}
            return func(*args, **kwargs)

        return decorated_auth
