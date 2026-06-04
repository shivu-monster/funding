import streamlit as st

# Page Configuration

st.set_page_config(
page_title="Top Funding Startups in India",
page_icon="🚀",
layout="wide",
initial_sidebar_state="expanded"
)

# Banner Image

try:
st.image(
"assets/banner.png",
use_container_width=True
)
except FileNotFoundError:
st.warning(
"Banner image not found. Place banner.png inside the assets folder."
)
except Exception as e:
st.error(f"Error loading banner: {e}")

# Title

st.title("🚀 Top Funding Startups in India")

st.markdown(
"""
Welcome to the **Top Funding Startups in India Dashboard**.

This interactive dashboard helps analyze startup funding trends,
investor activity, city-wise funding distribution, and provides
funding prediction insights using Machine Learning.
"""
)

# Sidebar Information

st.sidebar.title("Navigation")

st.sidebar.info(
"""
Use the pages menu on the left to navigate:

📊 Data Overview

📈 Visualizations

🔮 Prediction

📋 Insights
"""
)

# Dashboard Features

st.header("📌 Dashboard Features")

col1, col2 = st.columns(2)

with col1:
st.success("📊 Data Overview")
st.write(
"""

* Dataset Summary
* Missing Values Analysis
* Statistical Information
* Funding Statistics
  """
  )

  st.success("📈 Visualizations")
  st.write(
  """
* Top Funded Startups
* City-wise Funding
* Industry Analysis
* Funding Trends
  """
  )

with col2:
st.success("🔮 Prediction")
st.write(
"""

* Startup Funding Prediction
* Machine Learning Model
* Investment Analysis
  """
  )

  st.success("📋 Insights")
  st.write(
  """
* Top Startup Insights
* Investor Analysis
* Funding Recommendations
* Market Trends
  """
  )

# Project Objective

st.header("🎯 Project Objective")

st.write(
"""
The objective of this project is to analyze startup funding data
across India and identify important trends such as:

• Most funded startups

• Top investment sectors

• Active investors

• Startup hubs in India

• Funding prediction using machine learning
"""
)

# Footer

st.markdown("---")

st.caption(
"Developed using Streamlit, Pandas, Plotly, and Scikit-Learn"
)
