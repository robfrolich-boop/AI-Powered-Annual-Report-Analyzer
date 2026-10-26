
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# APP CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI-Powered Annual Report Analyzer",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# FINANCIAL DATA
# ==========================================

# Verified figures from Hove Annual Report 2025
# All values in DKK thousand

data = {
    "Financial metric": [
        "Revenue",
        "Gross profit",
        "EBITDA",
        "Net profit",
        "Equity",
        "Operating cash flow"
    ],
    "2024": [
        169331, 62628, 13488,
        5662, 79324, -4072
    ],
    "2025": [
        209067, 72702, 22561,
        13643, 87164, 6742
    ]
}

df = pd.DataFrame(data)

df["Change (DKK thousand)"] = df["2025"] - df["2024"]

df["Change (%)"] = (
    df["Change (DKK thousand)"]
    / df["2024"].abs()
    * 100
).round(1)

# Percentage growth is not meaningful when
# operating cash flow changes from negative to positive
df.loc[
    df["Financial metric"] == "Operating cash flow",
    "Change (%)"
] = float("nan")

# ==========================================
# CALCULATIONS
# ==========================================

revenue_2024 = 169331
revenue_2025 = 209067

ebitda_2024 = 13488
ebitda_2025 = 22561

margin_2024 = ebitda_2024 / revenue_2024 * 100
margin_2025 = ebitda_2025 / revenue_2025 * 100

revenue_growth = (
    (revenue_2025 - revenue_2024)
    / revenue_2024
    * 100
)

# ==========================================
# HEADER
# ==========================================

st.title("📊 AI-Powered Annual Report Analyzer")

st.markdown(
    """
    **Financial analysis of Hove A/S — Annual Report 2025**

    This portfolio project combines Python-based
    financial calculations, data visualization,
    PDF text extraction, and an AI-generated
    financial commentary.
    """
)

st.info(
    "Prototype V1: This application uses a verified "
    "Hove A/S dataset and a previously generated AI analysis. "
    "It does not analyze newly uploaded reports."
)

st.divider()

# ==========================================
# KEY PERFORMANCE INDICATORS
# ==========================================

st.header("Financial Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Revenue 2025",
        f"DKK {revenue_2025 / 1000:.1f}m",
        f"{revenue_growth:.1f}%"
    )

with col2:
    st.metric(
        "EBITDA 2025",
        f"DKK {ebitda_2025 / 1000:.1f}m",
        f"{(ebitda_2025 / ebitda_2024 - 1) * 100:.1f}%"
    )

with col3:
    st.metric(
        "EBITDA Margin 2025",
        f"{margin_2025:.1f}%",
        f"{margin_2025 - margin_2024:+.1f} pp",
        delta_color="normal"
    )

st.subheader("Financial Statement Comparison")

st.caption(
    "Values in DKK thousand. Percentage change is omitted "
    "for operating cash flow because it moved from negative "
    "to positive."
)

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True
)

st.divider()

# ==========================================
# VISUALIZATIONS
# ==========================================

st.header("Financial Visualizations")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig, ax = plt.subplots(figsize=(7, 5))

    years = ["2024", "2025"]
    revenue = [169.331, 209.067]
    ebitda = [13.488, 22.561]

    x = [0, 1]
    width = 0.35

    ax.bar(
        [i - width / 2 for i in x],
        revenue,
        width,
        label="Revenue"
    )

    ax.bar(
        [i + width / 2 for i in x],
        ebitda,
        width,
        label="EBITDA"
    )

    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("DKK million")
    ax.set_title("Revenue and EBITDA")
    ax.legend()
    ax.grid(axis="y", alpha=0.2)

    st.pyplot(fig)
    plt.close(fig)

with chart_col2:
    fig, ax = plt.subplots(figsize=(7, 5))

    margins = [margin_2024, margin_2025]

    bars = ax.bar(
        ["2024", "2025"],
        margins,
        width=0.45
    )

    ax.set_ylabel("Percent")
    ax.set_title("EBITDA Margin")
    ax.set_ylim(0, 13)

    for bar, margin in zip(bars, margins):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            margin + 0.3,
            f"{margin:.1f}%",
            ha="center"
        )

    st.pyplot(fig)
    plt.close(fig)

st.divider()

# ==========================================
# AI-GENERATED ANALYSIS
# ==========================================

st.header("AI-Generated Financial Analysis")

st.caption(
    "Generated using Qwen2.5-3B-Instruct in Google Colab. "
    "A missing verified cost contribution was subsequently "
    "added using Python. The result is displayed as a "
    "saved analysis, not generated live."
)

ai_analysis = """
EBITDA improved by DKK 9.073 million from
DKK 13.488 million in 2024 to DKK 22.561 million
in 2025. The largest direct contributor to this
growth was the increase in gross profit by
DKK 10.074 million.

Staff costs increased by DKK 1.212 million,
partially offsetting the EBITDA improvement.
Other external costs decreased by DKK 0.211
million, which also contributed positively
to EBITDA.

Revenue grew by DKK 39.7 million (23%) to
DKK 209.1 million, driven by higher sales of
pumps and grease to both existing and new
customers in the wind turbine segment.

The gross margin declined from 37% to 34.8%
due to a higher share of private label products.
"""

st.write(ai_analysis)

st.divider()

# ==========================================
# SOURCES AND METHODOLOGY
# ==========================================

st.header("Sources and Methodology")

st.markdown(
    """
    **Primary source:** Hove A/S, Annual Report 2025.

    - Page 17: Consolidated financial figures.
    - Page 4: Management commentary on revenue.

    **Methodology:** Python and pandas were used
    for financial calculations. pdfplumber was
    used in Google Colab to extract management
    commentary from the PDF. Qwen2.5-3B-Instruct
    generated the initial financial analysis.

    **Limitations:** Financial figures are stored
    in the application as a Hove-specific dataset.
    The application does not automatically extract
    financial figures from arbitrary reports,
    and the AI analysis is not generated live.
    """
)

st.caption(
    "Portfolio project | Python · pandas · "
    "matplotlib · pdfplumber · Qwen · Streamlit"
)
