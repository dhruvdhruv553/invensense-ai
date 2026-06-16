import pandas as pd


def calculate_inventory_risk(
    inventory_df,
    trends_df,
    sales_threshold,
    stock_threshold,
    trend_threshold
):
    df = inventory_df.merge(
        trends_df,
        on="category",
        how="left"
    )

    risk_status = []

    for _, row in df.iterrows():
        if (
            row["weekly_units_sold"] >= sales_threshold
            and row["stock_remaining"] <= stock_threshold
            and row["trend_score"] >= trend_threshold
        ):
            risk_status.append("Healthy 🟢")

        elif (
            row["weekly_units_sold"] < sales_threshold
            and row["stock_remaining"] > stock_threshold
        ):
            risk_status.append("At Risk 🔴")

        else:
            risk_status.append("Watch 🟡")

    df["risk_status"] = risk_status

    df["inventory_value"] = (
        df["stock_remaining"] * df["cost_price"]
    )

    df["gross_margin"] = (
        (df["selling_price"] - df["cost_price"])
        * df["weekly_units_sold"]
    )

    return df