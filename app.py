import streamlit as st
import pandas as pd
from utils.cv_generator import generate_cv_pdf, render_cv_html

st.set_page_config(page_title="Employee Headcount CV Generator", layout="wide")

# Title
st.title("📄 Employee CV Dashboard")

# Upload Headcount CSV
uploaded_file = st.sidebar.file_uploader("Upload Headcount CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/Headcount.csv")

# Upload Logo
uploaded_logo = st.sidebar.file_uploader("Upload Logo", type=["png", "jpg", "jpeg"])
logo_path = "data/Logo.png"
if uploaded_logo:
    logo_path = f"data/{uploaded_logo.name}"
    with open(logo_path, "wb") as f:
        f.write(uploaded_logo.getbuffer())

# Employee Selection
personnel = st.sidebar.selectbox("Select Personnel", df["Name"].unique())

# Get row
employee = df[df["Name"] == personnel].iloc[0]

# Render CV HTML preview
html_content = render_cv_html(employee, logo_path)
st.components.v1.html(html_content, height=900, scrolling=True)

# Export Button
if st.button("Export CV as PDF"):
    generate_cv_pdf(employee, logo_path)
    with open("data/cv_output.pdf", "rb") as pdf_file:
        st.download_button("Download CV", data=pdf_file, file_name=f"{employee['Name']}_CV.pdf", mime="application/pdf")
