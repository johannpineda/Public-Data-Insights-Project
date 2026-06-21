import pandas as pd
import numpy as np

np.random.seed(42)

n = 120000

df = pd.DataFrame({

    "Date": pd.date_range(
        start="2020-01-01",
        periods=n,
        freq="h"
    ),

    "City": np.random.choice([
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Miami"
    ], n),

    "Category": np.random.choice([
        "Transport",
        "Housing",
        "Food",
        "Entertainment",
        "Healthcare"
    ], n),

    "Value": np.random.randint(10, 500, n),

    "Users": np.random.randint(1, 20, n)

})

df.to_csv(
    "../data/public_data.csv",
    index=False
)

print("Dataset created")