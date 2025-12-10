import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime


def prepare_monthly_data(engine):
    # Load all members from database
    df = pd.read_sql("SELECT * FROM MEMBERS", engine)

    # Convert string dates to datetime objects
    df["Last Paid Date"] = pd.to_datetime(df["Last Paid Date"])

    # Extract just the year-month (e.g., 2025-01)
    df["Last Paid month"] = df["Last Paid Date"].dt.to_period("M")

    # Count how many members joined in each month
    monthly_counts = df.groupby("Last Paid month").size()

    # Convert to DataFrame with proper column names
    monthly_members = monthly_counts.reset_index()
    monthly_members.columns = ["Last Paid month", "Member_Count"]

    first_month = monthly_members["Last Paid month"].min()
    current_month = pd.Period(datetime.now(), freq="M")

    all_months = []

    loop_month = first_month

    while loop_month <= current_month:
        all_months.append(loop_month)
        loop_month += 1

    for loop_month in all_months:
        if loop_month not in monthly_members["Last Paid month"]:
            new_row = pd.DataFrame(
                {"Last Paid month": [loop_month], "Member_Count": [0]}
            )
            monthly_members = pd.concat([monthly_members, new_row], ignore_index=True)
            """
            Adds the new_row DataFrame to monthly_members by stacking them vertically.
            ignore_index=True renumbers all rows starting from 0.
            Like appending to a list, but for DataFrames.
            """
    monthly_members = monthly_members.sort_values("Last Paid month").reset_index(
        drop=True
    )

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
