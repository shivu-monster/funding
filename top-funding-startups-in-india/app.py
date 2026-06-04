import streamlit as st

# --------------------------------------------------

# Page Configuration

# --------------------------------------------------

st.set_page_config(
page_title="Top Funding Startups in India",
page_icon="🚀",
layout="wide",
initial_sidebar_state="expanded"
)

# --------------------------------------------------

# Banner

# --------------------------------------------------

try:
st.image(
"assets/banner.png",
use_container_width=True
)
except Exception:
st.info("Banner image not found.")

# --------------------------------------------------

# Title

# --------------------------------------------------

st.title("🚀 Top Funding Startups in India")

st.markdown(
"""

### Interactive Startup Funding Analysis Dashboard

Analyze startup funding trends in India, explore investor activity,
visualize funding patterns, and predict future startup funding using
Machine Learning.
"""
)

# --------------------------------------------------

# Quick Statistics

# --------------------------------------------------

st.header("📌 Dashboard Features")

col1, col2 = st.columns(2)

with col1:

```
st.success("📊 Data Overview")

st.markdown(
    """
```

* Dataset Summary
* Missing Value Analysis
* Statistical Reports
* Funding Statistics
  """
  )

  st.success("📈 Visualizations")

  st.markdown(
  """
* Top Funded Startups
* Funding by City
* Industry Analysis
* Funding Trends
  """
  )

with col2:

```
st.success("🔮 Funding Prediction")

st.markdown(
    """
```

* Startup Funding Prediction
* Machine Learning Model
* Investor Analysis
  """
  )

  st.success("📋 Insights")

  st.markdown(
  """
* Funding Insights
* Top Investors
* Startup Ecosystem Trends
* Recommendations
  """
  )

# --------------------------------------------------

# Project Objective

# --------------------------------------------------

st.header("🎯 Project Objective")

st.write(
"""
This project analyzes startup funding data across India
to identify patterns, trends, and investment opportunities.

Key objectives:

• Identify top funded startups

• Analyze city-wise funding distribution

• Discover leading industries

• Track investor participation

• Predict startup funding using Machine Learning
"""
)

# --------------------------------------------------

# Navigation Help

# --------------------------------------------------

st.header("🧭 Navigation")

st.info(
"""
Use the sidebar to access:

📊 Data Overview

📈 Visualizations

🔮 Funding Prediction

📋 Insights
"""
)

# --------------------------------------------------

# Technologies Used

# --------------------------------------------------

st.header("🛠️ Technologies")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Frontend", "Streamlit")
tech2.metric("Analysis", "Pandas")
tech3.metric("Charts", "Plotly")
tech4.metric("ML Model", "Random Forest")

# --------------------------------------------------

# Footer

# --------------------------------------------------

st.markdown("---")

st.caption(
"🚀 Developed using Streamlit, Pandas, Plotly, Scikit-Learn, and Python"
)
