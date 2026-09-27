import pandas as pd


def load_data():
    return pd.read_csv("data/sales_data.csv")


def total_sales(df):
    return df["Sales"].sum()


def total_profit(df):
    return df["Profit"].sum()


def sales_by_region(df):
    return df.groupby("Region")["Sales"].sum()



def sales_by_product(df):
    return df.groupby("Product")["Sales"].sum()

def profit_by_region(df):
    return df.groupby("Region")["Profit"].sum()

def profit_margin(df):
    return(df["Profit"].sum()/df["Sales"].sum())*100


def sales_by_month(df):
    df["Date"] = pd.to_datetime(df["Date"])
    return df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()


def profit_margin(df):
    return (df["Profit"].sum()/
df["Sales"].sum())*100

def top_sales_region(df):
    return df.groupby("Region")["Sales"].sum().idxmax()

def top_sales_product(df):
    return df.groupby("Product")["Sales"].sum().idxmax()

def top_profit_region(df):
    return df.groupby("Region")["Profit"].sum().idxmax()