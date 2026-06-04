import pandas as pd

def load_data(file_path):
"""
Load and preprocess startup funding dataset.
"""

```
# Load dataset
df = pd.read_csv(file_path)

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df = df.fillna("Unknown")

# Convert funding amount to numeric
if "AmountInUSD" in df.columns:
    df["AmountInUSD"] = (
        df["AmountInUSD"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    df["AmountInUSD"] = pd.to_numeric(
        df["AmountInUSD"],
        errors="coerce"
    )

    df["AmountInUSD"] = df["AmountInUSD"].fillna(0)

# Convert Date column
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

return df
```

def get_basic_stats(df):
"""
Return basic dataset statistics.
"""
stats = {
"rows": df.shape[0],
"columns": df.shape[1],
"missing_values": int(df.isnull().sum().sum()),
"duplicates": int(df.duplicated().sum())
}

```
return stats
```

def top_funded_startups(df, n=10):
"""
Return top funded startups.
"""
if "StartupName" not in df.columns:
return pd.DataFrame()

```
return (
    df.groupby("StartupName")["AmountInUSD"]
    .sum()
    .sort_values(ascending=False)
    .head(n)
    .reset_index()
)
```

def top_cities(df, n=10):
"""
Return top funding cities.
"""
if "CityLocation" not in df.columns:
return pd.DataFrame()

```
return (
    df.groupby("CityLocation")["AmountInUSD"]
    .sum()
    .sort_values(ascending=False)
    .head(n)
    .reset_index()
)
```

def top_industries(df, n=10):
"""
Return top funded industries.
"""
if "IndustryVertical" not in df.columns:
return pd.DataFrame()

```
return (
    df.groupby("IndustryVertical")["AmountInUSD"]
    .sum()
    .sort_values(ascending=False)
    .head(n)
    .reset_index()
)
```
