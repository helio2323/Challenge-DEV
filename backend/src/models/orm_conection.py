from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#Load env variables for postgress connection
user=os.getenv('USER_NAME')
password=os.getenv('PASSWORD')
host=os.getenv('HOST')
port=os.getenv('PORT')
database=os.getenv('DATABASE')

DATABASE_URI = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
    
