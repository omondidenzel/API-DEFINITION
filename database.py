from sqlalchemy import create_engine

URL_DATABASE = 'postgresql://postgres:your_password@localhost:5450/database_name'

def create_connection():
    return create_engine(URL_DATABASE)

engine = create_connection()


