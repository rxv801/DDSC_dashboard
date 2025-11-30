import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


@st.cache_data
def load_table(table_name):
    engine = create_engine("postgresql://rex@localhost:5432/DDSC")
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, engine)


st.title("📊 Membership")
df = load_table("members")
st.dataframe(df)
