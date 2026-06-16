import streamlit as st
from utils import load_inventory, load_trends
from scoring import calculate_inventory_risk
from recommendation_engine import generate_discount_recommendations
from dashboard import render_dashboard
from insights import generate_ai_insights

st.set_page_config(
    page_title="InvenSense AI",
    layout="wide"
)

st.title("🧠 InvenSense AI")
st.caption("AI-powered inventory intelligence for fast fashion retailers")

# Sidebar Controls
st.sidebar.header("Risk Threshold Controls")

sales_threshold = st.sidebar.slider(
    "Minimum Healthy Weekly Sales",
    1,
    50,
    15
)

stock_threshold = st.sidebar.slider(
    "Maximum Healthy Stock",
    10,
    500,
    150
)

trend_threshold = st.sidebar.slider(
    "Minimum Healthy Trend Score",
    0,
    100,
    60
)

inventory_df = load_inventory()
trends_df = load_trends()

scored_df = calculate_inventory_risk(
    inventory_df,
    trends_df,
    sales_threshold,
    stock_threshold,
    trend_threshold
)

recommendations_df = generate_discount_recommendations(scored_df)

render_dashboard(scored_df)

st.subheader("📉 Discount Simulator")

discount_adjustment = st.slider(
    "Adjust Discount %",
    0,
    50,
    20
)

sim_df = recommendations_df.copy()
sim_df["Adjusted Price"] = sim_df["selling_price"] * (
    1 - discount_adjustment / 100
)

sim_df["Estimated Margin"] = (
    sim_df["Adjusted Price"] - sim_df["cost_price"]
)

st.dataframe(sim_df)

st.subheader("🤖 AI Insights")
insights = generate_ai_insights(scored_df)

for insight in insights:
    st.info(insight)