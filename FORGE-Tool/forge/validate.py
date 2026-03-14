"""
Dataset validation module for the FORGE tool.

This module ensures that incoming datasets contain the required
structure and fields needed for the FORGE analytics pipeline.
"""


def validate(df):
    """
    Validate that the dataset contains all required columns.

    Args:
        df (pandas.DataFrame):
            Dataset loaded during the ingestion stage.

    Raises:
        ValueError:
            If any required column is missing from the dataset.

    Returns:
        None
    """

    # -------------------------
    # Required Dataset Columns
    # -------------------------
    # These fields are necessary for the FORGE analysis pipeline
    # to calculate revenue, profit, and customer/product metrics.
    required_columns = [
        "date",
        "revenue",
        "cost",
        "customer_id",
        "product_id",
        "category",
        "quantity"
    ]

    # -------------------------
    # Validate Column Presence
    # -------------------------
    # Ensure each required column exists in the dataset.
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Notify the user that validation has passed successfully
    print("Dataset validation passed.")
