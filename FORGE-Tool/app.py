"""
FORGE entry point.

This script allows the FORGE tool to be executed directly from the
project root. It simply imports the CLI runner and starts the pipeline.
"""

from cli import run_cli


# -------------------------
# Program Entry Point
# -------------------------
# When this script is executed directly, start the FORGE CLI pipeline.
if __name__ == "__main__":
    run_cli()
