import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from model.training import (
    train_membership_model,
    predict_next_month_members,
    prepare_monthly_data,
)
import plotly.express as px

engine = create_engine("postgresql://rex@localhost:5432/DDSC")


@st.cache_data
def load_table(table_name, engine=engine):
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, engine)


st.title("📊 Membership")
df = load_table("members")
st.dataframe(df)

monthly_data = prepare_monthly_data(engine)
training_model = train_membership_model(monthly_data)
next_month_prediction = predict_next_month_members(training_model, monthly_data)


def plot_monthly_membership(monthly_data):
    monthly_data = monthly_data.copy()
    monthly_data["Last Paid month"] = monthly_data["Last Paid month"].astype(str)
    fig = px.line(
        monthly_data,
        x="Last Paid month",
        y="Member_Count",
        title="Monthly Membership Over Time",
    )
    return fig


st.plotly_chart(plot_monthly_membership(monthly_data))
