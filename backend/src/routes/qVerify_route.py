from flask import Blueprint, json, jsonify, make_response, request
from src.services.ranking import create_ranking, create_daily_ranking, calculate_user_points_with_level
from src.utils.questionsVerify import questionVerify, submitQuestion
from src.utils.pistonApi import execute_code
from src.services.lang_responses import get_all_languages, get_all_user_responses

qVerify = Blueprint("qVerify", __name__)

@qVerify.route("/", methods=["GET"])
def index():
    return "Hello, World!"
@qVerify.route("/verify", methods=["POST"])
async def verify():

    data = request.json

    type_question = data.get("type_question")
    question_id = data.get("question_id")
    questionResponse = data.get("questionresponse")
    language = data.get("language")

    if type_question == "code":
        
        code_response = execute_code(language, questionResponse)

        response = questionVerify(question_id, code_response)

        return jsonify({
            "response": response,
            "code_response": code_response})


    if type_question == "quizz":

        response = questionVerify(question_id, questionResponse)

        return jsonify({
            "response": response,
            "code_response": questionResponse})

    return "Invalid type"


@qVerify.route("/submit", methods=["POST"])
async def submit():

    data = request.json

    type_question = data.get("type_question")
    user_id = data.get("user_id")
    question_id = data.get("question_id")
    questionResponse = data.get("questionresponse")
    language = data.get("language")

    if type_question == "code":
        
        code_response = execute_code(language, questionResponse)

        response = submitQuestion(question_id, user_id, code_response)

        return jsonify({
            "response": response,
            "code_response": code_response})


    if type_question == "quizz":

        response = submitQuestion(question_id, user_id, questionResponse)

        return jsonify({
            "response": response,
            "code_response": questionResponse
        })

    return "Invalid type"

@qVerify.route("/languages", methods=["GET"])
async def languages():
    json_data = json.loads(get_all_languages())

    return jsonify(json_data)

@qVerify.route("/responses", methods=["GET"])
async def responses():
    json_data = json.loads(get_all_user_responses())

    return jsonify(json_data)

@qVerify.route("/ranking", methods=["GET"])
async def ranking():
    json_data = create_ranking()
    print(json_data)
    return json_data

@qVerify.route("/dailyranking", methods=["GET"])
async def dailyranking():
    json_data = create_daily_ranking()
    print(json_data)
    return json_data

@qVerify.route("/userlevel", methods=["POST"])
async def userlevel():

    data = request.json

    userid = data.get("userid")

    userL = calculate_user_points_with_level(userid)

    return userL