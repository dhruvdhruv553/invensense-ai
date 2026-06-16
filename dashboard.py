import streamlit as st
import plotly.express as px


def render_dashboard(df):
    st.subheader("📊 Executive Dashboard")

    total_inventory_value = df["inventory_value"].sum()
    total_margin = df["gross_margin"].sum()

    healthy_count = len(df[df["risk_status"] == "Healthy 🟢"])
    watch_count = len(df[df["risk_status"] == "Watch 🟡"])
    risk_count = len(df[df["risk_status"] == "At Risk 🔴"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Inventory Value", f"${total_inventory_value:,.0f}")
    col2.metric("Gross Margin", f"${total_margin:,.0f}")
    col3.metric("Healthy Items", healthy_count)
    col4.metric("At Risk Items", risk_count)

    pie = px.pie(
        df,
        names="risk_status",
        title="Inventory Health"
    )

    bar = px.bar(
        df,
        x="category",
        y="stock_remaining",
        color="risk_status",
        title="Risk Distribution"
    )

    trend = px.bar(
        df,
        x="category",
        y="trend_score",
        title="Trend Score"
    )

    discount = px.bar(
        df[df["risk_status"] != "Healthy 🟢"],
        x="item_name",
        y="stock_remaining",
        title="Discount Opportunities"
    )

    st.plotly_chart(pie, use_container_width=True)
    st.plotly_chart(bar, use_container_width=True)
    st.plotly_chart(trend, use_container_width=True)
    st.plotly_chart(discount, use_container_width=True)