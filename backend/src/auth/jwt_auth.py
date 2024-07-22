import jwt
from datetime import datetime, timedelta, timezone
import os

secret = os.getenv("SECRET")

def token(userName, userId):
    exp_time = datetime.now(timezone.utc) + timedelta(minutes=10)
    payload = {
        'user': userName,
        'userId': userId,
        'exp': exp_time
    }
    generateToken = jwt.encode(
        payload,  # Payload deve ser passado diretamente
        secret,
        algorithm='HS256'
    )
    return generateToken

def decodeToken(token):
    try:
        decode_token = jwt.decode(token, secret, algorithms=['HS256'])
        return decode_token
    except jwt.ExpiredSignatureError:
        return 'Token expirado'
    except jwt.InvalidTokenError:
        return 'Token inválido'
