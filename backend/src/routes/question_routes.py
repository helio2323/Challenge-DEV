from flask import Blueprint, jsonify, make_response, request, json
from src.services.questions import get_all_questions,get_one_questions, create_question, get_one_questions, update_question, delete_question

question_routes = Blueprint("question_routes", __name__)


@question_routes.route("createquestion", methods=["POST"])
async def createquestion():

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
        response = data.get("response")
        created_at = data.get("created_at"),
        dificulty = data.get("dificulty")
        result = create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at, dificulty)

        return result
    


@question_routes.route("getallquestions", methods=["GET"])
async def getallquestions():
    json_obj = json.loads(get_all_questions())
    return json_obj

@question_routes.route("getonequestion", methods=["POST"])
async def getonequestion():
    data = request.json
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        result = get_one_questions(id)
        return result
    
@question_routes.route("updatequestion", methods=["PUT"])
async def updatequestion():
    data = request.json
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        title = data.get("title")
        subtitle = data.get("subtitle")
        example = data.get("example")
        type_question = data.get("type_question")
        question = data.get("question")
        id_language = data.get("id_language")
        xp_reward = data.get("xp_reward")
        response = data.get("response")
        created_at = data.get("created_at"),
        dificulty = data.get("dificulty")
        result = update_question(id, title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at, dificulty)
        return jsonify({"message": "Question updated"})
    
@question_routes.route("deletequestion", methods=["DELETE"])
async def deletequestion():
    data = request.json
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        result = delete_question(id)
        return jsonify({"message": "Question deleted"})