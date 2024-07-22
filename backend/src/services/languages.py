import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.models.bd_model import Language

def create_language(cod_language):
    #verify language exist
    language = Language.search_language(cod_language)
    if language:
        return {"message": "Language already exist"}
    
    try:
        lang = Language()
        new_language = lang.create_language(cod_language)
        return new_language
    except Exception as e:
        return {"message": str(e)}