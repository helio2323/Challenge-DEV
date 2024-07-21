from flask import Blueprint, jsonify, request

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET"])
def Register():
    return 'Hello Register'