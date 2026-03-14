# TKEL Forge Analytics Engine (FORGE)

The **TKEL Forge Analytics Engine (FORGE)** is a command-line business analytics tool designed to analyze sales datasets and generate actionable insights for decision makers.

The project demonstrates how a **structured analytics pipeline** can transform raw business data into meaningful analysis, risk detection, and strategic recommendations.

FORGE was developed as the **final project for Harvard’s CS50x** and simulates the type of modular analytics workflow commonly used in real-world data environments.

---

# Project Overview

Businesses collect large volumes of operational and sales data, but turning that data into useful insights is often difficult.

Decision makers frequently need answers to questions such as:

- Which products generate the most profit?
- Which customers contribute the most revenue?
- Are there risks from over-reliance on a single product or customer?
- Are products being sold at a negative margin?

FORGE automatically analyzes datasets to answer these questions and produces **reports, visualizations, and recommendations** that highlight potential risks and opportunities.

---

# How the Program Works

The tool is executed from the command line:


python cli.py --file data/raw/sample.csv --mode profit


Arguments:

| Argument | Description |
|--------|-------------|
| `--file` | Path to the dataset |
| `--mode` | Determines analysis type (profit or revenue) |

Once executed, the program runs the full analytics pipeline.

---

# Analytics Pipeline

The FORGE engine processes data through several modular stages:

### 1. Data Ingestion
`ingest.py` loads the dataset from a CSV file and confirms row and column counts.

### 2. Dataset Profiling
`profile.py` analyzes the dataset structure and reports:

- row count
- column count
- missing values
- duplicate records

### 3. Dataset Validation
`validate.py` verifies that required fields exist before analysis begins.

### 4. Data Cleaning
`clean.py` prepares the dataset by:

- removing duplicates
- converting numeric columns
- parsing date fields

### 5. Data Analysis
`analyze.py` calculates key business metrics including:

- total revenue
- total cost
- total profit
- revenue by customer
- profit by product
- revenue concentration
- profit concentration

The system also detects risks such as:

- excessive reliance on one customer
- products with negative profit margins

### 6. Visualization
`visualize.py` generates charts illustrating analysis results.

Currently implemented:
- Profit by product bar chart

Charts are saved as image files.

### 7. Strategic Recommendations
`recommend.py` generates executive-level insights when risk conditions are detected.

Example:
If a single product generates over 50% of total profit, the system recommends diversification.

### 8. Report Generation
`export.py` produces structured output including:

- summary CSV files
- text-based analysis reports

These are saved in the `outputs/` directory.

---

# Project Structure


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

data/
raw/

outputs/
reports/

tests/


Each module handles a **single responsibility** within the analytics pipeline.

---

# Design Decisions

Several architectural decisions shaped the design of FORGE.

### Modular Pipeline Architecture
Instead of writing one large script, the system was divided into independent modules representing stages of a data pipeline.

Benefits:

- easier maintenance
- clearer code structure
- easier expansion

### Command Line Interface
The project uses a command-line interface instead of a graphical interface to emphasize the underlying analytics logic while keeping the system lightweight.

### Extensibility
The architecture allows future features such as:

- forecasting models
- additional visualizations
- database integration
- machine learning analysis

---

# Conclusion

The **TKEL Forge Analytics Engine** demonstrates how programming and data analysis can work together to transform raw operational data into meaningful business insights.

The project reflects key concepts learned in CS50x including:

- modular programming
- structured data pipelines
- command-line interfaces
- data analysis workflows

FORGE provides a simplified example of how analytics systems can support decision-making through automated data processing, visualization, and insight generation.uding modular programming, data processing, command-line interfaces, and structured program design.
