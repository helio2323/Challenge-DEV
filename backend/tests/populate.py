import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from backend.src.services.questions import create_question
import json
import requests


# Popule a linguagem
"""
language.create_language('Python')
language.create_language('Javascript')
language.create_language('Java')
language.create_language('Rust')"""

json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'questions.json'))

with open(json_file_path, 'r') as file:
    data = json.load(file)


for question in data['questions']:

    json_data = {
        "title": question['title'],
        "subtitle": question['subtitle'],
        "example": question['example'],
        "type_question": question['type_question'],
        "question": question['question'],
        "id_language": question['id_language'],
        "xp_reward": question['xp_reward'],
        "response": question['response'],
        "created_at": question['created_at'],
        "dificulty": question['difficulty']
    }

    requests.post("http://167.88.33.24:5000/api/v1/createquestion", json=json_data)

