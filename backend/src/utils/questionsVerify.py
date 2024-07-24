import sys
import os

from flask import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.services.questions import get_one_questions
def questionVerify(id, responseQuestion):
    
    responseQuestion = responseQuestion.lower()
    
    question = get_one_questions(id)
    question = json.loads(question)
    question = question["response"].lower()

    if question == responseQuestion:
        return True
    else:
        return False
    

