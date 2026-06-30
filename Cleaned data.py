import pandas as pd

# 1. Load the dataset
df = pd.read_csv('merged_faostat_data.csv')

# 2. Drop completely duplicate rows
df.drop_duplicates(inplace=True)

# 3. Strip whitespace from text columns
str_cols = df.select_dtypes(include=['object']).columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# 4. Handle missing values in critical columns (e.g., Value)
# Replace missing numeric values with 0 or drop them
df['Value'] = df['Value'].fillna(0) 

# 5. Save the cleaned file
df.to_csv('cleaned_faostat_data.csv', index=False)
print("Data cleaning complete!")
