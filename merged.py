import glob
import pandas as pd

# 1. Get all files matching the pattern
# Adjust extension to '.xlsx' if they are Excel instead of CSV
file_pattern = "./data/FAOSTAT_data_en_*.csv"
all_files = glob.glob(file_pattern)

# 2. Read and combine all files into a list
df_list = [pd.read_csv(file) for file in all_files]

# 3. Concatenate them vertically
merged_df = pd.concat(df_list, ignore_index=True)

# 4. Save to a new file
merged_df.to_csv("./data/merged_faostat_data.csv", index=False)
print(f"Successfully merged {len(all_files)} files!")

