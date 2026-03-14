"""
Visualization module for the FORGE tool.

This module generates chart outputs from the analysis results and saves
them to the outputs/charts directory for reporting and review.
"""

import matplotlib.pyplot as plt
from pathlib import Path


# Define the directory where generated charts will be saved
CHART_DIR = Path("outputs/charts")

# Create the charts directory if it does not already exist
CHART_DIR.mkdir(parents=True, exist_ok=True)


def generate_charts(product_performance):
    """
    Generate visualization charts from product performance data.

    Args:
        product_performance (pandas.DataFrame):
            Aggregated product-level metrics returned by the analysis module.

    Returns:
        None
    """

    # -------------------------
    # Profit by Product Chart
    # -------------------------
    # Only generate this chart if the dataset includes profit metrics.
    if "profit" in product_performance.columns:

        # Create a new matplotlib figure
        plt.figure()

        # Plot a bar chart showing profit for each product
        plt.bar(
            product_performance["product_id"],
            product_performance["profit"]
        )

        # Label the chart for readability
        plt.title("Profit by Product")
        plt.xlabel("Product")
        plt.ylabel("Profit")

        # Define the output file path
        chart_path = CHART_DIR / "profit_by_product.png"

        # Save the chart image to the outputs directory
        plt.savefig(chart_path)

        # Close the figure to free memory resources
        plt.close()

        # Notify the user that the chart was successfully created
        print(f"Chart generated: {chart_path}")
