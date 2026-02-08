from sqlmodel import SQLModel
from .database import engine
from ..models.user import User
from ..models.todo import Todo

def create_db_and_tables():
    """
    Creates the database and all tables based on the SQLModel models.
    This function should be called on application startup.
    """
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_db_and_tables()