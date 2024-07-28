from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a variável de ambiente DATABASE_URL
database_url = os.getenv('DATABASE_URL')

# Verificar se a variável foi carregada corretamente
if not database_url:
    raise ValueError("A variável de ambiente DATABASE_URL não foi carregada corretamente")

print(database_url)
# Criar engine e sessão
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

# Declarative base
Base = declarative_base()

# Verificar a conexão
try:
    connection = engine.connect()
    print("Conexão bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    print(database_url)

# Agora você pode continuar com suas operações ORM
