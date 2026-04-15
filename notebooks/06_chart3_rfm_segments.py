"""
Chart 3 — RFM Segment Analysis: Who Are We Losing?
Style: matches Chart 1 dashboard — grey background, black axes, no grid
Requirements: pip install plotly pandas kaleido
Usage       : python chart3_rfm_segments.py
              → saves chart3_rfm_segments.html + chart3_rfm_segments.png
"""

import pandas as pd
import plotly.graph_objects as go

# ── Load & build RFM segments ──────────────────────────────────────────────
df = pd.read_csv("cleaned_ecommerce_churn_dataset.csv")
df["churn"] = (df["subscription_status"] == "cancelled").astype(int)

df["R_score"] = pd.qcut(df["recency_days"], q=4, labels=[4,3,2,1]).astype(int)
df["F_score"] = pd.qcut(df["frequency"],    q=4, labels=[1,2,3,4]).astype(int)
df["M_score"] = pd.qcut(df["monetary"],     q=4, labels=[1,2,3,4]).astype(int)
df["RFM_score"] = df["R_score"] + df["F_score"] + df["M_score"]

def segment(score):
    if score >= 10: return "Champions"
    elif score >= 8: return "Loyal Customers"
    elif score >= 6: return "Potential Loyalists"
    elif score >= 4: return "At Risk"
    else:            return "Lost"

df["segment"] = df["RFM_score"].apply(segment)

seg = (
    df.groupby("segment")
    .agg(
        n           = ("churn", "count"),
        churn_rate  = ("churn", "mean"),
        avg_monetary= ("monetary", "mean"),
        avg_recency = ("recency_days", "mean"),
    )
    .reset_index()
)
seg["churn_pct"] = (seg["churn_rate"] * 100).round(1)

# ── Palette ────────────────────────────────────────────────────────────────
C_BG    = "#EFEFEF"
C_TITLE = "#1A1A2E"
C_GREY  = "#777777"
C_TEAL  = "#2A9D8F"
C_RUST  = "#E76F51"
C_GOLD  = "#E9A820"
C_BLUE  = "#3A7CA5"
C_SLATE = "#4A6FA5"
C_LIGHT = "#90C8C2"
FONT    = "Arial, sans-serif"

SEG_ORDER  = ["Champions", "Loyal Customers", "Potential Loyalists", "At Risk", "Lost"]
SEG_COLORS = [C_RUST, C_TEAL, C_GOLD, C_SLATE, C_LIGHT]

seg["order"] = seg["segment"].map({s: i for i, s in enumerate(SEG_ORDER)})
seg = seg.sort_values("order")

avg_churn = seg["churn_pct"].mean()

# ── Figure ─────────────────────────────────────────────────────────────────
fig = go.Figure()

for _, row in seg.iterrows():
    color = SEG_COLORS[int(row["order"])]

    fig.add_trace(go.Scatter(
        x=[row["avg_recency"]],
        y=[row["churn_pct"]],
        mode="markers+text",
        name=row["segment"],
        marker=dict(
            size=row["n"] / 7,
            color=color,
            opacity=0.88,
            line=dict(width=0),
        ),
        text=row["segment"],
        textposition="top center",
        textfont=dict(size=11, color=C_TITLE, family=FONT),
        hovertemplate=(
            f"<b>{row['segment']}</b><br>"
            f"Customers: {row['n']:,}<br>"
            f"Churn Rate: {row['churn_pct']}%<br>"
            f"Avg Spend: ${row['avg_monetary']:,.0f}<br>"
            f"Avg Recency: {row['avg_recency']:.0f} days"
            "<extra></extra>"
        ),
        showlegend=True,
    ))

# Average churn reference line
fig.add_hline(
    y=avg_churn,
    line_dash="dash", line_color=C_GREY, line_width=1.5,
    annotation_text="",
    annotation_font=dict(size=10, color=C_GREY, family=FONT),
    annotation_position="right",
)


# Bubble size note
fig.add_annotation(
    x=0.01, y=0.02,
    xref="paper", yref="paper",
    text="<i>Bubble size = number of customers in segment</i>",
    showarrow=False,
    font=dict(size=10, color=C_GREY, family=FONT),
    align="left",
)

# ── Layout ─────────────────────────────────────────────────────────────────
fig.update_layout(
    title=dict(
        text="<b>RFM Segment Analysis: Who Are We Losing?</b>",
        x=0.5, xanchor="center",
        font=dict(size=22, color=C_TITLE, family=FONT),
    ),
    xaxis=dict(
        title=dict(
            text="Average Recency (Days Since Last Purchase)",
            font=dict(size=11, color=C_GREY, family=FONT),
        ),
        showgrid=False, zeroline=False,
        showline=True, linecolor=C_TITLE, linewidth=1.5,
        tickfont=dict(size=10, color=C_GREY, family=FONT),
    ),
    yaxis=dict(
        title=dict(
            text="Churn Rate (%)",
            font=dict(size=11, color=C_GREY, family=FONT),
        ),
        showgrid=False, zeroline=False,
        showline=True, linecolor=C_TITLE, linewidth=1.5,
        tickfont=dict(size=10, color=C_GREY, family=FONT),
        range=[18, 32],
    ),
    paper_bgcolor=C_BG,
    plot_bgcolor=C_BG,
    font=dict(family=FONT, color=C_TITLE, size=11),
    height=540,
    margin=dict(t=80, b=100, l=70, r=60),
    legend=dict(
        orientation="h",
        x=0.5, xanchor="center",
        y=-0.22,
        font=dict(size=11, family=FONT),
        bgcolor="rgba(0,0,0,0)",
        itemsizing="constant",
    ),
)

# ── Export ─────────────────────────────────────────────────────────────────
fig.write_html("chart3_rfm_segments.html")
fig.write_image("chart3_rfm_segments.png", width=1400, height=540, scale=2)
print("✅  Saved: chart3_rfm_segments.html + chart3_rfm_segments.png")
