def parse_question(question):
    question = question.lower()

    metric = None
    region = None
    product = None

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

    if "laptop" in question or "laptops" in question:
                  product = "Laptop"
    elif "phone" in question or "phones" in question:
                  product = "Phone"
    elif "monitor" in question or "monitors" in question:
                  product = "Monitor"          
    

    return {"metric": metric, "region": region, "product": product}