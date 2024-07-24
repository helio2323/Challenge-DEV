from flask import Blueprint, jsonify, request, make_response
from src.auth.authentication import get_one_user, login_user, register_user, get_users, update_user

routes = Blueprint("routes", __name__)

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
    
@routes.route("users", methods=["GET"])
async def get_all_users():

    result = get_users()
    print(result)
    return result
@routes.route("user/<id>", methods=["GET"])
async def get_user(id):
    result = get_one_user(id)
    print(result)
    return result

@routes.route('updateuser', methods=['PUT'])
async def updateuser():
    data = request.json

    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        result = update_user(id, name, email, password)

        return result