import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from src.models.orm_conection import Base, engine, session  # Updated import
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound




class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    language = Column(String, nullable=False)
    questions = relationship("Questions", back_populates="language")  # Corrigido

    @staticmethod
    def create_language(language):
        new_language = Language(language=language)
        session.add(new_language)
        session.commit()

        return new_language

    @staticmethod
    def search_language(language):
        return session.query(Language).filter_by(language=language).first()
    
    @staticmethod
    def get_all_languages():
        return session.query(Language).all()
    
    @staticmethod
    def update_language(id, language):
        lang = session.query(Language).filter_by(id=id).first()
        lang.language = language
        session.commit()

    @staticmethod
    def delete_language(id):
        lang = session.query(Language).filter_by(id=id).first()
        session.delete(lang)
        session.commit()

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    response = Column(String, unique=True)
    questions = relationship("Questions", back_populates="responses")  # Corrigido
    user_responses = relationship("UserResponse", back_populates="response")  # Add this line

    @staticmethod
    def create_response(response):
        new_response = Response(response=response)
        session.add(new_response)
        session.commit()

        return new_response
    @staticmethod
    def search_response(response):
        return session.query(Response).filter_by(response=response).first()
    
    @staticmethod
    def get_all_responses():
        return session.query(Response).all()
    
    @staticmethod
    def update_response(id, response):
        resp = session.query(Response).filter_by(id=id).first()
        resp.response = response
        session.commit()

    @staticmethod
    def delete_response(id):
        resp = session.query(Response).filter_by(id=id).first()
        session.delete(resp)
        session.commit()

class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    subtitle = Column(String)
    example = Column(String)
    type_question = Column(String)
    question = Column(String)
    id_language = Column(Integer, ForeignKey("languages.id"))
    language = relationship("Language", back_populates="questions")  # Corrigido
    xp_reward = Column(Integer)
    response_id = Column(Integer, ForeignKey("responses.id"))
    responses = relationship("Response", back_populates="questions")  # Corrigido
    created_at = Column(Date)
    user_responses = relationship("UserResponse", back_populates="question")

    @staticmethod
    def create_question(title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at):
        new_question = Questions(
            title=title,
            subtitle=subtitle,
            example=example,
            type_question=type_question,
            question=question,
            id_language=id_language,
            xp_reward=xp_reward,
            response_id=response_id,
            created_at=created_at
        )
        session.add(new_question)
        session.commit()

        return new_question
    @staticmethod
    def search_question(question):
        return session.query(Questions).filter_by(question=question).first()
    
    @staticmethod
    def get_all_questions():
        return session.query(Questions).all()
    
    @staticmethod
    def update_question(id, title, subtitle, example, type_question, question, id_language, xp_reward, response_id, created_at):
        question_obj = session.query(Questions).filter_by(id=id).first()
        question_obj.title = title
        question_obj.subtitle = subtitle
        question_obj.example = example
        question_obj.type_question = type_question
        question_obj.question = question
        question_obj.id_language = id_language
        question_obj.xp_reward = xp_reward
        question_obj.response_id = response_id
        question_obj.created_at = created_at
        session.commit()

        return question_obj
    @staticmethod
    def delete_question(id):
        question = session.query(Questions).filter_by(id=id).first()
        session.delete(question)
        session.commit()
        
        return "Question deleted"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    xp = Column(Integer)
    level = Column(Integer)
    challenges = relationship("UserChallenge", back_populates="user")
    responses = relationship("UserResponse", back_populates="user")

    @staticmethod
    def create_user(name, email, password):
        try:
            new_user = User(name=name, email=email, password=password)
            session.add(new_user)
            session.commit()
            return new_user
        except SQLAlchemyError as e:
            session.rollback()
            print(f'Error creating user: {e}')
            return None

    @staticmethod
    def search_user(email):
        try:
            user = session.query(User).filter_by(email=email).first()
            return user
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(f'Error searching user: {e}')
            return None
         
    def search_user_by_id(id):
        try:
            user = session.query(User).filter_by(id=id).first()
            return user
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(f'Error searching user: {e}')
            return None

    @staticmethod
    def get_all_users():
        try:
            users = session.query(User).all()
            return users
        except SQLAlchemyError as e:
            print(f'Error getting all users: {e}')
            return None    
    @staticmethod
    def update_user(id, name, email, password):
        try:
            id = int(id)
            # Verifica se o email já está em uso por outro usuário
            existing_user = session.query(User).filter(User.email == email, User.id != id).first()
            if existing_user:
                print("O email já está em uso por outro usuário.")
                return None
            
            user = session.query(User).filter_by(id=id).first()
            if user:
                user.name = name
                user.email = email
                user.password = password
                session.commit()
                return user
            else:
                print("Usuário não encontrado.")
                return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f'Error updating user: {e}')
            return None
class UserChallenge(Base):
    __tablename__ = "users_challenges"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    user = relationship("User", back_populates="challenges")
    challenge = relationship("Challenge", back_populates="users")
    completed = Column(Boolean)
    date_completed = Column(Date)
    date_started = Column(Date)
    active = Column(Boolean)

    @staticmethod
    def create_user_challenge(user_id, challenge_id, completed, date_completed, date_started, active):
        try:
            new_user_challenge = UserChallenge(
            user_id=user_id,
            challenge_id=challenge_id,
            completed=completed,
            date_completed=date_completed,
            date_started=date_started,
            active=active
        )
            session.add(new_user_challenge)
            session.commit()

            return new_user_challenge
        except SQLAlchemyError as e:
            session.rollback()
            print(f'Error creating user_challenge: {e}')
            return None
    @staticmethod
    def search_user_challenge(id, challenge_id):
        try:
            user_challenge = session.query(UserChallenge).filter_by(id=id, challenge_id=challenge_id).first()
            return user_challenge
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(f'Error searching user_challenge: {e}')
            return None
    @staticmethod
    def get_all_user_challenge():
        try:
            user_challenge = session.query(UserChallenge).all()
            return user_challenge
        except SQLAlchemyError as e:
            print(f'Error getting all user_challenge: {e}')
            return None
            
    @staticmethod
    def update_user_challenge(id, user_id, challenge_id, completed, date_completed, date_started, active):
        user_challenge = session.query(UserChallenge).filter_by(id=id).first()
        user_challenge.user_id = user_id
        user_challenge.challenge_id = challenge_id
        user_challenge.completed = completed
        user_challenge.date_completed = date_completed
        user_challenge.date_started = date_started
        user_challenge.active = active
        session.commit()
    
    @staticmethod
    def delete_user_challenge(id):
        user_challenge = session.query(UserChallenge).filter_by(id=id).first()
        session.delete(user_challenge)
        session.commit()

        return "User Challenge deleted"
class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True)
    type_challenge = Column(String)
    xp_reward = Column(Integer)
    users = relationship("UserChallenge", back_populates="challenge")

    @staticmethod
    def create_challenge(type_challenge, xp_reward):
        new_challenge = Challenge(type_challenge=type_challenge, xp_reward=xp_reward)
        session.add(new_challenge)
        session.commit()

        return new_challenge
    @staticmethod
    def search_challenge(id):
        try:
            challenge = session.query(Challenge).filter_by(id=id).first()
            return challenge
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(f'Error searching challenge: {e}')
            return None
        
    @staticmethod
    def get_all_challenge():
        try:
            challenge = session.query(Challenge).all()
            return challenge
        except SQLAlchemyError as e:
            print(f'Error getting all challenge: {e}')
            return None
            
    @staticmethod
    def update_challenge(id, type_challenge, xp_reward):
        challenge = session.query(Challenge).filter_by(id=id).first()
        challenge.type_challenge = type_challenge
        challenge.xp_reward = xp_reward
        session.commit()

        return challenge
    @staticmethod
    def delete_challenge(id):
        challenge = session.query(Challenge).filter_by(id=id).first()
        session.delete(challenge)
        session.commit()

        return "Challenge deleted"
class UserResponse(Base):
    __tablename__ = "users_responses"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    response_id = Column(Integer, ForeignKey("responses.id"))
    user = relationship("User", back_populates="responses")
    question = relationship("Questions", back_populates="user_responses")  # Alterado
    response = relationship("Response", back_populates="user_responses")  # Ensure this is correctly referenced
    responded_at = Column(Date)

    @staticmethod
    def create_user_response(user_id, question_id, response_id, responded_at):
        new_user_response = UserResponse(
            user_id=user_id,
            question_id=question_id,
            response_id=response_id,
            responded_at=responded_at
        )
        session.add(new_user_response)
        session.commit()

        return new_user_response
    @staticmethod
    def search_user_response(user_id, question_id):
        return session.query(UserResponse).filter_by(user_id=user_id, question_id=question_id).first()
    
    @staticmethod
    def get_all_user_responses():
        return session.query(UserResponse).all()
    
    @staticmethod
    def update_user_response(id, user_id, question_id, response_id, responded_at):
        user_response = session.query(UserResponse).filter_by(id=id).first()
        user_response.user_id = user_id
        user_response.question_id = question_id
        user_response.response_id = response_id
        user_response.responded_at = responded_at
        session.commit()

        return user_response
    @staticmethod
    def delete_user_response(id):
        user_response = session.query(UserResponse).filter_by(id=id).first()
        session.delete(user_response)
        session.commit()

        return "User Response deleted"
    
Base.metadata.create_all(engine)

