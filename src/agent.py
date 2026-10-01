from src.question_parser import parse_question
from src.answer_engine import answer_question

def run_agent(question):
    parsed = parse_question(question)
    if parsed["metric"] is None:
        return "Sorry, I could not understand the business question."

    return answer_question(question)