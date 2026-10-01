def explain_answer(metric, result, region=None):
    if metric == "total_sales":
        metric_name = "total sales"
    elif metric == "total_profit":
        metric_name = "total profit"
    elif metric == "profit_margin":
        metric_name = "profit margin"
    else: metric_name = metric


    if region is not None:
        return f"The {metric_name} in {region} is {result}."
    else:
        return f"The {metric_name} is {result}."  