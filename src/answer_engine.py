from src.question_parser import parse_question
from src.metric_runner import run_metric
from src.explanation_engine import explain_answer

def answer_question(question):
    parsed = parse_question(question)
    metric = parsed["metric"]
    region = parsed["region"]
    product = parsed["product"]

    if metric is None:
       return "Sorry, I could not understand the business metric."

    result = run_metric(metric, region, product)

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

    return explain_answer(metric, result, region) 