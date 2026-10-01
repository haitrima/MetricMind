import matplotlib.pyplot as plt
def plot_sales_by_region(df, region=None):
    if region is not None:
        df = df[df["Region"] == region]

    sales = df.groupby("Region")["Sales"].sum()

    sales.plot(kind="bar")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()