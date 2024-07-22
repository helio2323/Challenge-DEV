import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import bcrypt
from flask import Flask, json, jsonify

from src.models.bd_model import User
from src.auth.jwt_auth import token, decodeToken
from src.utils.utlgen import transform_objects_to_json

app = Flask(__name__)

def login_user(email, password):
    email = email.lower()
    user = User.search_user(email)
    
    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404
    else:
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            generateToken = token(user.name, user.id)

        return jsonify({"response": "User logged in",
                        "token": generateToken}), 200



def register_user(id, email, password):
    email = email.lower()
    user = User()
    verify_user = user.search_user(email)

    if verify_user is not None:
        return jsonify({
            "message": "User already exists"
        }), 409
    else:
        salt = bcrypt.gensalt()
        password_bcrypt = bcrypt.hashpw(password.encode('utf-8'), salt)
        password_bcrypt = password_bcrypt.decode('utf-8')
        new_user = User.create_user(id, email, password_bcrypt)

        return jsonify({"message": "User created", "id": new_user.id}), 201

    
def get_users():
    
    users = User.get_all_users()
    #transforma os objetos em JSON
    users = transform_objects_to_json(users, id="id", name="name", email="email")
    print(users)
    return users

def get_one_user(id):
    user = User.search_user_by_id(id)
    user_json = json.dumps({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

    return user_json

def update_user(id, name, email, password):

    email = email.lower()
    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User.update_user(id, name, email, password)
    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404
    user_json = json.dumps({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })

    print(user_json)
    return user_json

