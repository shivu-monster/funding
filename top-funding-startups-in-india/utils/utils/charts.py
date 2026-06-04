import plotly.express as px
import pandas as pd

def plot_top_startups(df, top_n=10):
"""
Bar chart for top funded startups.
"""
data = (
df.groupby("StartupName")["AmountInUSD"]
.sum()
.sort_values(ascending=False)
.head(top_n)
.reset_index()
)

```
fig = px.bar(
    data,
    x="StartupName",
    y="AmountInUSD",
    title=f"Top {top_n} Funded Startups"
)

return fig
```

def plot_top_cities(df, top_n=10):
"""
Pie chart for funding by city.
"""
data = (
df.groupby("CityLocation")["AmountInUSD"]
.sum()
.sort_values(ascending=False)
.head(top_n)
.reset_index()
)

```
fig = px.pie(
    data,
    names="CityLocation",
    values="AmountInUSD",
    title="Funding Distribution by City"
)

return fig
```

def plot_top_industries(df, top_n=10):
"""
Industry-wise funding chart.
"""
data = (
df.groupby("IndustryVertical")["AmountInUSD"]
.sum()
.sort_values(ascending=False)
.head(top_n)
.reset_index()
)

```
fig = px.bar(
    data,
    x="IndustryVertical",
    y="AmountInUSD",
    title="Top Industries by Funding"
)

return fig
```

def plot_top_investors(df, top_n=10):
"""
Top investors chart.
"""
data = (
df["InvestorsName"]
.value_counts()
.head(top_n)
.reset_index()
)

```
data.columns = ["Investor", "Investments"]

fig = px.bar(
    data,
    x="Investor",
    y="Investments",
    title="Top Investors"
)

return fig
```

def plot_funding_trend(df):
"""
Funding trend over years.
"""
df["Date"] = pd.to_datetime(
df["Date"],
errors="coerce"
)

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

return fig
```

def plot_investment_type_distribution(df):
"""
Investment type distribution.
"""
data = (
df["InvestmentType"]
.value_counts()
.reset_index()
)

```
data.columns = ["InvestmentType", "Count"]

fig = px.pie(
    data,
    names="InvestmentType",
    values="Count",
    title="Investment Type Distribution"
)

return fig
```
