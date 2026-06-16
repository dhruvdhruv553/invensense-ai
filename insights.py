def generate_ai_insights(df):
    insights = []

    at_risk = df[df["risk_status"] == "At Risk 🔴"]

    for _, row in at_risk.iterrows():
        insights.append(
            f"{row['category']} inventory is accumulating faster "
            f"than sales. Trend direction is "
            f"{row['trend_direction']}. Early markdown action "
            f"could preserve margin."
        )

    if len(insights) == 0:
        insights.append(
            "Inventory health is currently stable across all categories."
        )

    return insights