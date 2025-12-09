import streamlit as st
import pandas as pd
from src.utils.utils import get_engine


st.title("⚙️ Miscellaneous")

st.write("Drop the updated membership list here to process and update the database.")

uploaded_file = st.file_uploader("Choose an excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    engine = get_engine()

    df.to_sql("members", engine, if_exists="replace")

    st.cache_data.clear()
    st.success("Membership data updated successfully!")
