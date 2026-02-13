import pandas as pd
import numpy as np

# Creating a sample dataset
data = {'order_id': np.arange(1, 1001)}  # order_id from 1 to 1000
df = pd.DataFrame(data)

# Check the default data type
print(df['order_id'].dtype)  # This will show int64
print(f"Memory Usage: {df.memory_usage(deep=True)}")
# Convert order_id to int16 (smallest type that fits)
df['order_id'] = df['order_id'].astype(np.int16)

# Check the memory usage
print(f"Memory Usage: {df.memory_usage(deep=True)}")

