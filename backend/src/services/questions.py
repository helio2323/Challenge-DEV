import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.models.bd_model import Questions
from src.utils.utlgen import transform_objects_to_json
from flask import jsonify, request, json
from datetime import datetime

# Create a new question
def create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at, dificulty):
    try:
        # Ensure that id_language and xp_reward are integers
        id_language = int(id_language)
        xp_reward = int(xp_reward)

        # Ensure that created_at is a valid datetime string
        if not created_at:
            created_at = None  # Define como NULL se a data estiver vazia
        else:
            created_at = datetime.now().strftime('%Y-%m-%d')

        new_question = Questions.create_question(
            title=title,
            subtitle=subtitle,
            example=example,
            type_question=type_question,
            question=question,
            id_language=id_language,
            xp_reward=xp_reward,
            response=response,
            created_at=created_at,
            dificulty=dificulty
        )
        return jsonify({"message": "Question created", "id": new_question.id})
    except (ValueError, TypeError) as e:
        print(f"Error in input data: {e}")
        return jsonify({"message": "Invalid input data"}), 400

def get_all_questions():
    questions = Questions.get_all_questions()
    questions = transform_objects_to_json(questions, id="id", title="title", subtitle="subtitle", example="example", type_question="type_question", question="question", id_language="id_language", xp_reward="xp_reward", response="response", created_at="created_at", dificulty="dificulty")
    
    return questions

def get_one_questions(id):
    try:
        question = Questions.search_question(id)
        question_json = json.dumps({
            "id": question.id,
            "title": question.title,
            "subtitle": question.subtitle,
            "example": question.example,
            "type_question": question.type_question,
            "question": question.question,
            "id_language": question.id_language,
            "xp_reward": question.xp_reward,
            "response": question.response,
            "created_at": question.created_at,
            "dificulty": question.dificulty
        })

        return question_json
    except:
        return "Question not found"

from datetime import datetime

def update_question(id, title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at, dificulty):
    try:
        # Convertendo id_language e xp_reward para inteiros
        id_language = int(id_language)
        xp_reward = int(xp_reward)

        # Verificando e formatando created_at
        if not created_at:
            created_at = None  # Define como NULL se a data estiver vazia
        else:
            created_at = datetime.now().strftime('%Y-%m-%d')
        # Atualizando a questão
        updated_question = Questions.update_question(
            id=id,
            title=title,
            subtitle=subtitle,
            example=example,
            type_question=type_question,
            question=question,
            id_language=id_language,
            xp_reward=xp_reward,
            response=response,
            created_at=created_at,
            dificulty=dificulty
        )

        return updated_question
    except (ValueError, TypeError) as e:
        print(f"Error in input data: {e}")
        return None


def delete_question(id):
    question = Questions.delete_question(id)
    return question
