# Creating a dataset with repeated string values
import pandas as pd
data = {'city': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles'] * 100000}
df = pd.DataFrame(data)

# Check the memory usage with object type
print(df['city'].dtype)  # This will show object (i.e., string)

# Convert to category type
df['city'] = df['city'].astype('category')

# Check the memory usage after conversion
print(f"Memory Usage: {df.memory_usage(deep=True)}")