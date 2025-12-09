import pandas as pd
from sklearn.linear_model import LinearRegression


def prepare_monthly_data(engine):
    df = pd.read_sql("SELECT * FROM MEMBERS", engine)
    df["Last Paid Date"] = pd.to_datetime(df["Last Paid Date"])
    df["Last Paid month"] = df["Last Paid Date"].dt.to_period("M")
    monthly_members = df.groupby("Last Paid month").size().reset_index()
    monthly_members.columns = ["Last Paid month", "Member_Count"]
    monthly_members["month_numb"] = range(1, len(monthly_members) + 1)
    return monthly_members


def train_membership_model(monthly_members):
    X = monthly_members[["month_numb"]]
    Y = monthly_members["Member_Count"]
    model = LinearRegression()
    model.fit(X, Y)
    return model


def predict_next_month_members(model, monthly_members):
    next_month = len(monthly_members) + 1
    prediction = model.predict([[next_month]])
    return prediction
