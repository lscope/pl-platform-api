from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import Engine

from .env import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


db_url: str = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine: Engine = create_engine(db_url)


def create_db() -> None:
    """Create DB tables.
    """
    SQLModel.metadata.create_all()

def get_sql_session():
    """Get SQL session.

    Yields:
        Session: SQL session
    """
    with Session(bind=engine) as session:
        yield session
