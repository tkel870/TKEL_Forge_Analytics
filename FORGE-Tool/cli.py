"""
FORGE command-line interface.

This module runs the complete FORGE analytics pipeline including
data ingestion, validation, cleaning, analysis, visualization,
recommendations, and report exports.
"""

import argparse
from forge.ingest import load_csv
from forge.profile import profile_dataset
from forge.validate import validate
from forge.clean import clean
from forge.analyze import analyze
from forge.visualize import generate_charts
from forge.recommend import generate_recommendations
from forge.export import export_txt_report, export_csv_summary


def run_cli():
    """
    Execute the FORGE analytics pipeline from the command line.
    """

    # -------------------------
    # Parse CLI Arguments
    # -------------------------
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
    # Startup Information
    # -------------------------
    print("FORGE Tool Starting...")
    print(f"File: {args.file}")
    print(f"Mode: {args.mode}")

    # -------------------------
    # Load Dataset
    # -------------------------
    df = load_csv(args.file)

    # -------------------------
    # Profile Dataset
    # -------------------------
    profile_dataset(df)

    # -------------------------
    # Validate Dataset Structure
    # -------------------------
    validate(df)

    # -------------------------
    # Clean Dataset
    # -------------------------
    df = clean(df)

    # -------------------------
    # Run Analysis
    # -------------------------
    results, product_performance = analyze(df, args.mode)

    # -------------------------
    # Generate Charts
    # -------------------------
    generate_charts(product_performance)

    # -------------------------
    # Generate Recommendations
    # -------------------------
    recommendations = generate_recommendations(results)

    if recommendations:
        print("\nExecutive Recommendations")
        print("-------------------------")

        for rec in recommendations:
            print(f"• {rec}")

    # -------------------------
    # Export Reports
    # -------------------------
    export_txt_report(results)
    export_csv_summary(product_performance)


# -------------------------
# Entry Point
# -------------------------
if __name__ == "__main__":
    run_cli()
