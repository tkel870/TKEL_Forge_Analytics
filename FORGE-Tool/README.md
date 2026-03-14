TKEL Forge Analytics Engine
Video Demo: <VIDEO URL HERE>
Description:

The TKEL Forge Analytics Engine (FORGE) is a command-line business analytics tool designed to analyze sales data and generate actionable insights for decision makers. The goal of this project is to demonstrate how structured data pipelines can be used to transform raw business data into meaningful analysis, risk detection, and strategic recommendations.

FORGE was built as the final project for CS50x and was designed to simulate the type of analytics pipeline commonly used in real-world data analysis environments. The tool processes a dataset step-by-step, performing data ingestion, profiling, validation, cleaning, analysis, visualization, and reporting.

The system is designed with a modular architecture so that each stage of the analytics pipeline is handled by a dedicated module. This approach makes the system easier to maintain, expand, and understand.

Problem the Project Solves

Businesses frequently collect large amounts of operational and sales data, but turning that data into meaningful insights can be difficult. Decision makers often need answers to questions such as:

Which products generate the most profit?

Which customers contribute the most revenue?

Are there business risks such as over-reliance on a single customer or product?

Are there products being sold at a negative margin?

FORGE addresses these questions by automatically analyzing a dataset and producing structured insights, charts, and recommendations that highlight potential risks and opportunities.

How the Program Works

The tool is executed from the command line using the following command:

python cli.py --file data/raw/sample.csv --mode profit

The --file argument specifies the dataset to analyze, and the --mode argument determines whether the analysis focuses on revenue or profit.

When the program runs, it executes the full FORGE analytics pipeline.

The pipeline includes the following stages:

1. Data Ingestion

The dataset is loaded from a CSV file using the ingest.py module. This step ensures the file is successfully loaded and reports the number of rows and columns.

2. Dataset Profiling

The profile.py module performs a quick diagnostic review of the dataset, reporting the number of rows, columns, missing values, and duplicate records. This provides immediate visibility into potential data quality issues.

3. Dataset Validation

The validate.py module ensures that the dataset contains the required fields necessary for the analysis. If any required columns are missing, the program stops with a clear error message.

4. Data Cleaning

The clean.py module prepares the dataset for analysis by removing duplicate rows, converting numeric fields to proper data types, and converting date values into datetime objects.

5. Data Analysis

The analyze.py module performs the core analytics calculations. It computes metrics such as:

Total revenue

Total cost

Total profit

Revenue by customer

Profit by product

Customer revenue concentration

Product profit concentration

The analysis also detects risk conditions such as heavy reliance on a single product or customer and products generating negative margins.

6. Visualization

The visualize.py module generates charts that help illustrate the results of the analysis. Currently, the tool generates a bar chart showing profit by product and saves it as an image file.

7. Strategic Recommendations

The recommend.py module evaluates the analysis results and generates executive-level recommendations when risks are detected. For example, if a single product generates more than half of total profit, the tool recommends diversifying revenue sources.

8. Report Generation

Finally, the export.py module generates output files including a text report and a CSV summary of product performance.

These files are saved in the outputs directory.

Project Structure

The project is organized into several directories and modules:

forge/
    ingest.py
    profile.py
    validate.py
    clean.py
    analyze.py
    recommend.py
    visualize.py
    export.py
    cli.py

Each module performs a single responsibility within the analytics pipeline.

Additional folders include:

data/       → raw datasets used for analysis
outputs/    → generated charts and reports
tests/      → testing scripts
Design Decisions

One of the primary design decisions was to build the project as a modular analytics pipeline instead of a single large script. This allows each component of the system to be developed independently while keeping the codebase organized and readable.

Another design choice was to implement the tool as a command-line application rather than a graphical interface. This approach keeps the system lightweight while demonstrating the underlying analytics logic clearly.

The modular architecture also allows the tool to be easily expanded in the future. Additional features such as more advanced visualizations, forecasting models, or integration with databases could be added without significantly altering the existing pipeline.

Conclusion

The TKEL Forge Analytics Engine demonstrates how programming can be used to transform raw data into meaningful insights. By combining data processing, analysis, visualization, and automated recommendations, the project provides a simplified example of a real-world analytics workflow.

The project reflects many of the core concepts learned in CS50x, including modular programming, data processing, command-line interfaces, and structured program design.
