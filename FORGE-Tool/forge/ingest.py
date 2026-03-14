"""
Data ingestion module for the FORGE tool.

This module is responsible for loading external datasets into pandas
DataFrames so they can be processed by the FORGE analytics pipeline.
"""

import pandas as pd


def load_csv(file_path):
    """
    Load a CSV dataset into a pandas DataFrame.

    Args:
        file_path (str):
            Path to the CSV file containing the dataset.

    Returns:
        pandas.DataFrame:
            The loaded dataset ready for profiling, validation,
            and analysis within the FORGE pipeline.
    """

    try:
        # Attempt to read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Confirm successful dataset loading
        print("Dataset successfully loaded.")

        # Provide quick dataset diagnostics for the user
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")

        # Return the DataFrame to the next stage of the FORGE pipeline
        return df

    except FileNotFoundError:
        # Handle cases where the specified file path does not exist
        print(f"Error: File not found → {file_path}")
        raise

    except Exception as e:
        # Catch any other loading errors (format issues, permissions, etc.)
        print(f"Error loading dataset: {e}")
        raise
