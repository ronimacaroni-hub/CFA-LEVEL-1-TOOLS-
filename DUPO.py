import streamlit as st

# 1. THIS MUST BE FIRST
st.set_page_config(page_title="DuPont Analysis", layout="wide")

# 2. Custom CSS for the Navy and Gold theme
st.markdown("""
    <style>
    .stApp {
        background-color: #000080;
    }
    /* White text for all labels and paragraphs */
    .stApp p, .stApp label, .stApp span, .stApp div {
        color: #FFFFFF !important;
    }
    /* Golden Yellow for Headings */
    h1, h2, h3 {
        color: #FFD700 !important;
        text-align: center;
    }
    /* Styling the Metric Boxes to stand out */
    [data-testid="stMetricValue"] {
        color: #FFD700 !important;
    }
    /* Styling the Form and Buttons */
    div.stButton > button {
        background-color: #000080;
        color: #FFD700;
        border: 2px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Rest of your logic
st.title("📊 DUPONT ANALYSIS DASHBOARD")
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
    # Logic remains the same
    margin = (net_income / revenue) * 100
    turnover = revenue / assets
    leverage = assets / equity
    roe = (margin/100 * turnover * leverage) * 100

    st.divider()
    
    # Using columns for the 3-step breakdown as discussed
    c1, c2, c3 = st.columns(3)
    c1.metric("Net Profit Margin", f"{round(margin, 2)}%")
    c2.metric("Asset Turnover", f"{round(turnover, 2)}x")
    c3.metric("Equity Multiplier", f"{round(leverage, 2)}x")
    
    st.markdown(f"<h2 style='text-align: center;'>Final ROE: {round(roe, 2)}%</h2>", unsafe_allow_html=True)
    st.info("Breakdown identifies if ROE is driven by profitability, efficiency, or leverage.")
