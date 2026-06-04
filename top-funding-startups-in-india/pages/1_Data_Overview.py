import streamlit as st
import pandas as pd
from utils.preprocessing import load_data

st.set_page_config(page_title="Data Overview", page_icon="📊")

st.title("📊 Data Overview")

# Load Dataset

df = load_data("data/startup_funding.csv")

# Dataset Shape

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

# Dataset Preview

st.subheader("Dataset Preview")
st.dataframe(df.head(10))

# Column Information

st.subheader("Column Information")
column_info = pd.DataFrame({
"Column": df.columns,
"Data Type": df.dtypes.astype(str)
})
st.dataframe(column_info)

# Missing Values

st.subheader("Missing Values")
missing_values = df.isnull().sum().reset_index()
missing_values.columns = ["Column", "Missing Values"]
st.dataframe(missing_values)

# Statistical Summary

st.subheader("Statistical Summary")
st.dataframe(df.describe(include="all"))

# Unique Values

st.subheader("Unique Values Count")
unique_values = pd.DataFrame({
"Column": df.columns,
"Unique Values": [df[col].nunique() for col in df.columns]
})
st.dataframe(unique_values)

# Funding Statistics

if "AmountInUSD" in df.columns:

```
df["AmountInUSD"] = pd.to_numeric(
    df["AmountInUSD"],
    errors="coerce"
)

st.subheader("Funding Statistics")

total_funding = df["AmountInUSD"].sum()
avg_funding = df["AmountInUSD"].mean()
max_funding = df["AmountInUSD"].max()
min_funding = df["AmountInUSD"].min()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Funding", f"${total_funding:,.0f}")
    st.metric("Average Funding", f"${avg_funding:,.0f}")

with col2:
    st.metric("Maximum Funding", f"${max_funding:,.0f}")
    st.metric("Minimum Funding", f"${min_funding:,.0f}")
```

# Dataset Download

st.subheader("Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
label="Download CSV",
data=csv,
file_name="startup_funding.csv",
mime="text/csv"
)

