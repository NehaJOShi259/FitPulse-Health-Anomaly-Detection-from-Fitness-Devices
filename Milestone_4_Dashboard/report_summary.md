# Milestone 4: Dashboard for Health Anomaly Insights

## Objective
The objective of this milestone is to develop an interactive Streamlit-based dashboard
that enables users to upload fitness data and visualize health anomalies related to
heart rate, step count, and sleep duration.

## Dashboard Workflow
1. User uploads fitness data in CSV or JSON format.
2. The dashboard validates required columns and preprocesses timestamps.
3. Isolation Forest is applied to detect anomalies in health metrics.
4. Anomaly summaries are displayed.
5. Interactive visualizations highlight abnormal patterns.
6. Users can download a CSV anomaly report.

## Tools & Libraries Used
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn (Isolation Forest)

## Key Insights
- Abnormal heart rate spikes and drops were identified.
- Irregular step count behavior was detected.
- Sleep duration anomalies highlighted unhealthy sleep patterns.
