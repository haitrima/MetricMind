from src.question_parser import parse_question
from src.metric_runner import run_metric

def answer_question(question):
    parsed = parse_question(question)
    metric = parsed["metric"]
    region = parsed["region"]

    if metric is None:
        return "Sorry, I could not understand the business metric."

    return run_metric(metric,region)

    if result is None:
        return "Sorry, I could not calculate the requested metric."

    if metric == "total_sales":
        metric_name = "Total Sales"
    elif metric == "total_profit":
        metric_name = "Total Profit"
    elif metric == "profit_margin":
        metric_name = "Profit Margin"
    else:
        metric_name = metric

    if region is not None:
            return f"{metric_name} in {region}: {result}"
    
    else: return f"{metric_name}: {result}"