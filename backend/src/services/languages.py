from src.models.bd_model import Language

def create_language(language):
    try:
        language = Language()
        new_language = Language.create_language(language)
        return new_language
    except Exception as e:
        return {"message": str(e)}