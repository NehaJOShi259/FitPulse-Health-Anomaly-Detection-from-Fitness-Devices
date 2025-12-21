import pandas as pd
import numpy as np
from pathlib import Path


def load_data(data_path):
    """
    Load raw fitness datasets from CSV files and convert timestamps to UTC.
    """
    activity = pd.read_csv(data_path / "dailyActivity_merged.csv")
    heart = pd.read_csv(data_path / "heartrate_seconds_sample.csv")
    sleep = pd.read_csv(data_path / "sleepDay_merged.csv")

    # Convert timestamps to datetime (UTC)
    activity["ActivityDate"] = pd.to_datetime(activity["ActivityDate"], utc=True)
    heart["Time"] = pd.to_datetime(heart["Time"], utc=True)
    sleep["SleepDay"] = pd.to_datetime(sleep["SleepDay"], utc=True)

    return activity, heart, sleep



def main():
    data_path = Path("data")
    activity, heart, sleep = load_data(data_path)
    
    print("Data loaded successfully")
    print("Activity shape:", activity.shape)
    print("Heart rate shape:", heart.shape)
    print("Sleep shape:", sleep.shape)


if __name__ == "__main__":
    main()

