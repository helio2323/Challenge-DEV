from flask import Blueprint, jsonify, request

routes = Blueprint("routes", __name__)


@routes.route("/", methods=["GET"])
async def index():
    return 'Hello World'

@routes.route("/login", methods=["GET"])
async def login():
    return 'Hello Login'