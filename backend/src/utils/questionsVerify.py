import datetime
import sys
import os

from flask import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.services.questions import get_one_questions
from src.models.bd_model import User, UserResponse
from src.auth.authentication import get_one_user
from src.utils.pistonApi import execute_code

def aumentar_nivel(pontos_atual, nivel_atual):
    pontos_total = pontos_atual
    while pontos_total >= 1000:
        pontos_total -= 1000
        nivel_atual += 1
    return pontos_total, nivel_atual


def questionVerify(id, responseQuestion):
    
    responseQuestion = responseQuestion.lower()
    
    question = get_one_questions(id)
    question = json.loads(question)
    question = question["response"].lower()

    print(question, responseQuestion)
    if question == responseQuestion:
        return "Question correct"
    else:
        return "Question incorrect"
    
def submitQuestion(question_id, user_id, responseQuestion):
    response = questionVerify(question_id, responseQuestion)
    current_date = datetime.datetime.now()

    #verity if question was already answered
    user_response = UserResponse.search_user_response(user_id, question_id)
    if user_response:
        return "Question already answered"

    if response == "Question correct":
        get_xp = get_one_questions(question_id)
        get_xp = json.loads(get_xp)
        xp = get_xp["xp_reward"]
        level_user = get_one_user(user_id)
        level_user = json.loads(level_user)
        nivel_atual = level_user["level"]
        
        xp_user = get_one_user(user_id)
        xp_user = json.loads(xp_user)
        xp_user = xp_user["xp"]
        xp_user = xp_user + xp

        level = aumentar_nivel(xp_user, nivel_atual)

        #add xp to user
        User.update_xp_level(user_id, xp_user, level)

        #save the response question
        UserResponse.create_user_response(user_id, question_id, current_date)
    
        return 'Question answered'
    else:
        return "Question incorrect"


