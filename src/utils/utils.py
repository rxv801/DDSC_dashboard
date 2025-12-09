from sqlalchemy import create_engine


def get_engine():
    return create_engine("postgresql://rex@localhost:5432/DDSC")
