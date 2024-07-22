import sys
import os
import bcrypt
from flask import Flask, jsonify

from src.models.bd_model import User
from src.auth.jwt_auth import token, decodeToken

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



def register_user(name, email, password):
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
        new_user = User.create_user(name, email, password_bcrypt)

        return jsonify({"message": "User created", "id": new_user.id}), 201

    
