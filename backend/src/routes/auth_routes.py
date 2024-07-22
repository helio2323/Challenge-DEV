from flask import Blueprint, jsonify, request, make_response
from src.auth.authentication import login_user, register_user

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["POST"])
async def index():
    return 'Hello World'

@routes.route("/register", methods=["POST"])
async def register():
    
    data = request.json

    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        result = register_user(name, email, password)

        return result
    
@routes.route("/login", methods=["POST"])
async def login():
    
    data = request.json

    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        email = data.get("email")
        password = data.get("password")
        result = login_user(email, password)

        return result