import streamlit as st
import pandas as pd
import plotly.express as px
from utils.preprocessing import load_data

st.set_page_config(page_title="Visualizations", page_icon="📈")

st.title("📈 Startup Funding Visualizations")

# Load Data

df = load_data("data/startup_funding.csv")

# Ensure AmountInUSD is numeric

df["AmountInUSD"] = pd.to_numeric(df["AmountInUSD"], errors="coerce")

# -------------------------------

# Top Funded Startups

# -------------------------------

st.subheader("🏆 Top 10 Funded Startups")

if "StartupName" in df.columns:
top_startups = (
df.groupby("StartupName")["AmountInUSD"]
.sum()
.sort_values(ascending=False)
.head(10)
.reset_index()
)

```
fig = px.bar(
    top_startups,
    x="StartupName",
    y="AmountInUSD",
    title="Top 10 Funded Startups"
)
st.plotly_chart(fig, use_container_width=True)
```

# -------------------------------

# Top Funding Cities

# -------------------------------

st.subheader("🏙️ Top Funding Cities")

if "CityLocation" in df.columns:
city_funding = (
df.groupby("CityLocation")["AmountInUSD"]
.sum()
.sort_values(ascending=False)
.head(10)
.reset_index()
)

```
fig = px.pie(
    city_funding,
    names="CityLocation",
    values="AmountInUSD",
    title="Funding Distribution by City"
)

st.plotly_chart(fig, use_container_width=True)
```

# -------------------------------

# Industry-wise Funding

# -------------------------------

st.subheader("🏭 Industry-wise Funding")

if "IndustryVertical" in df.columns:
industry_funding = (
df.groupby("IndustryVertical")["AmountInUSD"]
.sum()
.sort_values(ascending=False)
.head(10)
.reset_index()
)

```
fig = px.bar(
    industry_funding,
    x="IndustryVertical",
    y="AmountInUSD",
    title="Top Industries by Funding"
)

st.plotly_chart(fig, use_container_width=True)
```

# -------------------------------

# Investment Type Analysis

# -------------------------------

st.subheader("💰 Investment Type Distribution")

if "InvestmentType" in df.columns:
investment_count = (
df["InvestmentType"]
.value_counts()
.reset_index()
)

```
investment_count.columns = ["InvestmentType", "Count"]

fig = px.pie(
    investment_count,
    names="InvestmentType",
    values="Count",
    title="Investment Type Distribution"
)

st.plotly_chart(fig, use_container_width=True)
```

# -------------------------------

# Top Investors

# -------------------------------

st.subheader("🤝 Top Investors")

if "InvestorsName" in df.columns:
investor_count = (
df["InvestorsName"]
.value_counts()
.head(10)
.reset_index()
)

```
investor_count.columns = ["Investor", "Investments"]

fig = px.bar(
    investor_count,
    x="Investor",
    y="Investments",
    title="Top 10 Investors"
)

st.plotly_chart(fig, use_container_width=True)
```

# -------------------------------

# Funding Trend Over Time

# -------------------------------

st.subheader("📅 Funding Trend")

if "Date" in df.columns:
try:
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

```
    trend = (
        df.groupby(df["Date"].dt.year)["AmountInUSD"]
        .sum()
        .reset_index()
    )

    trend.columns = ["Year", "Funding"]

    fig = px.line(
        trend,
        x="Year",
        y="Funding",
        markers=True,
        title="Funding Trend Over Years"
    )

    st.plotly_chart(fig, use_container_width=True)

except:
    st.warning("Date column could not be processed.")
```
