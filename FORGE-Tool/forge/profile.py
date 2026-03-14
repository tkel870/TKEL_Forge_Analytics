"""
Dataset profiling module for the FORGE tool.

This module provides quick diagnostic information about a dataset
before it enters the main FORGE analysis pipeline. Profiling helps
identify potential issues such as missing values or duplicate records.
"""


def profile_dataset(df):
    """
    Generate a quick dataset profile for diagnostics.

    Args:
        df (pandas.DataFrame):
            Dataset loaded during the ingestion stage of the FORGE pipeline.

    Returns:
        None
    """

    # Display header for the dataset profiling section
    print("\nDataset Profile")
    print("---------------")

    # -------------------------
    # Dataset Size
    # -------------------------
    # Determine the number of rows and columns in the dataset
    rows, cols = df.shape

    print(f"Rows: {rows}")
    print(f"Columns: {cols}")

    # -------------------------
    # Missing Values
    # -------------------------
    # Count the total number of missing values across all columns
    missing_values = df.isnull().sum().sum()

    print(f"Missing Values: {missing_values}")

    # -------------------------
    # Duplicate Records
    # -------------------------
    # Identify duplicate rows that could affect analysis accuracy
    duplicate_rows = df.duplicated().sum()

    print(f"Duplicate Rows: {duplicate_rows}")

    # Notify the user that the profiling stage has completed
    print("Profile complete.\n")
