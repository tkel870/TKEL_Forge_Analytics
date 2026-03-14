"""
Analysis module for the FORGE tool.

This module computes revenue and profit metrics, customer concentration,
product performance, and business-risk warnings from cleaned sales data.
"""


def analyze(df, mode):
    """
    Analyze cleaned sales data and return summary metrics and product performance.

    Args:
        df (pandas.DataFrame): Cleaned transaction dataset.
        mode (str): Analysis mode. Supported values are "revenue" and "profit".

    Returns:
        tuple:
            dict: Summary metrics and warning messages.
            pandas.DataFrame: Product-level aggregated performance table.
    """

    # Validate the selected analysis mode before running calculations
    if mode not in ["revenue", "profit"]:
        raise ValueError("mode must be 'revenue' or 'profit'")

    print("Running analysis...")

    # Store warning messages that flag business risk
    warnings = []

    # -------------------------
    # Overall Metrics
    # -------------------------

    # Calculate total revenue across the full dataset
    total_revenue = df["revenue"].sum()
    print(f"Total Revenue: {total_revenue}")

    # -------------------------
    # Customer Analysis
    # -------------------------

    # Aggregate revenue by customer to measure customer contribution
    revenue_by_customer = df.groupby("customer_id")["revenue"].sum()

    print("\nRevenue by Customer:")
    print(revenue_by_customer)

    # Identify the customer generating the highest total revenue
    top_customer = revenue_by_customer.idxmax()
    top_customer_revenue = revenue_by_customer.max()

    print("\nTop Customer by Revenue:")
    print(f"{top_customer} (Revenue: {top_customer_revenue})")

    # Measure how dependent total revenue is on the top customer
    customer_revenue_percent = (
        (top_customer_revenue / total_revenue) * 100
        if total_revenue != 0 else 0
    )

    print("\nCustomer Revenue Concentration:")
    print(f"{customer_revenue_percent:.1f}% of total revenue comes from {top_customer}")

    # Flag customer concentration risk when one customer drives most revenue
    if customer_revenue_percent > 50:
        warning = "WARNING: Revenue is heavily concentrated in a single customer."
        warnings.append(warning)
        print(warning)

    # -------------------------
    # Product Revenue Analysis
    # -------------------------

    # Aggregate revenue by product to compare product sales performance
    revenue_by_product = df.groupby("product_id")["revenue"].sum()

    print("\nRevenue by Product:")
    print(revenue_by_product)

    # -------------------------
    # Revenue Mode
    # -------------------------

    # In revenue mode, return revenue-focused product metrics only
    if mode == "revenue":
        product_performance = df.groupby("product_id").agg({
            "revenue": "sum"
        }).reset_index()

        # Identify the highest revenue-generating product
        top_product = revenue_by_product.idxmax()
        top_revenue = revenue_by_product.max()

        print("\nTop Performing Product by Revenue:")
        print(f"{top_product} (Revenue: {top_revenue})")

        print("Analysis complete.")

        results = {
            "total_revenue": total_revenue,
            "top_customer": top_customer,
            "top_customer_revenue": top_customer_revenue,
            "customer_revenue_percent": customer_revenue_percent,
            "top_product": top_product,
            "top_revenue": top_revenue,
            "warnings": warnings
        }

        return results, product_performance

    # -------------------------
    # Profit Mode
    # -------------------------

    # Work on a copy so the original cleaned dataset is not modified in place
    df = df.copy()

    # Calculate profit for each transaction
    df["profit"] = df["revenue"] - df["cost"]

    # Calculate overall cost and profit totals
    total_cost = df["cost"].sum()
    total_profit = df["profit"].sum()

    print(f"Total Cost: {total_cost}")
    print(f"Total Profit: {total_profit}")

    # Aggregate profit by product to compare product profitability
    profit_by_product = df.groupby("product_id")["profit"].sum()

    # Build a product performance table for reporting and export
    product_performance = df.groupby("product_id").agg({
        "revenue": "sum",
        "cost": "sum",
        "profit": "sum"
    }).reset_index()

    print("\nProfit by Product:")
    print(profit_by_product)

    print("\nTop Products by Profit:")
    print(profit_by_product.sort_values(ascending=False).head(3))

    # Identify the most profitable product
    top_product = profit_by_product.idxmax()
    top_profit = profit_by_product.max()

    print("\nTop Performing Product:")
    print(f"{top_product} (Profit: {top_profit})")

    # Identify the least profitable product
    worst_product = profit_by_product.idxmin()
    worst_profit = profit_by_product.min()

    print("\nWorst Performing Product:")
    print(f"{worst_product} (Profit: {worst_profit})")

    # Measure how dependent total profit is on the top product
    profit_percent = (
        (top_profit / total_profit) * 100
        if total_profit != 0 else 0
    )

    print("\nProfit Concentration:")
    print(f"{profit_percent:.1f}% of total profit comes from {top_product}")

    # Flag product concentration risk when one product drives most profit
    if profit_percent > 50:
        warning = "WARNING: Profit is heavily concentrated in a single product."
        warnings.append(warning)
        print(warning)

    # Identify products that generate negative total profit
    negative_margin_products = product_performance[
        product_performance["profit"] < 0
    ]

    # Flag any products with negative margins
    if not negative_margin_products.empty:
        bad_products = negative_margin_products["product_id"].tolist()
        warning = f"WARNING: Negative margin detected in products: {', '.join(bad_products)}"
        warnings.append(warning)
        print(warning)

    # Notify the CLI that the FORGE analysis pipeline has completed
    print("Analysis complete.")

    # -------------------------
    # Build Final Results Summary
    # -------------------------
    # Package the key metrics calculated during analysis into a results
    # dictionary. This structure is returned to the CLI and later used
    # by the FORGE reporting and recommendation modules.

    results = {
        # Overall financial performance
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "total_profit": total_profit,

        # Customer concentration metrics
        "top_customer": top_customer,
        "top_customer_revenue": top_customer_revenue,
        "customer_revenue_percent": customer_revenue_percent,

        # Product performance metrics
        "top_product": top_product,
        "top_profit": top_profit,
        "worst_product": worst_product,
        "worst_profit": worst_profit,

        # Profit concentration risk indicator
        "profit_percent": profit_percent,

        # List of warning messages generated during analysis
        "warnings": warnings
    }

    # Return the summary metrics along with the product-level
    # performance table used for reporting and chart generation
    return results, product_performance
