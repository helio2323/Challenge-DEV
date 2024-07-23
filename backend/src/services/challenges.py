import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.models.bd_model import Challenge
from src.utils.utlgen import transform_objects_to_json
from flask import request, json

def get_all_challenges():
    challenges = Challenge.get_all_challenge()
    challenges_json = transform_objects_to_json(challenges, id="id", type_challenge="type_challenge", xp_reward="xp_reward")
    return json.loads(challenges_json)

def get_one_challenge(id):
    challenge = Challenge.search_challenge(id)
    challenge_json = json.dumps({
        "id": challenge.id,
        "type_challenge": challenge.type_challenge,
        "xp_reward": challenge.xp_reward
    })
    return json.loads(challenge_json)

