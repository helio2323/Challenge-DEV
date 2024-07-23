from flask import Blueprint, jsonify, make_response, request
from src.services.userChallenges import create_user_challenge, update_user_challenge, get_all_user_challenge, get_one_user_challenge
from src.services.challenges import get_all_challenges, get_one_challenge

ChaRoutes = Blueprint("ChaRoutes", __name__)


@ChaRoutes.route("userChallenges", methods=["GET"])
async def get_user_challenge():
    return "Hello World"

@ChaRoutes.route('createUserChallenge', methods=['POST'])
async def createUserChallenge():
    data = request.json
    
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        user_id = data.get("user_id")
        challenge_id = data.get("challenge_id")
        completed = data.get("completed")
        date_completed = data.get("date_completed")
        date_started = data.get("date_started")
        active = data.get("active")
        result = create_user_challenge(user_id, challenge_id, completed, date_completed, date_started, active)

        return result

@ChaRoutes.route('getUserChallenges', methods=['GET'])
async def getUserChallenges():
    return get_all_user_challenge()

@ChaRoutes.route('userchallenge', methods=['GET'])
async def userchallenge():
    data = request.json
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        challenge_id = data.get("challenge_id")
        result = get_one_user_challenge(id, challenge_id)
        
        return result

@ChaRoutes.route('updateUserChallenge', methods=['PUT'])
async def updateUserChallenge():
    data = request.json
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        user_id = data.get("user_id")
        challenge_id = data.get("challenge_id")
        completed = data.get("completed")
        date_completed = data.get("date_completed")
        date_started = data.get("date_started")
        active = data.get("active")
        result = update_user_challenge(id, user_id, challenge_id, completed, date_completed, date_started, active)
        
        return result

@ChaRoutes.route('challenges', methods=['GET'])
async def challenges():
    return get_all_challenges()

@ChaRoutes.route('challenge', methods=['GET'])
async def challenge():
    data = request.json
    if data is None:
        return make_response(
            jsonify({"message": "Bad Request"}), 400
        )
    else:
        id = data.get("id")
        result = get_one_challenge(id)
        
        return result