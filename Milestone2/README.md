# Milestone 2: Feature Extraction and Modeling

## Objective

The goal of this milestone is to extract meaningful insights from the fitness dataset (`Clean.csv`) by:

1. Extracting statistical and time-series features for Heart Rate, Steps, and Sleep.
2. Modeling trends over time using Prophet to identify deviations from expected behavior.
3. Clustering behavioral patterns to identify normal and atypical user behavior.

---

## Dataset Description

* **File:** `Clean.csv`
* **Key Columns Used:**

  * `Heart Rate` → heart rate readings over time
  * `Daily Steps` → daily step counts
  * `Sleep Duration` → duration of sleep
  * `Age`, `BMI Category`, `Stress Level`, `Physical Activity Level` → used for clustering
  * `Timestamp` → time-series index

---

## Steps Performed

### 1. Feature Extraction

* Computed **statistical features**: mean, standard deviation, skewness, kurtosis for Heart Rate, Steps, and Sleep.
* Used **TSFresh** to extract additional time-series features like trends, autocorrelations, and frequency characteristics.

### 2. Trend Modeling

* Modeled temporal patterns using **Facebook Prophet** for Heart Rate, Steps, and Sleep.
* Forecasted expected values and calculated residuals to identify unusual deviations.
* Visualized trends with confidence intervals for each metric.

### 3. Behavioral Clustering

* Combined TSFresh features with demographic and activity data.
* Encoded categorical variables (`BMI Category`, `Stress Level`, `Physical Activity Level`).
* Imputed missing values using column mean.
* Scaled features using **StandardScaler**.
* Applied **KMeans clustering** to identify behavioral groups.
* Visualized clusters with **PCA**.

---

## Tools and Libraries Used

* Python 3.x
* pandas
* numpy
* TSFresh
* Prophet
* scikit-learn
* matplotlib

---

## Observations

* **Statistical Features:**

  * Heart Rate Mean: (add value)
  * Steps Standard Deviation: (add value)
  * Sleep Duration Skewness: (add value)

* **Trend Analysis:**

  * Forecast plots showed expected trends and deviations for each metric.
  * Residual analysis highlighted potential anomalies.

* **Behavioral Clustering:**

  * Cluster 0 → Normal behavior
  * Cluster 1 → High stress / atypical patterns
  * Cluster 2 → Moderate deviations

---

## Folder Structure

```
Milestone2/
├── feature_extraction.py
├── modeling.py
├── requirements.txt
├── README.md
└── data/
    └── Clean.csv

