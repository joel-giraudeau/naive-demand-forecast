import numpy as np
import pandas as pd


def generate_synthetic_demand(
    start_date="2023-01-01",
    periods=730,
    seed=42
):
    """
    Generate synthetic daily demand data with trend,
    weekly seasonality, and random noise.
    """

    np.random.seed(seed)

    dates = pd.date_range(start=start_date, periods=periods, freq="D")

    trend = np.linspace(50, 70, periods)
    seasonality = 10 * np.sin(2 * np.pi * dates.dayofyear / 7)
    noise = np.random.normal(0, 5, periods)

    demand = trend + seasonality + noise

    df = pd.DataFrame({
        "date": dates,
        "demand": demand
    })

    return df


if __name__ == "__main__":
    df = generate_synthetic_demand()
    df.to_csv("data/synthetic_demand.csv", index=False)
    print("Synthetic dataset saved to data/synthetic_demand.csv")