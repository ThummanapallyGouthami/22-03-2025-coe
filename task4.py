# Creating a dataset with float values
import pandas as pd
import numpy as np

data = {'sales_amount': np.random.random(1000000)}  # Random float values
df = pd.DataFrame(data)

# Check the default data type
print(df['sales_amount'].dtype)  # This will show float64

# Convert to float32 for memory optimization
df['sales_amount'] = df['sales_amount'].astype(np.float32)

# Check the memory usage
print(f"Memory Usage: {df.memory_usage(deep=True)}")

# float32 takes 4 bytes compared to 8 bytes for float64.