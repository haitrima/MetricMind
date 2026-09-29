from src.metrics import load_data
from src.query_engine import find_metric

def run_metric(metric_name):
    df = load_data()
    metric = find_metric(metric_name)

    if metric is None:
        return None

    if "formula" in metric:
        total_profit = df["Profit"].sum()
        total_sales = df["Sales"].sum()
        return (total_profit / total_sales) * 100

    column = metric["column"]
    aggregation = metric["aggregation"]

    if aggregation == "sum":
        return df[column].sum()
        return None