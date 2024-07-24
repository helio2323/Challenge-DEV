import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.models.bd_model import Questions
from src.utils.utlgen import transform_objects_to_json
from flask import jsonify, request, json
from datetime import datetime

# Create a new question
def create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at):
    try:
        # Ensure that id_language and xp_reward are integers
        id_language = int(id_language)
        xp_reward = int(xp_reward)

        # Ensure that created_at is a valid datetime string
        if not created_at:
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
            created_at=created_at
        )
        return jsonify({"message": "Question created", "id": new_question.id})
    except (ValueError, TypeError) as e:
        print(f"Error in input data: {e}")
        return None

def get_all_questions():
    questions = Questions.get_all_questions()
    questions = transform_objects_to_json(questions, id="id", title="title", subtitle="subtitle", type_question="type_question", question="question", id_language="id_language", xp_reward="xp_reward", response="response", created_at="created_at")

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
            "created_at": question.created_at
        })

        return question_json
    except:
        return "Question not found"

from datetime import datetime

def update_question(id, title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at):
    try:
        # Convertendo id_language e xp_reward para inteiros
        id_language = int(id_language)
        xp_reward = int(xp_reward)

        # Verificando e formatando created_at
        if created_at:
            try:
                # Tenta converter para o formato de data aceito
                created_at = datetime.strptime(created_at, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                # Se o formato estiver incorreto, defina uma data padrão
                created_at = datetime.now().strftime('%Y-%m-%d')
        else:
            # Se created_at for vazio, defina uma data padrão
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
            created_at=created_at
        )

        return updated_question
    except (ValueError, TypeError) as e:
        print(f"Error in input data: {e}")
        return None


def delete_question(id):
    question = Questions.delete_question(id)
    return question
