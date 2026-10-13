from src.metrics import load_data
from src.query_engine import find_metric, find_dimension


def run_metric(metric_name, region=None, product=None):
    df = load_data()

    metric = find_metric(metric_name)

    if metric is None:
        return None

    if region is not None:
        dimension = find_dimension("region")
        if dimension is None:
            return None
        column = dimension["column"]
        df = df[df[column].astype(str).str.strip().str.lower() == region.strip().lower()]

    if product is not None:
        dimension = find_dimension("product")
        if dimension is None:
            return None
        column = dimension["column"]
        df = df[df[column].astype(str).str.strip().str.lower() == product.strip().lower()]

    if df.empty:
        return 0

    if "formula" in metric:
        total_profit_value = df["Profit"].sum()
        total_sales_value = df["Sales"].sum()

        if total_sales_value == 0:
            return 0

        return (total_profit_value / total_sales_value) * 100

    column = metric["column"]
    aggregation = metric["aggregation"]

    if aggregation == "sum":
        return df[column].sum()

    return None