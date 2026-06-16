def generate_discount_recommendations(df):
    recommendations = []

    for _, row in df.iterrows():
        if row["risk_status"] == "Watch 🟡":
            discount = 15
            action = "Within 14 days"

        elif row["risk_status"] == "At Risk 🔴":
            discount = 30
            action = "Immediate"

        else:
            discount = 0
            action = "None"

        explanation = (
            f"{row['category']} demand is "
            f"{row['trend_direction'].lower()} "
            f"with stock remaining at "
            f"{row['stock_remaining']} units."
        )

        recommendations.append({
            **row.to_dict(),
            "recommended_discount": discount,
            "action_window": action,
            "ai_explanation": explanation
        })

    return df.__class__(recommendations)