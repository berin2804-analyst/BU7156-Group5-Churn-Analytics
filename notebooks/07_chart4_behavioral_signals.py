"""
Chart 4 — Behavioural Characteristics vs Churn (Violin Plot)
Based on EDA notebook violin plot — updated colours and labelling only
Style: matches dashboard — grey background, consistent palette
Requirements: pip install matplotlib seaborn pandas scipy
Usage       : python chart4_behavioral_signals.py
              → saves chart4_behavioral_signals.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# ── Load ───────────────────────────────────────────────────────────────────
df = pd.read_csv("cleaned_ecommerce_churn_dataset.csv")
df["churn"]       = (df["subscription_status"] == "cancelled").astype(int)
df["churn_label"] = df["churn"].map({0: "Active", 1: "Churned"})

# ── Palette — matches dashboard ────────────────────────────────────────────
C_BG       = "#EFEFEF"
C_TITLE    = "#1A1A2E"
C_TEAL     = "#2A9D8F"   # Active
C_RUST     = "#E76F51"   # Churned
C_GREY     = "#777777"
FONT       = "Arial"

CHURN_PALETTE = {"Active": C_TEAL, "Churned": C_RUST}

# ── Only 3 key features (as per chart spec) ────────────────────────────────
features = [
    ("recency_days",        "Recency (Days Since Last Purchase)"),
    ("inactivity_ratio",    "Inactivity Ratio"),
    ("cancellations_count", "Cancellations Count"),
]

# ── Figure ─────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(14, 5.5))
fig.patch.set_facecolor(C_BG)

for ax, (col, label) in zip(axes, features):
    ax.set_facecolor(C_BG)

    # Violin plot
    sns.violinplot(
        x="churn_label", y=col,
        data=df,
        ax=ax,
        palette=CHURN_PALETTE,
        inner="quartile",
        linewidth=1.2,
        order=["Active", "Churned"],
    )

    # Mann-Whitney U test
    active  = df[df["churn"] == 0][col].dropna()
    churned = df[df["churn"] == 1][col].dropna()
    _, p = stats.mannwhitneyu(active, churned, alternative="two-sided")
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"

    # Median values
    med_active  = active.median()
    med_churned = churned.median()

    # Chart title
    ax.set_title(
        label,
        fontsize=12, fontweight="bold",
        color=C_TITLE, fontfamily=FONT, pad=10,
    )

    # P-value label below title
    p_color = C_RUST if p < 0.05 else C_GREY
    ax.set_xlabel(
        f"p = {p:.3f}  {sig}",
        fontsize=9, color=p_color, fontfamily=FONT,
    )

    # Median annotations
    ax.text(0, med_active  * 1.01, f"Median: {med_active:.1f}",
            ha="center", va="bottom", fontsize=8.5,
            color=C_TEAL, fontfamily=FONT, fontweight="bold")
    ax.text(1, med_churned * 1.01, f"Median: {med_churned:.1f}",
            ha="center", va="bottom", fontsize=8.5,
            color=C_RUST, fontfamily=FONT, fontweight="bold")

    # Axis styling
    ax.set_ylabel("", fontsize=10)
    ax.tick_params(colors=C_GREY, labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#AAAAAA")
    ax.spines["bottom"].set_color(C_TITLE)
    ax.spines["bottom"].set_linewidth(1.5)
    ax.spines["left"].set_linewidth(1.0)
    ax.xaxis.label.set_color(C_GREY)
    ax.tick_params(axis="x", colors=C_TITLE, labelsize=10)

# ── Legend ─────────────────────────────────────────────────────────────────
legend_patches = [
    mpatches.Patch(color=C_TEAL, label="Active"),
    mpatches.Patch(color=C_RUST, label="Churned"),
]
fig.legend(
    handles=legend_patches,
    loc="lower center",
    ncol=2,
    fontsize=11,
    frameon=False,
    bbox_to_anchor=(0.5, -0.04),
)

# ── Main title ─────────────────────────────────────────────────────────────
fig.suptitle(
    "Behavioural Characteristics vs Churn",
    fontsize=16, fontweight="bold",
    color=C_TITLE, fontfamily=FONT, y=1.02,
)

# Subtitle
fig.text(
    0.5, 0.97,
    "Churned and active customers exhibit surprisingly similar purchase patterns (all p > 0.05)",
    ha="center", fontsize=10, color=C_GREY, fontfamily=FONT,
)

plt.tight_layout()
plt.savefig(
    "chart4_behavioral_signals.png",
    dpi=180, bbox_inches="tight",
    facecolor=C_BG,
)
print("✅  Saved: chart4_behavioral_signals.png")
