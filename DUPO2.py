import streamlit as st

# 1. Page Configuration (MUST be the first Streamlit command)
st.set_page_config(page_title="BSE Institute | DuPont Analysis", layout="wide")

# 2. High-Contrast Professional CSS
st.markdown("""
    <style>
    /* Main Background: Dark Navy/Black for a Pro Look */
    .stApp {
        background-color: #0E1117 !important;
    }
    
    /* Global text: White */
    * {
        color: #FFFFFF !important;
    }

    /* Headings: Gold (BSE/CFA Style) */
    h1, h2, h3 {
        color: #FFD700 !important;
        text-align: center !important;
        font-weight: bold !important;
    }

    /* INPUT BOXES: Dark background with WHITE TEXT inside */
    input {
        color: #FFFFFF !important;
        background-color: #262730 !important;
    }
    
    /* Target the specific Streamlit number input div */
    div[data-baseweb="input"] {
        background-color: #262730 !important;
        border: 1px solid #FFD700 !important;
    }

    /* BUTTON: Gold with Black Text */
    button[kind="primaryFormSubmit"] {
        background-color: #FFD700 !important;
        color: #000000 !important;
        border-radius: 5px !important;
        width: 100% !important;
        font-weight: bold !important;
    }
    
    /* Metrics: Bright White/Gold */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Dashboard Header
st.title("📊 DUPONT ANALYSIS DASHBOARD")
st.markdown("<h3 style='text-align: center;'>BSE Institute Campus | CFA Level 1 Prep</h3>", unsafe_allow_html=True)

# 4. Input Form
with st.form("financial_data"):
    col1, col2 = st.columns(2)
    with col1:
        net_income = st.number_input("Net Income ($)", value=10000.0)
        revenue = st.number_input("Total Revenue ($)", value=100000.0)
    with col2:
        assets = st.number_input("Average Total Assets ($)", value=200000.0)
        equity = st.number_input("Average Shareholders' Equity ($)", value=80000.0)
    
    submit = st.form_submit_button("RUN FINANCIAL ANALYSIS")

# 5. Calculation and Output Logic
if submit:
    margin = (net_income / revenue) * 100
    turnover = revenue / assets
    leverage = assets / equity
    roe = (margin/100 * turnover * leverage) * 100

    st.divider()
    
    st.markdown("### Component Breakdown")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.metric("Net Profit Margin", f"{round(margin, 2)}%")
    with c2:
        st.metric("Asset Turnover", f"{round(turnover, 2)}x")
    with c3:
        st.metric("Equity Multiplier", f"{round(leverage, 2)}x")
    
    st.divider()
    st.markdown(f"<h1 style='text-align: center; color: #FFD700;'>FINAL ROE: {round(roe, 2)}%</h1>", unsafe_allow_html=True)
    st.info("Analysis: This identifies if ROE is driven by Profitability, Efficiency, or Leverage.")
