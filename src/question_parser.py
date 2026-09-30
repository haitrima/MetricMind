def parse_question(question):
    question = question.lower()

    metric = None
    region = None

    if "sales" in question:
        metric = "total_sales"
    elif "profit margin" in question:
        metric = "profit_margin"
    elif "profit" in question:
        metric = "total_profit"

    

    if "europe" in question:
            region = "Europe"
    elif "asia" in question:
            region = "Asia"
    elif "north america" in question:
            region = "North America"
    

    return {"metric": metric, "region": region}