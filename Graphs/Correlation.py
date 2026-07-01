import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# 1. LOAD YOUR MERGED CSV DATA
# ==========================================
csv_filename = "merged_faostat_data.csv"

try:
    df = pd.read_csv(csv_filename)
    print(f"[INFO] Loaded '{csv_filename}'. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
except FileNotFoundError:
    print(f"[ERROR] Could not find '{csv_filename}' in this folder!")
    exit()

# ==========================================
# 2. EXTRACT NUMERIC DATA & CLEAN
# ==========================================
numeric_df = df.select_dtypes(include=[np.number])

# Exclude metadata columns
exclude = ["Year", "Year Code", "Area Code", "Item Code", "Element Code"]
numeric_columns = [col for col in numeric_df.columns if col not in exclude]

if len(numeric_columns) < 2:
    print("[ERROR] Not enough numeric columns to calculate correlation.")
    exit()

df_clean = df[numeric_columns].dropna()
corr_matrix = df_clean.corr(method="pearson").to_numpy() # Convert to numpy matrix
labels = list(df_clean.columns)

# ==========================================
# 3. BUILD HEATMAP USING MATPLOTLIB ONLY
# ==========================================
fig, ax = plt.subplots(figsize=(8, 7))

# Draw the matrix grid using 'coolwarm' color spectrum
im = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1.0, vmax=1.0)

# Create a clean colorbar legend
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)
cbar.ax.set_ylabel("Pearson Correlation Coefficient (r)", rotation=-90, va="bottom")

# Set up Axis ticks using the column names
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

# Rotate label text so long columns don't overlap
plt.setp(ax.get_xticklabels(), rotation=35, ha="right", rotation_mode="anchor")

# Manually loop over data dimensions and write the text values inside the cells
for i in range(len(labels)):
    for j in range(len(labels)):
        text_color = "white" if abs(corr_matrix[i, j]) > 0.5 else "black"
        ax.text(
            j, i, f"{corr_matrix[i, j]:.3f}", 
            ha="center", va="center", color=text_color, fontweight="bold"
        )

# Add titles and structural layout tweaks
ax.set_title("Correlation Analysis of Merged FAOSTAT Metrics", fontsize=14, fontweight="bold", pad=20)
fig.tight_layout()

# ==========================================
# 4. AUTOMATED SAVE AND SHOW FOR GITHUB
# ==========================================
os.makedirs("visualizations", exist_ok=True)
output_path = "visualizations/correlation_matrix.png"

plt.savefig(output_path, dpi=300, bbox_inches="tight")
print(f"[SUCCESS] Heatmap graphic file saved locally to: {output_path}")

plt.show()

