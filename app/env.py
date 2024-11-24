from annotated_types import Gt
from typing import Annotated
from pydantic_settings import BaseSettings



class Db(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_name: str
    db_port: Annotated[int, Gt(gt=0)]


db: Db = Db()

DB_USERNAME: str = db.db_username
DB_PASSWORD: str = db.db_password
DB_HOST: str = db.db_host
DB_NAME: str = db.db_name
DB_PORT: int = db.db_port
