import streamlit as st

st.set_page_config(
page_title="Indian Startup Funding Analysis",
page_icon="📈",
layout="wide"
)

st.title("📈 Indian Startup Funding Analysis")
st.markdown("""
Welcome to the Startup Funding Dashboard.

Use the sidebar to navigate through:

* Data Overview
* Visualizations
* Prediction
* Insights
  """)

st.image("assets/banner.png", use_container_width=True)
