def parse_question(question):
    question = question.lower()

    metric = None
    region = None
    product = None

    # Identify the requested metric
    if "profit margin" in question or "margin" in question:
        metric = "profit_margin"
    elif "profit" in question:
        metric = "total_profit"
    elif "sales" in question or "revenue" in question:
        metric = "total_sales"

    # Identify the region
    if "europe" in question:
        region = "Europe"
    elif "asia" in question:
        region = "Asia"
    elif "north america" in question:
        region = "North America"

    # Identify the product
    if "laptop" in question:
        product = "Laptop"
    elif "phone" in question:
        product = "Phone"
    elif "monitor" in question:
        product = "Monitor"

    return {
        "metric": metric,
        "region": region,
        "product": product,
    }