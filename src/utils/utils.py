import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def get_engine():
    db_url = os.getenv("DATABASE_URL", "postgresql://localhost:5432/DDSC")
    return create_engine(db_url)