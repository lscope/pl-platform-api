from annotated_types import Gt
from typing import Annotated
from pydantic_settings import BaseSettings



class Db(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str
    postgres_port: Annotated[int, Gt(gt=0)]

db: Db = Db()

DB_USERNAME: str = db.postgres_user
DB_PASSWORD: str = db.postgres_password
DB_HOST: str = db.postgres_host
DB_NAME: str = db.postgres_db
DB_PORT: int = db.postgres_port