import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("⚙️ Miscellaneous")

st.write("Drop the updated membership list here to process and update the database.")

uploaded_file = st.file_uploader("Choose an excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel("membership.xlsx")
    engine = create_engine("postgresql://rex@localhost:5432/DDSC")

    df.to_sql("members", engine, if_exists="replace")
