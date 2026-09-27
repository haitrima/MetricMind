from src.metrics import(
    load_data,
    total_sales,
    total_profit,
    profit_margin,
    sales_by_region,
    sales_by_product,
    profit_by_region,
    sales_by_month
)

df = load_data()


print("Total Sales:",
    total_sales(df))

print("Total Profit:",
    total_profit(df))