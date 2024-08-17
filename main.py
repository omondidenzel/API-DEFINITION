from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
import database
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

Base = declarative_base()

# Model definition
class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)

Base.metadata.create_all(database.engine)

# Data Type validation
class UsersValidation(BaseModel):
    user_id: int
    user_name: str


@app.post("/create_users/")
async def create_user_fun(users: UsersValidation):
    with Session(database.engine) as session:
        user1 = Users(user_id = users.user_id, user_name= users.user_name)
        session.add(user1)
        session.commit()
        session.close()

@app.get('/get_users/')
async def get_users_fun():
    with Session(database.engine) as session_read:
        results = session_read.query(Users).all() 
        return {
            'data': results
        }
