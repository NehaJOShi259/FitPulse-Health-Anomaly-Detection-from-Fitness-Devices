import pandas as pd
import numpy as np
from pathlib import Path


def load_data(data_path):
    """
    Load raw fitness datasets from CSV files.
    """
    activity = pd.read_csv(data_path / "dailyActivity_merged.csv")
    heart = pd.read_csv(data_path / "heartrate_seconds_merged.csv")
    sleep = pd.read_csv(data_path / "sleepDay_merged.csv")
    
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

