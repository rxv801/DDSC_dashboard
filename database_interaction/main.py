import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel("membership.xlsx")
engine = create_engine("postgresql://rex@localhost:5432/DDSC")

df.to_sql("members", engine, if_exists="replace")
