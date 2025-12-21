# modeling.py

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load TSFresh features (or recombine in same script)
hr_features = pd.read_csv('data/hr_features.csv')
steps_features = pd.read_csv('data/steps_features.csv')
sleep_features = pd.read_csv('data/sleep_features.csv')
data = pd.read_csv('data/Clean.csv')

# ------------------------------
# Prophet trend modeling example for Heart Rate
hr = data[['Timestamp','Heart Rate']].rename(columns={'Timestamp':'ds','Heart Rate':'y'})
model_hr = Prophet()
model_hr.fit(hr)

future_hr = model_hr.make_future_dataframe(periods=30)
forecast_hr = model_hr.predict(future_hr)

# Plot Prophet forecast
model_hr.plot(forecast_hr)
plt.title('Heart Rate Trend')
plt.show()

# ------------------------------
# Behavioral Clustering

# Combine features and some numeric columns
combined_features = pd.concat([hr_features, steps_features, sleep_features, 
                               data[['Age']].reset_index(drop=True)], axis=1)

# One-hot encode categorical columns if any
categorical_cols = ['BMI Category', 'Physical Activity Level', 'Stress Level']
for col in categorical_cols:
    if col in data.columns:
        dummies = pd.get_dummies(data[col], prefix=col)
        combined_features = pd.concat([combined_features, dummies], axis=1)

# Impute missing values
combined_features.fillna(combined_features.mean(), inplace=True)

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(combined_features)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels
combined_features['cluster'] = clusters

# PCA for visualization
pca = PCA(n_components=2)
components = pca.fit_transform(scaled_features)

plt.figure(figsize=(8,6))
plt.scatter(components[:,0], components[:,1], c=clusters, cmap='viridis', s=50)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Behavioral Clusters')
plt.colorbar(label='Cluster')
plt.show()
