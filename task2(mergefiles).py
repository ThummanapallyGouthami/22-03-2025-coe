import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Step 1: Set up the database connection (replace with your credentials)
username = 'root'
password = '1234'
host = 'localhost'
database = 'cvr'
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
engine = create_engine(connection_string)

# Step 2: Read SQL data into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM  household_energy', engine)

# Step 3: Read the CSV file into a pandas DataFrame
df_csv = pd.read_csv(r'C:\Users\CVR\Downloads\house_hold.csv')


# Step 4: Merge the two DataFrames on 'household_id'
merged_df = pd.merge(df_sql, df_csv, on='household_id',how='outer')

pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)

print(merged_df)
print(merged_df.dtypes)
print(f"memory usage: {merged_df.memory_usage(deep=True)}")
merged_df['household_id']=merged_df['household_id'].astype(np.int16)
print(merged_df['household_id'].dtype)