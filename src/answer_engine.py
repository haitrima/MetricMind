from src.question_parser import parse_question
from src.metric_runner import run_metric

def answer_question(question):
    parsed = parse_question(question)
    metric = parsed["metric"]
    region = parsed["region"]

    if metric is None:
        return None

    return run_metric(metric,region)