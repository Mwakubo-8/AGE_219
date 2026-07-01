import matplotlib.pyplot as plt
import pandas as pd

# Load your combined/merged file (CSV, Excel, or Feather format)
# df = pd.read_csv("merged_faostat_data.csv")

# Simulated structure of your merged dataset
data_dict = {
"Area": ["Tanzania"] * 5 + ["Kenya"] * 5,
"Item": ["Maize"] * 10,
"Element": ["Yield"] * 10,
"Year": [2016, 2017, 2018, 2019, 2020] * 2,
"Value": [1.5, 1.6, 1.4, 1.8, 1.9, 1.2, 1.3, 1.1, 1.4, 1.5],
}
df = pd.DataFrame(data_dict)

# Filter the merged dataframe for a specific segment
filtered_df = df[(df["Area"] == "Tanzania") & (df["Item"] == "Maize")]

# Plotting the timeline
plt.figure(figsize=(10, 5))
plt.plot(
    filtered_df["Year"],
    filtered_df["Value"],
    marker="s",
    color="#e377c2",
    linewidth=2.5,
    label="Maize Yield",
)

plt.title("Tanzania: Maize Yield Trend Analysis (2016-2020)", fontsize=14, pad=15)
plt.xlabel("Year (Calendar Year)", fontsize=11, labelpad=10)
plt.ylabel("Yield (Tonnes per Hectare - t/ha)", fontsize=11, labelpad=10)

plt.xticks(filtered_df["Year"])
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()
