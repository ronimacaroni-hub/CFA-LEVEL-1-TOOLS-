import streamlit as st

st.set_page_config(page_title="DuPont Analysis")

st.title("📊 3-Step DuPont Analysis Dashboard")
st.markdown("### CFA Level 1: Financial Statement Analysis (FSA)")

with st.form("financial_data"):
    col1, col2 = st.columns(2)
    with col1:
        net_income = st.number_input("Net Income ($)", value=10000.0)
        revenue = st.number_input("Revenue ($)", value=100000.0)
    with col2:
        assets = st.number_input("Average Assets ($)", value=200000.0)
        equity = st.number_input("Average Equity ($)", value=80000.0)
    submit = st.form_submit_button("Calculate Breakdown")

if submit:
    # Calculations
    margin = (net_income / revenue) * 100
    turnover = revenue / assets
    leverage = assets / equity
    roe = (margin/100 * turnover * leverage) * 100

    st.divider()
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Net Profit Margin", f"{round(margin, 2)}%")
    c2.metric("Asset Turnover", f"{round(turnover, 2)}x")
    c3.metric("Equity Multiplier", f"{round(leverage, 2)}x")
    
    st.success(f"## Final ROE: {round(roe, 2)}%")
    st.info("This breakdown helps identify if ROE is driven by profitability, efficiency, or leverage.")
