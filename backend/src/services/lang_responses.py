import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.utlgen import transform_objects_to_json
from src.models.bd_model import Language, UserResponse
from flask import jsonify

def get_all_user_responses():
    lang_responses = UserResponse.get_all_user_responses()
    #transforma os objetos em JSON
    lang_responses = transform_objects_to_json(lang_responses, id="id", user_id="user_id", question_id="question_id", responded_at="responded_at")

    return lang_responses

def get_all_languages():
    languages = Language.get_all_languages()
    #transforma os objetos em JSON
    languages = transform_objects_to_json(languages, id="id", language="language")

    return languages

