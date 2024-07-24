from pistonapi import PistonAPI

def get_language_versions(language_name):
    piston = PistonAPI()
    languages = piston.runtimes
    version = None
    
    if language_name in languages:
        version = languages[language_name]["version"]
        return version
    else:
        return "Linguagem não suportada"

def execute_code(language_name, code):
    piston = PistonAPI()
    version = get_language_versions(language_name)
    # Execute seu código se a versão foi encontrada
    result = piston.execute(language=language_name, version=version, code=code)
    result = str(result).strip()
    return result

