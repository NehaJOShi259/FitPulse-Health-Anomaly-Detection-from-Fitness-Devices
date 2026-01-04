# Milestone 3: Anomaly Detection and Visualization

## Objective
Detect anomalies in heart rate and sleep data using Prophet and residual analysis.

## Steps Followed
1. Prepared heart rate, sleep, and steps dataframes from Clean.csv
2. Converted timestamps to datetime
3. Trained Prophet models
4. Forecasted expected values and calculated residuals
5. Detected anomalies using 3-sigma threshold
6. Visualized anomalies in time-series plots

## Tools Used
- Python 3, Google Colab
- Pandas, Numpy, Matplotlib
- Prophet (Facebook/Meta)

## Key Insights
- Heart rate anomalies appear as sudden spikes/drops
- Sleep anomalies appear as unusually long or short durations
- The plots highlight these anomalies clearly

## Visualizations
- `visualizations/heart_rate_anomalies.png`
- `visualizations/sleep_anomalies.png`

