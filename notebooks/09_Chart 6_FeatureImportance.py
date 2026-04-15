import matplotlib.pyplot as plt
import numpy as np


# Data
features = [
    "Gender: Male",
    "high_cancel_risk",
    "preferred_category_Home",
    "category_Sports",
    "category_Home",
    "category_Electronics",
    "Country: Pakistan",
    "preferred_category_Clothing",
    "preferred_category_Electronics",
    "Country: UK"
]

importance = [0.085, 0.072, 0.070, 0.066, 0.065, 0.057, 0.055, 0.054, 0.054, 0.049]

# Reverse for plotting
features_plot = features[::-1]
importance_plot = importance[::-1]

# Style
bg_color = "#efefef"
axis_color = "#1f2333"
text_grey = "#6b6b6b"
indigo = "#3F3D8F"

bar_colors = [
    "#8bbfba",
    "#8bbfba",
    "#8bbfba",
    "#8bbfba",
    "#8bbfba",
    "#8bbfba",
    "#8bbfba",
    "#e3a11b",
    "#2f9d8f",
    "#de6f4b"
]

# Plot
fig, ax = plt.subplots(figsize=(16, 7.2), facecolor=bg_color)
ax.set_facecolor(bg_color)

bars = ax.barh(features_plot, importance_plot, color=bar_colors, edgecolor=bg_color, height=0.82)

# Value labels
for i, v in enumerate(importance_plot):
    ax.text(v + 0.0004, i, f"{v:.3f}",
            va="center", ha="left",
            fontsize=10, color=axis_color)

# Title and axis labels (INDIGO)
ax.set_title(
    "XGBoost Feature Importance: Which Metrics Matter Most for Churn?",
    fontsize=22, fontweight="bold", color=indigo, pad=18
)
ax.set_xlabel("Importance Score", fontsize=11, color=indigo, labelpad=10)

# Y-axis labels in indigo
ax.tick_params(axis="y", colors=indigo, labelsize=11)
ax.tick_params(axis="x", colors=text_grey, labelsize=9, length=0)

# Axes styling
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color(axis_color)
ax.spines["bottom"].set_color(axis_color)
ax.spines["left"].set_linewidth(1.2)
ax.spines["bottom"].set_linewidth(1.2)

# X-axis ticks
ax.set_xlim(0, 0.102)  # extended slightly to give annotation room
xticks = np.arange(0, 0.11, 0.01)
ax.set_xticks(xticks)
ax.set_xticklabels([f"{x:.2f}" if x > 0 else "0" for x in xticks])


# Improved annotation placement
top_idx = len(features_plot) - 1
top_val = importance_plot[top_idx]

ax.annotate(
    "Top driver",
    xy=(top_val, top_idx),
    xytext=(0.097, top_idx),  # shifted further right
    va="center",
    ha="left",
    fontsize=10,
    color=axis_color,
    bbox=dict(boxstyle="square,pad=0.25", fc=bg_color, ec=axis_color, lw=0.8),
    arrowprops=dict(arrowstyle="-|>", lw=0.8, color=axis_color)
)

plt.tight_layout()
plt.show()