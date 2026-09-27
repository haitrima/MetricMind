from src.metrics import(
    load_data,
    total_sales,
    total_profit,
    profit_margin,
    sales_by_region,
    sales_by_product,
    profit_by_region,
    sales_by_month,
    top_sales_region,
    top_sales_product,
    top_profit_region
)

df = load_data()


print("Total Sales:",
total_sales(df))

print("Total Profit:",
total_profit(df))

print("Profit Margin:",
profit_margin(df))

print("Sales by Region:")
print(sales_by_region(df))

print("Sales by Product:")
print(sales_by_product(df))

print("Profit by Region:")
print(profit_by_region(df))

print("Sales by Month:")
print(sales_by_month(df))

print("Top Sales Region:")
print(top_sales_region(df))

print("Top Sales Product:")
print(top_sales_product(df))

print("Top Profit Region:")
print(top_profit_region(df))