def explain_answer(metric, result, region=None, product=None):
    if metric == "total_sales":
        metric_name = "total sales"
    elif metric == "total_profit":
        metric_name = "total profit"
    elif metric == "profit_margin":
        metric_name = "profit margin"
    else:
        metric_name = metric

    filters = []
    if product is not None:
        filters.append(product)
    if region is not None:
        filters.append(region)

    if filters:
        description = " in ".join(filters)
        return f"The {metric_name} for {description} is {result}."

    return f"The {metric_name} is {result}."