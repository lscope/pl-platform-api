from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import Engine

from .env import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from .models.orm.users import User


db_url: str = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine: Engine = create_engine(db_url)


def populate_db() -> None:
    """Create DB tables.
    """
    SQLModel.metadata.create_all(bind=engine)

def get_sql_session():
    """Get SQL session.

    Yields:
        Session: SQL session
    """
    with Session(bind=engine) as session:
        yield session
