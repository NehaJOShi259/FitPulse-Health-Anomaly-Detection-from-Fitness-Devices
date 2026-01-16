import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FitPulse Dashboard", layout="wide")
st.title("FitPulse – Health Anomaly Dashboard")

# -----------------------------
# Upload CSV
# -----------------------------
uploaded_file = st.file_uploader("Upload fitness dataset (CSV)", type=["csv"])

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    return df

def detect_anomalies(series, k=3):
    mean = series.mean()
    std = series.std()
    return abs(series - mean) > k * std

if uploaded_file:
    data = load_data(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    metric = st.selectbox(
        "Select metric",
        ["avg_heart_rate", "daily_steps", "hours_sleep"]
    )

    k = st.slider("Anomaly sensitivity (k)", 1.5, 4.0, 3.0, 0.1)

    data["anomaly"] = detect_anomalies(data[metric], k)

    st.subheader(f"{metric.replace('_',' ').title()} Trend with Anomalies")

    fig = px.line(data, x="date", y=metric)
    fig.add_scatter(
        x=data[data["anomaly"]]["date"],
        y=data[data["anomaly"]][metric],
        mode="markers",
        marker=dict(color="red", size=8),
        name="Anomaly"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Download Anomaly Report")
    st.download_button(
        "Download CSV",
        data[data["anomaly"]].to_csv(index=False),
        file_name="anomaly_report.csv",
        mime="text/csv"
    )
