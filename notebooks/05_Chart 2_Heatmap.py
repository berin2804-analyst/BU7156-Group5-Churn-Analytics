import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle


# Data
data = pd.DataFrame({
    "Beauty":      [22.7, 22.4, 25.0, 24.1, 15.5, 19.7],
    "Clothing":    [21.2, 23.1, 36.4, 19.5, 15.2, 25.8],
    "Electronics": [19.3, 25.0, 29.1, 32.9, 17.9, 29.7],
    "Home":        [35.2, 24.7, 30.8, 33.3, 26.2, 23.4],
    "Sports":      [17.5, 26.5, 25.8, 31.1, 24.2, 18.8]
}, index=["Canada", "Germany", "India", "Pakistan", "UK", "USA"])


# Style
bg_color = "#efefef"
axis_color = "#1f2333"
text_grey = "#6b6b6b"
indigo = "#3F3D8F"

fig, ax = plt.subplots(figsize=(14, 7.5), facecolor=bg_color)
ax.set_facecolor(bg_color)


# Heatmap (Blue gradient)
hm = sns.heatmap(
    data,
    annot=True,
    fmt=".1f",
    cmap="Blues",   # ✅ blue gradient
    linewidths=1.2,
    linecolor=bg_color,
    cbar=True,
    annot_kws={"fontsize": 11, "fontweight": "bold"},
    ax=ax
)


# Adaptive text color
for text in ax.texts:
    value = float(text.get_text())
    if value > 28:
        text.set_color("white")
    else:
        text.set_color(axis_color)


# Highlight India × Clothing

row = data.index.get_loc("India")
col = data.columns.get_loc("Clothing")

ax.add_patch(
    Rectangle(
        (col, row),
        1, 1,
        fill=False,
        edgecolor="#de6f4b",  # highlight color (same as your top feature tone)
        lw=3
    )
)


# Titles and labels (INDIGO)
ax.set_title(
    "Churn Rate (%) — Country × Preferred Category",
    fontsize=22,
    fontweight="bold",
    color=indigo,
    pad=18
)

ax.set_xlabel("Preferred Category", fontsize=12, color=indigo, labelpad=10)
ax.set_ylabel("Country", fontsize=12, color=indigo, labelpad=10)

ax.tick_params(axis="x", colors=indigo, labelsize=11, rotation=0, length=0)
ax.tick_params(axis="y", colors=indigo, labelsize=11, rotation=0, length=0)


# Colorbar styling
cbar = hm.collections[0].colorbar
cbar.ax.tick_params(labelsize=10, colors=text_grey, length=0)
cbar.set_label("Churn Rate (%)", fontsize=11, color=indigo, labelpad=10)

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()