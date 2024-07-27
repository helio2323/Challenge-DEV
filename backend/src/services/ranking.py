from datetime import datetime, timezone
from email.utils import parsedate_tz, mktime_tz
import sys
import os

from flask import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.auth.authentication import get_users
from src.services.lang_responses import get_all_user_responses
from src.utils.utlgen import transform_objects_to_json
from src.services.questions import get_one_questions



def create_ranking():
    users = get_users()
    responses = get_all_user_responses()

    responses = json.loads(responses)
    users = json.loads(users)
    
    # Criar um dicionário para armazenar o ranking
    ranking = {user['id']: {'name': user['name'], 'email': user['email'], 'responses': 0, 'points': 0} for user in users if isinstance(user, dict)}
    
    # Contar as respostas e calcular os pontos
    for response in responses:
        if isinstance(response, dict):
            user_id = response.get('user_id')
            if user_id in ranking:
                ranking[user_id]['responses'] += 1
                quest = get_one_questions(response.get('question_id'))
                quest = json.loads(quest)
                ranking[user_id]['points'] += quest['xp_reward']  # Exemplo de pontos, você pode ajustar conforme a lógica do seu sistema
    
    # Converter o dicionário em uma lista ordenada de acordo com os pontos
    ranking_list = sorted(ranking.values(), key=lambda x: x['points'], reverse=True)
    return ranking_list

def create_daily_ranking():
    users = get_users()
    responses = get_all_user_responses()

    responses = json.loads(responses)
    users = json.loads(users)
    
    # Criar um dicionário para armazenar o ranking
    ranking = {user['id']: {'name': user['name'], 'email': user['email'], 'responses': 0, 'points': 0} for user in users if isinstance(user, dict)}
    
    # Obter a data atual em UTC
    today = datetime.now(timezone.utc).date()
    
    # Contar as respostas e calcular os pontos
    for response in responses:
        if isinstance(response, dict):
            user_id = response.get('user_id')
            if user_id in ranking:
                responseDate = parse_date(response.get('responded_at'))
                if responseDate.date() == today:
                    ranking[user_id]['responses'] += 1
                    quest = get_one_questions(response.get('question_id'))
                    quest = json.loads(quest)
                    ranking[user_id]['points'] += quest['xp_reward']  # Exemplo de pontos, você pode ajustar conforme a lógica do seu sistema

    # Filtrar apenas usuários que responderam hoje
    ranking = {user_id: info for user_id, info in ranking.items() if info['responses'] > 0}
    
    # Converter o dicionário em uma lista ordenada de acordo com os pontos
    ranking_list = sorted(ranking.values(), key=lambda x: x['points'], reverse=True)
    return ranking_list

def parse_date(date_str):
    # Converter string de data para um objeto datetime
    parsed_date = parsedate_tz(date_str)
    timestamp = mktime_tz(parsed_date)
    response_date = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return response_date

#Buscar soma dos pontos de um unico usuario

def calculate_user_points(user_id):
    users = get_users()
    responses = get_all_user_responses()

    responses = json.loads(responses)
    users = json.loads(users)
    
    # Criar um dicionário para armazenar os dados do usuário
    user_data = {'name': '', 'email': '', 'responses': 0, 'points': 0}
    
    # Obter os detalhes do usuário
    for user in users:
        if isinstance(user, dict) and user['id'] == user_id:
            user_data['name'] = user['name']
            user_data['email'] = user['email']
            break
    
    # Obter a data atual em UTC
    today = datetime.now(timezone.utc).date()
    
    # Contar as respostas e calcular os pontos do usuário
    for response in responses:
        if isinstance(response, dict) and response.get('user_id') == user_id:
            responseDate = parse_date(response.get('responded_at'))
            user_data['responses'] += 1
            quest = get_one_questions(response.get('question_id'))
            quest = json.loads(quest)
            user_data['points'] += quest['xp_reward']

    return user_data

def calculate_level(points):
    # Define os pontos necessários para o primeiro nível
    base_points = 500
    level = 1

    while points >= base_points:
        points -= base_points
        level += 1
        # Aumenta os pontos necessários para o próximo nível em 15%
        base_points = int(base_points * 1.15)

    # Pontos restantes necessários para o próximo nível
    next_level_points = base_points - points

    return level, next_level_points

def calculate_user_points_with_level(user_id):
    user_data = calculate_user_points(user_id)
    level, next_level_points = calculate_level(user_data['points'])
    user_data['level'] = level
    user_data['next_level_points'] = next_level_points
    return user_data
