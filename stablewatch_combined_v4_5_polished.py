
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import random

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(page_title="Stablewatch", layout="wide")

# -----------------------------
# GLOBAL STYLING INJECTION
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTabs [data-baseweb="tab-list"] {
            border-bottom: 2px solid #e2e8f0;
            margin-bottom: 1rem;
        }
        .stTabs [data-baseweb="tab"] {
            font-weight: 600;
            padding: 0.5rem 1rem;
        }
        .stDataFrame {
            border: 1px solid #d1d5db;
            border-radius: 8px;
        }
        .element-container:has(.stTable) {
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 1rem;
            background-color: #f9fafb;
        }
        h1, h2, h3 {
            color: #1f2937;
        }
    </style>
""", unsafe_allow_html=True)


# Sidebar Guidance
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/5/55/Stablecoin_icon.png", width=100)
st.sidebar.title("Stablewatch")
st.sidebar.markdown("Navigate the tabs above to explore AI-powered stablecoin analysis.")
st.sidebar.info("This app evaluates stablecoins on peg stability, AI risk scores, and overall safety.")

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Homepage", "📊 Dashboard", "🔍 Price Drivers", "📰 News & AI Insights"])

# -----------------------------
# HOMEPAGE
# -----------------------------
with tab1:
    st.markdown("""
        <style>
            .hero { text-align: center; margin-top: 2em; }
            .hero h1 { font-size: 3em; font-weight: bold; }
            .hero p { font-size: 1.2em; color: #555; max-width: 700px; margin: 0 auto; margin-top: 1em; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='hero'><h1>Know Your Stablecoin</h1><p>AI-powered insights into stablecoin transparency, risk, and stability. Built for investors, analysts, and institutions.</p></div>", unsafe_allow_html=True)

    st.markdown("### 💡 Why Stablewatch?")
    st.markdown("""
    - **Real-time Peg Tracking**  
    - **AI-Powered Risk Scores**  
    - **Collateralization & Volume Signals**  
    - **Daily Updated Metrics**
    """, unsafe_allow_html=True)

    st.markdown("### 💳 Subscription Plans")
    st.markdown("""
    | Plan        | Features                                                       | Price     |
    |-------------|----------------------------------------------------------------|-----------|
    | **Starter** | Live dashboard, 5 tokens, 7-day charts                         | Free      |
    | **Pro**     | Full AI analysis, 10+ tokens, alerts, reports                  | $19/mo    |
    | **Enterprise** | API access, team logins, white-label dashboard             | Custom    |
    """, unsafe_allow_html=True)

    st.markdown("### 📬 Stay Updated")
    st.text_input("Email for early access & updates")



# -----------------------------
# PRICE DRIVERS TAB
with tab3:
    st.title("🔍 Stablecoin Price Drivers & Hypotheticals")
    st.markdown("""
    ### 💡 What Moves a Stablecoin Off-Peg?
    - **Loss of confidence or insolvency** of the issuing platform
    - **Redemptions exceeding reserves**
    - **Regulatory restrictions**
    - **Market-wide liquidity crunch**
    """)

    st.markdown("### ✏️ Simulate Hypothetical Scenario")

    scenario_options = {
        "USDT fails audit": {"impact": "Peg drops to $0.95", "risk": -25},
        "USDC blacklisted in 2 countries": {"impact": "Peg drops to $0.985", "risk": -10},
        "DAI adds more ETH collateral": {"impact": "Peg stable, confidence up", "risk": +5},
        "Binance delists FRAX": {"impact": "Peg volatility rises", "risk": -15},
        "TUSD depegs 5%": {"impact": "High sell-off risk", "risk": -30}
    }

    selected_event = st.selectbox("Select Event", list(scenario_options.keys()))
    scenario_data = scenario_options[selected_event]

    impact = scenario_data["impact"]
    risk_delta = scenario_data["risk"]

    st.markdown("### 🔮 Outcome")
    st.table(pd.DataFrame([{
        "Event": selected_event,
        "Expected Impact": impact,
        "Risk Score Δ": f"{risk_delta:+} pts"
    }]))

    st.title("🔍 Stablecoin Price Drivers & Hypotheticals")
    st.markdown("""
    ### 💡 What Moves a Stablecoin Off-Peg?
    - **Loss of confidence or insolvency** of the issuing platform (e.g. a major audit failure)
    - **Redemptions exceeding reserves**, causing collateral to be depleted
    - **Regulatory actions or deplatforming** that freeze or blacklist tokens
    - **Market-wide liquidity crunch** where holders sell stablecoins for safer assets
    """)

    st.markdown("### ✏️ Customize Hypothetical Scenario")

    colA, colB, colC = st.columns(3)
    with colA:
        event = st.text_input("Scenario", "USDT fails audit")
    with colB:
        effect = st.text_input("Expected Impact", "Peg drops to $0.95")
    with colC:
        risk_delta = st.slider("Risk Score Change", -50, 50, -25)

    st.markdown("### 🔮 Generated Table")
    st.table(pd.DataFrame([{
        "Event": event,
        "Expected Impact": effect,
        "Risk Score Δ": f"{risk_delta:+} pts"
    }]))

    st.title("🔍 Stablecoin Price Drivers & Hypotheticals")
    st.markdown("""
    ### 💡 What Moves a Stablecoin Off-Peg?
    - **Loss of confidence or insolvency** of the issuing platform (e.g. a major audit failure)
    - **Redemptions exceeding reserves**, causing collateral to be depleted
    - **Regulatory actions or deplatforming** that freeze or blacklist tokens
    - **Market-wide liquidity crunch** where holders sell stablecoins for safer assets

    ### 🔮 Hypothetical Scenarios
    | Event | Expected Impact | Risk Score Drop |
    |-------|------------------|-----------------|
    | Tether fails audit | Peg drops to $0.95 | -25 pts |
    | USDC blacklisted in 2 countries | Reduced demand, peg to $0.985 | -10 pts |
    | DAI over-collateralized surge | Peg stable, trust increases | +5 pts |
    | Binance delists FRAX | Peg volatility increases | -15 pts |
    
    These scenarios help analysts and institutions understand risk outside of price alone.
    """)

# -----------------------------
# NEWS TAB
with tab4:
    st.title("📰 Stablecoin News & AI Insights")
    st.markdown("""
    ### 🗞️ Latest Headlines
    - **Circle (USDC) announces new real-time reserve dashboard**
    - **Tether increases transparency amid audit pressure**
    - **SEC investigates algorithmic stablecoins**

    ### 🤖 AI-Generated Observations
    > _"DAI has maintained a strong peg despite volatility in ETH. Collateralization ratio trending positive."_  
    > _"USDT score dropped 3 points due to large redemptions and exchange delistings."_

    ### 📌 Recommendations
    - ✅ **DAI** appears resilient and well-collateralized — *Low Risk*
    - ⚠️ **USDT** transparency still limited — *Monitor closely*
    - ❗ **TUSD** shows reduced trust metrics — *Consider alternatives*

    These insights are updated regularly and curated by Stablewatch AI.
    """)


# -----------------------------
# DASHBOARD
# -----------------------------
with tab2:
    st.title("📊 Stablecoin Risk Dashboard")

    # Simulated data for stablecoins
    coins = {
        "USDC": "✅ Very Safe",
        "USDT": "🟡 Moderate Risk",
        "DAI": "✅ Very Safe",
        "FRAX": "🟠 Caution",
        "TUSD": "🔴 High Risk"
    }

    st.markdown("### Select a stablecoin to view")
    selected_coin = st.selectbox("Stablecoin", list(coins.keys()))

    safety_label = coins[selected_coin]

    # Simulate peg data
    today = datetime.datetime.today()
    dates = [today - datetime.timedelta(days=i) for i in reversed(range(7))]
    prices = [1 + random.uniform(-0.005, 0.005) for _ in dates]

    delta = round(prices[-1] - 1.0, 4)
    score = round(100 - abs(delta * 1000), 1)

    # Display in a column layout
    st.markdown(f"### {selected_coin} — {safety_label}")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric("AI Risk Score", f"{score}/100", delta=f"{delta:+.4f}")
        st.write("**Status:**", safety_label)
        st.write("**Volatility:**", f"{round(max(prices)-min(prices), 5)}")
        st.caption("Risk score is AI-generated based on price deviations and volatility.")

    with col2:
        fig, ax = plt.subplots()
        ax.plot(dates, prices, marker='o')
        ax.axhline(1.0, color='gray', linestyle='--', linewidth=1)
        ax.set_title(f"{selected_coin} 7-Day Peg Trend")
        ax.set_ylabel("USD Price")
        ax.set_xlabel("Date")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
        fig.autofmt_xdate(rotation=45)
        st.pyplot(fig)

    st.caption("Last updated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
