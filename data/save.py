from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()


def save():
    user = os.getenv('DB_USER')
    pw = os.getenv('DB_PASS')
    name = os.getenv("DB_NAME")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    connstring = f"mysql+pymysql://{user}:{pw}@{host}:{port}/{name}?charset=utf8"
    engine = create_engine(connstring, pool_recycle=3600)

    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())
