import matplotlib.pyplot as plt
import pandas as pd

# Example setup from a merged breakdown
bar_dict = {
"Area": ["Tanzania"] * 4,
"Item": ["Maize", "Rice", "Wheat", "Sorghum"],
"Element": ["Production"] * 4,
"Year": [2020] * 4,
"Value": [5800, 3200, 150, 800],  # in Thousand Tonnes
}
df_bar = pd.DataFrame(bar_dict)

# Visualizing categorical totals from the merge
plt.figure(figsize=(9, 5.5))
colors = ["#4ca3dd", "#7570b3", "#d95f02", "#1b9e77"]
bars = plt.bar(
    df_bar["Item"], df_bar["Value"], color=colors, edgecolor="black", width=0.6
)

plt.title(
"Crop Production Comparison in Tanzania (Year: 2020)", fontsize=14, pad=15
)
plt.xlabel("Agricultural Crop Item", fontsize=11, labelpad=10)
plt.ylabel(
"Production Volume (Thousand Metric Tonnes - kt)", fontsize=11, labelpad=10
)

# Text tracking values over bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 100,
        f"{int(height)} kt",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
    )

plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()


