import os
import sys
from datetime import date, datetime, timedelta
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.models.bd_model import UserChallenge
from src.utils.utlgen import transform_objects_to_json

def create_user_challenge(user_id, challenge_id, completed, date_completed, date_started, active):
    useChallenge = UserChallenge()
    all_challenges = get_all_user_challenge()
    current_time = datetime.now()
    
    def process_challenges(challenge_type, days):
        challenges = [c for c in all_challenges if c['user_id'] == user_id and c['challenge_id'] == challenge_type]
        
        for challenge in challenges:
            start_date = datetime.strptime(challenge['date_started'], "%a, %d %b %Y %H:%M:%S GMT")
            if current_time - start_date > timedelta(days=days):
                print(f'Updating old challenge {challenge["id"]} to inactive')
                update_user_challenge(challenge['id'], user_id, challenge_type, challenge['completed'], challenge['date_completed'], challenge['date_started'], False)
        
        if challenges:
            latest_challenge = max(challenges, key=lambda x: datetime.strptime(x['date_started'], "%a, %d %b %Y %H:%M:%S GMT"))
            if current_time - datetime.strptime(latest_challenge['date_started'], "%a, %d %b %Y %H:%M:%S GMT") > timedelta(days=days):
                print(f'Creating new challenge {challenge_type}')
                useChallenge.create_user_challenge(user_id, challenge_type, completed, date_completed, date_started, active)
        else:
            print(f'Creating new challenge {challenge_type}')
            useChallenge.create_user_challenge(user_id, challenge_type, completed, date_completed, date_started, active)

    process_challenges(1, 1)  # Daily challenge
    process_challenges(2, 7)  # Weekly challenge

    return 'Challenges created or updated'

def get_all_user_challenge():
    useChallenge = UserChallenge()
    challenges = useChallenge.get_all_user_challenge()
    challenges_json = transform_objects_to_json(challenges, id="id", user_id="user_id", challenge_id="challenge_id", completed="completed", date_completed="date_completed", date_started="date_started", active="active")
    return json.loads(challenges_json)

def get_one_user_challenge(id, challenge_id):
    useChallenge = UserChallenge()
    challenge = useChallenge.search_user_challenge(id, challenge_id)
    
    challenge_dict = {
        "id": challenge.id,
        "user_id": challenge.user_id,
        "challenge_id": challenge.challenge_id,
        "completed": challenge.completed,
        "date_completed": challenge.date_completed,
        "date_started": challenge.date_started,
        "active": challenge.active
    }
    
    # Use json.dumps with the date_handler function
    challenge_json = json.dumps(challenge_dict, default=date_handler)
    print(challenge_json)
    return json.loads(challenge_json)
def update_user_challenge(id, user_id, challenge_id, completed, date_completed, date_started, active):
    useChallenge = UserChallenge()
    useChallenge.update_user_challenge(id, user_id, challenge_id, completed, date_completed, date_started, active)

    return 'Challenge updated'
# Teste da função

def date_handler(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Type not serializable")
