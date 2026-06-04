import streamlit as st
import pandas as pd
from utils.preprocessing import load_data

st.set_page_config(
page_title="Insights",
page_icon="📋"
)

st.title("📋 Startup Funding Insights")

# Load Dataset

df = load_data("data/startup_funding.csv")

# Ensure funding column is numeric

df["AmountInUSD"] = pd.to_numeric(
df["AmountInUSD"],
errors="coerce"
)

# Remove missing funding values

df = df.dropna(subset=["AmountInUSD"])

# -----------------------------------

# Key Metrics

# -----------------------------------

st.header("📊 Key Metrics")

total_funding = df["AmountInUSD"].sum()
average_funding = df["AmountInUSD"].mean()

total_startups = (
df["StartupName"].nunique()
if "StartupName" in df.columns
else 0
)

col1, col2, col3 = st.columns(3)

with col1:
st.metric(
"Total Funding",
f"${total_funding:,.0f}"
)

with col2:
st.metric(
"Average Funding",
f"${average_funding:,.0f}"
)

with col3:
st.metric(
"Total Startups",
total_startups
)

# -----------------------------------

# Top Funded Startup

# -----------------------------------

st.header("🏆 Top Funded Startup")

if "StartupName" in df.columns:

```
top_startup = (
    df.groupby("StartupName")["AmountInUSD"]
    .sum()
    .sort_values(ascending=False)
)

if len(top_startup) > 0:
    st.success(
        f"Most funded startup: "
        f"{top_startup.index[0]} "
        f"(${top_startup.iloc[0]:,.0f})"
    )
```

# -----------------------------------

# Top Funding City

# -----------------------------------

st.header("🏙️ Funding Hotspot")

if "CityLocation" in df.columns:

```
top_city = (
    df.groupby("CityLocation")["AmountInUSD"]
    .sum()
    .sort_values(ascending=False)
)

if len(top_city) > 0:
    st.info(
        f"Highest funded city: "
        f"{top_city.index[0]} "
        f"(${top_city.iloc[0]:,.0f})"
    )
```

# -----------------------------------

# Top Industry

# -----------------------------------

st.header("🏭 Leading Industry")

if "IndustryVertical" in df.columns:

```
top_industry = (
    df.groupby("IndustryVertical")["AmountInUSD"]
    .sum()
    .sort_values(ascending=False)
)

if len(top_industry) > 0:
    st.success(
        f"Top funded industry: "
        f"{top_industry.index[0]} "
        f"(${top_industry.iloc[0]:,.0f})"
    )
```

# -----------------------------------

# Top Investor

# -----------------------------------

st.header("🤝 Most Active Investor")

if "InvestorsName" in df.columns:

```
top_investor = (
    df["InvestorsName"]
    .dropna()
    .value_counts()
)

if len(top_investor) > 0:
    st.info(
        f"Most active investor: "
        f"{top_investor.index[0]} "
        f"({top_investor.iloc[0]} investments)"
    )
```

# -----------------------------------

# Business Insights

# -----------------------------------

st.header("💡 Business Insights")

insights = []

if "CityLocation" in df.columns and len(top_city) > 0:
insights.append(
f"• {top_city.index[0]} attracts the highest startup funding."
)

if "IndustryVertical" in df.columns and len(top_industry) > 0:
insights.append(
f"• {top_industry.index[0]} is the leading sector for investments."
)

if "StartupName" in df.columns and len(top_startup) > 0:
insights.append(
f"• {top_startup.index[0]} received the highest overall funding."
)

if average_funding > 0:
insights.append(
f"• Average funding per startup is approximately ${average_funding:,.0f}."
)

for insight in insights:
st.write(insight)

# -----------------------------------

# Recommendations

# -----------------------------------

st.header("🚀 Recommendations")

st.markdown(
"""

1. Focus on high-growth sectors such as FinTech, AI, and EdTech.
2. Explore investment opportunities in major startup hubs.
3. Track active investors for partnership opportunities.
4. Analyze successful startups to identify growth patterns.
5. Monitor funding trends to make data-driven decisions.
   """
   )

# -----------------------------------

# Raw Dataset

# -----------------------------------

with st.expander("View Dataset"):
st.dataframe(df)
