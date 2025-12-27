import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="FitPulse Health Data Preview", layout="wide")

st.title("FitPulse: Health Anomaly Detection (Milestone 1)")
st.write("Preview of preprocessed fitness data")

DATA_PATH = Path("data/merged_1min_dataset.csv")

if DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)

    st.success("Merged dataset loaded successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(50), use_container_width=True)

    st.subheader("Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

else:
    st.error("merged_1min_dataset.csv not found in data folder")
    st.info("Run preprocess.py first to generate the merged dataset")

