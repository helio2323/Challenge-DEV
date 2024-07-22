from flask import Blueprint, jsonify, request, make_response
from src.services.languages import create_language
from src.services.questions import *


services_routes = Blueprint("services_routes", __name__)

@services_routes.route("/newlanguage", methods=["POST"])
async def newlanguage():

    data = request.json

    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        name = data.get("name")

        result = create_language(name)
        print(result['language'])
        return jsonify(result)

@services_routes.route("/newquestion", methods=["POST"])
async def new_question():

    data = request.json

    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        title = data.get("title")
        subtitle = data.get("subtitle")
        example = data.get("example")
        type_question = data.get("type_question")
        question = data.get("question")
        id_language = data.get("id_language")
        xp_reward = data.get("xp_reward")
        response_id = data.get("response_id")
        created_at = data.get("created_at")

        result = create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at)

        return result
    
