import matplotlib.pyplot as plt
import numpy as np


# Data
models = ['LR', 'RF', 'XGBoost']
metrics = ['Recall', 'Precision', 'AUC-ROC']

before_smote = {
    'Recall':    [0.41, 0.52, 0.61],
    'Precision': [0.72, 0.78, 0.81],
    'AUC-ROC':   [0.69, 0.75, 0.79]
}

after_smote = {
    'Recall':    [0.59, 0.63, 0.68],
    'Precision': [0.64, 0.71, 0.76],
    'AUC-ROC':   [0.71, 0.77, 0.82]
}


# Style
bg_color = "#efefef"
axis_color = "#1f2333"
text_grey = "#6b6b6b"
indigo = "#3F3D8F"

# Before SMOTE
before_colors = {
    'Recall': "#cfcfcf",
    'Precision': "#b8c4d6",
    'AUC-ROC': "#9fb3c8"
}

# After SMOTE
after_colors = {
    'Recall': "#de6f4b",
    'Precision': "#2f9d8f",
    'AUC-ROC': "#e3a11b"
}


# Plot setup
x = np.arange(len(models))
bar_width = 0.12

fig, ax = plt.subplots(figsize=(16, 7.5), facecolor=bg_color)
ax.set_facecolor(bg_color)

# Order within each model group:
# Recall before, Recall after, Precision before, Precision after, AUC before, AUC after
offsets = np.array([-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]) * bar_width

bars = []
bars.append(ax.bar(x + offsets[0], before_smote['Recall'], bar_width, color=before_colors['Recall'], label='Recall (Before SMOTE)'))
bars.append(ax.bar(x + offsets[1], after_smote['Recall'],  bar_width, color=after_colors['Recall'],  label='Recall (After SMOTE)'))
bars.append(ax.bar(x + offsets[2], before_smote['Precision'], bar_width, color=before_colors['Precision'], label='Precision (Before SMOTE)'))
bars.append(ax.bar(x + offsets[3], after_smote['Precision'],  bar_width, color=after_colors['Precision'],  label='Precision (After SMOTE)'))
bars.append(ax.bar(x + offsets[4], before_smote['AUC-ROC'], bar_width, color=before_colors['AUC-ROC'], label='AUC-ROC (Before SMOTE)'))
bars.append(ax.bar(x + offsets[5], after_smote['AUC-ROC'],  bar_width, color=after_colors['AUC-ROC'],  label='AUC-ROC (After SMOTE)'))


# Labels on bars
for group in bars:
    for bar in group:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            h + 0.008,
            f"{h:.2f}",
            ha='center',
            va='bottom',
            fontsize=9,
            color=axis_color,
            rotation=0
        )


# Axes and title

ax.set_title(
    "Comparison of Model Performance Before and After SMOTE",
    fontsize=22,
    fontweight='bold',
    color=indigo,
    pad=18
)

ax.set_ylabel("Score", fontsize=11, color=indigo, labelpad=10)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=11, color=indigo, fontweight='bold')

ax.tick_params(axis='y', colors=text_grey, labelsize=10, length=0)
ax.tick_params(axis='x', length=0)

ax.set_ylim(0, 0.92)

# Subtle horizontal grid
ax.yaxis.grid(True, linestyle='-', alpha=0.12)
ax.set_axisbelow(True)

# Spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color(axis_color)
ax.spines["bottom"].set_color(axis_color)
ax.spines["left"].set_linewidth(1.2)
ax.spines["bottom"].set_linewidth(1.2)


# Legend
legend = ax.legend(
    ncol=3,
    loc='upper center',
    bbox_to_anchor=(0.5, -0.10),
    frameon=False,
    fontsize=10
)
for text in legend.get_texts():
    text.set_color(axis_color)


# Annotation for key finding

xgb_index = 2
xgb_recall_after_x = x[xgb_index] + offsets[1]
xgb_recall_after_y = after_smote['Recall'][xgb_index]

ax.annotate(
    "Optimal choice\nXGBoost + SMOTE\nRecall = 0.68",
    xy=(xgb_recall_after_x, xgb_recall_after_y),
    xytext=(2.55, 0.84),
    textcoords='data',
    ha='left',
    va='center',
    fontsize=10,
    color=axis_color,
    bbox=dict(boxstyle="square,pad=0.3", fc=bg_color, ec=axis_color, lw=0.8),
    arrowprops=dict(arrowstyle="-|>", color=axis_color, lw=0.8)
)

plt.tight_layout()
plt.show()