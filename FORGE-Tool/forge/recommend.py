"""
Recommendation module for the FORGE tool.

This module generates strategic recommendations based on the results
of the FORGE analysis pipeline. Recommendations are intended to help
users interpret risk indicators and identify potential business actions.
"""


def generate_recommendations(results):
    """
    Generate executive recommendations based on analysis results.

    Args:
        results (dict):
            Summary metrics and warning messages returned by the FORGE
            analysis module.

    Returns:
        list:
            A list of recommendation strings intended for business users.
    """

    # Store recommendations generated from detected risks
    recommendations = []

    # -------------------------
    # Profit Concentration Risk
    # -------------------------
    # If a single product generates more than 50% of total profit,
    # suggest diversifying revenue across additional products.
    if results.get("profit_percent", 0) > 50:
        recommendations.append(
            f"Reduce dependency on product {results['top_product']}. "
            "Consider expanding sales of other products to diversify profit."
        )

    # -------------------------
    # Customer Concentration Risk
    # -------------------------
    # If one customer generates a majority of revenue, recommend
    # expanding the customer base to reduce financial risk.
    if results.get("customer_revenue_percent", 0) > 50:
        recommendations.append(
            "Revenue is heavily concentrated in a single customer. "
            "Consider expanding the customer base to reduce risk."
        )

    # -------------------------
    # Negative Margin Detection
    # -------------------------
    # If analysis warnings indicate negative margins, recommend
    # investigating pricing strategy or cost structure.
    if "warnings" in results:
        for warning in results["warnings"]:
            if "Negative margin" in warning:
                recommendations.append(
                    "Investigate pricing or cost structure for products generating negative margins."
                )

    # Return the list of generated recommendations
    return recommendations
