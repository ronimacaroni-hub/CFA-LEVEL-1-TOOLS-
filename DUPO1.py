import streamlit as st

# 1. Page Configuration (MUST be the first Streamlit command)
st.set_page_config(page_title="DuPont Analysis Dashboard", layout="wide")

# 2. Professional White & Black Theme CSS
st.markdown("""
    <style>
    /* Main Background: Pure White */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Force ALL text to Black for high contrast */
    * {
        color: #000000 !important;
    }

    /* Headings: Bold Black, Centered */
    h1, h2, h3 {
        color: #000000 !important;
        text-align: center !important;
        font-weight: bold !important;
        text-transform: uppercase;
    }

    /* Input Boxes: White background with Black border */
    div[data-baseweb="input"] {
        border: 1px solid #000000 !important;
        background-color: #FFFFFF !important;
    }

    /* Form Button: Professional Black with White Text */
    button[kind="primaryFormSubmit"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 5px !important;
        width: 100% !important;
        font-weight: bold !important;
    }
    
    /* Metric Display Styling */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: bold !important;
    }
    
    [data-testid="stMetricLabel"] p {
        color: #333333 !important;
        font-size: 16px !important;
    }

    /* Success/Info Box Styling */
    .stAlert {
        background-color: #F0F2F6 !important;
        border: 1px solid #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Dashboard Header
st.title("📊 DUPONT ANALYSIS DASHBOARD")
st.markdown("<h3 style='text-align: center;'>CFA Level 1: Financial Statement Analysis (FSA)</h3>", unsafe_allow_html=True)

# 4. Input Form
with st.form("financial_data"):
    col1, col2 = st.columns(2)
    with col1:
        net_income = st.number_input("Net Income ($)", value=10000.0, step=500.0)
        revenue = st.number_input("Total Revenue ($)", value=100000.0, step=1000.0)
    with col2:
        assets = st.number_input("Average Total Assets ($)", value=200000.0, step=1000.0)
        equity = st.number_input("Average Shareholders' Equity ($)", value=80000.0, step=1000.0)
    
    submit = st.form_submit_button("RUN ANALYSIS")

# 5. Calculation and Output Logic
if submit:
    # Formulaic Calculations
    margin = (net_income / revenue) * 100
    turnover = revenue / assets
    leverage = assets / equity
    roe = (margin/100 * turnover * leverage) * 100

    st.divider()
    
    # Visual 3-Step Breakdown
    st.markdown("### 3-Step Component Breakdown")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.metric("Net Profit Margin", f"{round(margin, 2)}%")
    with c2:
        st.metric("Asset Turnover", f"{round(turnover, 2)}x")
    with c3:
        st.metric("Equity Multiplier", f"{round(leverage, 2)}x")
    
    st.divider()
    
    # Final Result Display
    st.markdown(f"<h1 style='text-align: center; font-size: 50px;'>FINAL ROE: {round(roe, 2)}%</h1>", unsafe_allow_html=True)
    
    st.info("**Analysis Summary:** This breakdown reveals if the Return on Equity is driven by Profitability (Margin), Efficiency (Turnover), or Financial Leverage (Multiplier).")
