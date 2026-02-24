from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, db_url: str):
        self._engine = create_engine(db_url)
        self._sessionLocal = sessionmaker(bind=self._engine)
        