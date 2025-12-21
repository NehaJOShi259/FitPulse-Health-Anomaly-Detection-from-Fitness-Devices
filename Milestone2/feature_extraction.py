# feature_extraction.py

import pandas as pd
import numpy as np
from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute

# Load dataset
data = pd.read_csv('data/Clean.csv')

# Prepare Heart Rate dataframe
hr = data[['Timestamp','Heart Rate']].rename(columns={'Timestamp':'time','Heart Rate':'value'})
hr['id'] = 1  # single user

# Prepare Steps dataframe
steps = data[['Timestamp','Daily Steps']].rename(columns={'Timestamp':'time','Daily Steps':'value'})
steps['id'] = 1

# Prepare Sleep dataframe
sleep = data[['Timestamp','Sleep Duration']].rename(columns={'Timestamp':'time','Sleep Duration':'value'})
sleep['id'] = 1

# Compute simple statistical features
def compute_stats(df):
    return {
        'mean': np.mean(df['value']),
        'std': np.std(df['value']),
        'skew': df['value'].skew(),
        'kurtosis': df['value'].kurtosis()
    }

hr_stats = compute_stats(hr)
steps_stats = compute_stats(steps)
sleep_stats = compute_stats(sleep)

print("Heart Rate Stats:", hr_stats)
print("Steps Stats:", steps_stats)
print("Sleep Stats:", sleep_stats)

# Extract TSFresh features
hr_features = extract_features(hr, column_id='id', column_sort='time')
impute(hr_features)

steps_features = extract_features(steps, column_id='id', column_sort='time')
impute(steps_features)

sleep_features = extract_features(sleep, column_id='id', column_sort='time')
impute(sleep_features)

# Save features to CSV (optional)
hr_features.to_csv('data/hr_features.csv', index=False)
steps_features.to_csv('data/steps_features.csv', index=False)
sleep_features.to_csv('data/sleep_features.csv', index=False)

