from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from Models.base import Base
from Models import offer  
from Models import subscription 


class Database:
    def __init__(self, db_url: str):
        self._engine = create_engine(db_url)
        self._session_local = sessionmaker(bind=self._engine)

    def create_tables(self):
        Base.metadata.create_all(self._engine)

    def get_session(self) -> Session:
        return self._session_local()

    def dispose(self):
        self._engine.dispose()
        