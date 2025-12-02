import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

engine = create_engine("postgresql://rex@localhost:5432/DDSC")

df = pd.read_sql("SELECT * FROM MEMBERS", engine)
df["Last Paid Date"] = pd.to_datetime(df["Last Paid Date"])
df["Last Paid month"] = df["Last Paid Date"].dt.to_period("M")

monthly_members = df.groupby("Last Paid month").size().reset_index()
monthly_members.columns = ["Last Paid month", "Member_Count"]

monthly_members["month_numb"] = range(1, len(monthly_members) + 1)

X = monthly_members[["month_numb"]]
Y = monthly_members["Member_Count"]

model = LinearRegression()
model.fit(X, Y)

next_month = len(monthly_members) + 1
prediction = model.predict([[next_month]])

print(f"Predicted member count for next month: {int(prediction[0])}")
