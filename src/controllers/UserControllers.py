import sys, os
import json
import jwt
from flask import request, make_response, jsonify
from src.models.user import User

SECRET_KEY = os.getenv('JWT_SECRET_KEY')


def login():
    data = json.loads(request.data)
    try:
        user = User.query.filter_by(email=data['email']).first()

        if user:
            payload = {
                'user_id': user.id,
                'name': user.name,
                'email': user.email
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            res = {'status': 'success', 'access_token': token}

        return jsonify(res), 200

    except Exception as e:
        response = jsonify({'message': 'Internal Server Error'})
        return response, 500


def register():
    data = json.loads(request.data)
    try:
        user = User(data)
        user.save()
        if user:
            res = {'status': 'success'}
        return jsonify(res), 201
    except Exception as e:
        print(e)
        response = jsonify({'message': 'Internal Server Error'})
        return response, 500
