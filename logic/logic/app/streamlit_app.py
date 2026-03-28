import pandas as pd
import streamlit as st

from logic.risk_scoring import run_risk_analysis
from logic.ai_summary import generate_account_summary, generate_next_best_actions, generate_email_draft

st.set_page_config(page_title="Customer Health & Renewal Risk AI Assistant", layout="wide")

st.title("Customer Health & Renewal Risk AI Assistant")
st.write("Analyze customer health, predict renewal risk, and generate recommended next actions.")

# Load data
df = run_risk_analysis("customer_health_data.csv")

# Account selector
account_names = df["account_name"].tolist()
selected_account = st.selectbox("Select an account", account_names)

# Filter selected account
row = df[df["account_name"] == selected_account].iloc[0]

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Account Overview")
    st.metric("ARR", f"${row['arr']:,}")
    st.metric("Days to Renewal", int(row["days_to_renewal"]))
    st.metric("Risk Level", row["risk_level"])

    st.subheader("Health Signals")
    st.write(f"**License Utilization:** {row['license_utilization_percent']}%")
    st.write(f"**Support Tickets (90d):** {row['support_tickets_last_90_days']}")
    st.write(f"**High Severity Tickets:** {row['high_severity_tickets_last_90_days']}")
    st.write(f"**Product Adoption Score:** {row['product_adoption_score']}")
    st.write(f"**Executive Engagement Score:** {row['executive_engagement_score']}")
    st.write(f"**NPS Score:** {row['nps_score']}")
    st.write(f"**Login Frequency Score:** {row['login_frequency_score']}")
    st.write(f"**Training Completion:** {row['training_completion_percent']}%")
    st.write(f"**Open Escalations:** {row['open_escalations']}")
    st.write(f"**Region:** {row['region']}")
    st.write(f"**CSM:** {row['csm_name']}")

with col2:
    st.subheader("Risk Drivers")
    st.write(row["risk_reasons"])

    st.subheader("AI Account Summary")
    st.text_area("Summary", generate_account_summary(row), height=300)

    st.subheader("Recommended Next Actions")
    st.text(generate_next_best_actions(row))

    st.subheader("Draft Customer Email")
    st.text_area("Email Draft", generate_email_draft(row), height=220)
