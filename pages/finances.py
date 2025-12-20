import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import streamlit as st
import pandas as pd
from src.utils.utils import get_engine

engine = get_engine()


@st.cache_data
def load_table(table_name, _engine):  # Note: _engine to prevent hashing
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, _engine)


st.title("💰 Finances")
df = load_table("finances", engine)
st.dataframe(df)

# Add transaction form
st.subheader("Add New Transaction")
with st.form("add_transaction"):
    date = st.date_input("Date")
    category = st.text_input("Category")
    description = st.text_area("Description")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    trans_type = st.selectbox("Type", ["income", "expense"])

    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        from sqlalchemy import text

        query = text("""
        INSERT INTO finances (date, category, description, amount, type)
        VALUES (:date, :category, :description, :amount, :type)
        """)
        with engine.connect() as conn:
            conn.execute(
                query,
                {
                    "date": date,
                    "category": category,
                    "description": description,
                    "amount": amount,
                    "type": trans_type,
                },
            )
            conn.commit()
        st.success("Transaction added!")
        st.cache_data.clear()
        st.rerun()
