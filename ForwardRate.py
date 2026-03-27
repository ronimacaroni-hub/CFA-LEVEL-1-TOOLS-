import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="Fixed Income Tool", page_icon="📈")

st.title("📈 Yield Curve & Forward Rate Calculator")
st.markdown("### CFA Level 1: Fixed Income Analysis")
st.write("This tool derives the term structure of interest rates and calculates implied forward rates.")

# Sidebar for Spot Rate Inputs
st.sidebar.header("Input Spot Rates (%)")
s1 = st.sidebar.number_input("1-Year Spot Rate (S1)", value=2.00, step=0.1)
s2 = st.sidebar.number_input("2-Year Spot Rate (S2)", value=2.50, step=0.1)
s3 = st.sidebar.number_input("3-Year Spot Rate (S3)", value=3.20, step=0.1)

# CFA L1 Formula for Forward Rates:
# (1 + S2)^2 = (1 + S1) * (1 + 1y1y)
f_1y1y = (((1 + s2/100)**2 / (1 + s1/100)) - 1) * 100

# (1 + S3)^3 = (1 + S2)^2 * (1 + 2y1y)
f_2y1y = (((1 + s3/100)**3 / (1 + s2/100)**2) - 1) * 100

# Prepare Data for Charting
chart_data = pd.DataFrame({
    "Maturity": ["1 Year", "2 Year", "3 Year"],
    "Spot Rate (%)": [s1, s2, s3]
})

# Display Results
st.subheader("Yield Curve Visualization")
st.line_chart(chart_data.set_index("Maturity"))

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="1y1y Forward Rate", value=f"{round(f_1y1y, 3)}%")
    st.caption("The 1-year rate, 1 year from now.")

with col2:
    st.metric(label="2y1y Forward Rate", value=f"{round(f_2y1y, 3)}%")
    st.caption("The 1-year rate, 2 years from now.")

st.info("💡 **CFA Logic:** This model assumes the 'Pure Expectations Theory' where forward rates are unbiased predictors of future spot rates.")
