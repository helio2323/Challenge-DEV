from src.models.bd_model import Questions

def create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at):
    try:
        question = Questions()
        question.create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at)
        return {"message": "Question created"}
    except Exception as e:
        return {"message": str(e)}

def get_all_questions():
    try:
        questions = Questions.get_all_questions()
        return questions
    except Exception as e:
        return {"message": str(e)}
def update_question(id, title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at):
    try:
        question = Questions()
        question.update_question(id, title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at)
        return {"message": "Question updated"}
    except Exception as e:
        return {"message": str(e)}

def delete_question(id):
    try:
        question = Questions()
        question.delete_question(id)
        return {"message": "Question deleted"}
    except Exception as e:
        return {"message": str(e)}
