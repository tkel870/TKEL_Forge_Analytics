"""
Data cleaning module for the FORGE tool.

This module prepares raw datasets for analysis by removing duplicates,
standardizing data types, and ensuring key columns are correctly formatted.
"""

import pandas as pd


def clean(df):
    """
    Clean the dataset before running the FORGE analysis pipeline.

    Args:
        df (pandas.DataFrame):
            Raw dataset loaded from the CSV ingestion step.

    Returns:
        pandas.DataFrame:
            Cleaned dataset ready for analysis.
    """

    # Notify the user that the cleaning stage has started
    print("Cleaning dataset...")

    # -------------------------
    # Remove Duplicate Records
    # -------------------------
    # Drop rows that are exact duplicates to avoid double-counting
    # transactions in the analysis.
    df = df.drop_duplicates()

    # -------------------------
    # Convert Numeric Columns
    # -------------------------
    # Ensure numeric columns are properly interpreted as numbers.
    # Invalid values are converted to NaN so they do not break analysis.
    numeric_columns = ["revenue", "cost", "quantity"]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # -------------------------
    # Convert Date Column
    # -------------------------
    # Convert the date field to a datetime format so it can be used
    # for time-based analysis or future reporting features.
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Notify the CLI that the cleaning process has completed
    print("Cleaning complete.")

    # Return the cleaned dataset to the next stage of the FORGE pipeline
    return df
