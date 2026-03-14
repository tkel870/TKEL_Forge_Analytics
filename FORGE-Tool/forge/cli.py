"""
Command Line Interface for the FORGE tool.

This module serves as the entry point for running the FORGE analytics pipeline.
It loads the dataset, performs validation and cleaning, runs the analysis,
generates charts and recommendations, and exports the final reports.
"""

import argparse
from forge.ingest import load_csv
from forge.validate import validate
from forge.clean import clean
from forge.analyze import analyze
from forge.export import export_txt_report, export_csv_summary
from forge.profile import profile_dataset
from forge.recommend import generate_recommendations
from forge.visualize import generate_charts


def run_cli():
    """
    Execute the full FORGE analysis pipeline from the command line.

    This function parses user inputs, loads the dataset, runs each stage of
    the analytics pipeline, and generates the final outputs including charts,
    recommendations, and report files.
    """

    # -------------------------
    # Parse Command Line Arguments
    # -------------------------
    # Users must provide the dataset path and select an analysis mode.
    parser = argparse.ArgumentParser(description="FORGE Analytics Tool")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to CSV file"
    )

    parser.add_argument(
        "--mode",
        required=True,
        choices=["profit", "revenue"],
        help="Analysis mode"
    )

    args = parser.parse_args()

    # -------------------------
    # Display Startup Information
    # -------------------------
    # Inform the user which dataset and analysis mode are being used.
    print("FORGE Tool Starting...")
    print(f"File: {args.file}")
    print(f"Mode: {args.mode}")

    # -------------------------
    # Load Dataset
    # -------------------------
    # Read the CSV file into a pandas DataFrame.
    df = load_csv(args.file)

    # -------------------------
    # Dataset Profiling
    # -------------------------
    # Provide a quick diagnostic overview of the dataset.
    profile_dataset(df)

    # -------------------------
    # Validate Dataset
    # -------------------------
    # Ensure required columns and basic structure are present.
    validate(df)

    # -------------------------
    # Clean Dataset
    # -------------------------
    # Prepare the data for analysis by handling formatting issues.
    df = clean(df)

    # -------------------------
    # Run Core FORGE Analysis
    # -------------------------
    # Generate summary metrics and product performance results.
    results, product_performance = analyze(df, args.mode)

    # -------------------------
    # Generate Visualization Outputs
    # -------------------------
    # Create charts from the analysis results.
    generate_charts(product_performance)

    # -------------------------
    # Generate Executive Recommendations
    # -------------------------
    # Use analysis results to produce strategic suggestions.
    recommendations = generate_recommendations(results)

    if recommendations:
        print("\nExecutive Recommendations")
        print("-------------------------")

        for rec in recommendations:
            print(f"• {rec}")

    # -------------------------
    # Export Reports
    # -------------------------
    # Save results to report files for review and distribution.
    export_txt_report(results)
    export_csv_summary(product_performance)


# -------------------------
# CLI Entry Point
# -------------------------
# Allows the module to be executed directly from the command line.
if __name__ == "__main__":
    run_cli()
