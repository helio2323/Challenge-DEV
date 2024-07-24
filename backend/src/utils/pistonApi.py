from pistonapi import PistonAPI

def get_language_versions(language_name):

    piston = PistonAPI()

    languages = piston.runtimes

    language_name = "python"
    version = None
    
    if language_name in languages:
        version = languages[language_name]["version"]
        return version
    else:
        return "Linguagem não suportada"

def execute_code(language_name, code):
    piston = PistonAPI()
    version = get_language_versions(language_name)
# Execute your own code if the version was found
    result = piston.execute(language=language_name, version=version, code=code)
    print(result)

