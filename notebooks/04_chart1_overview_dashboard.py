"""
Chart 1 — E-Commerce Platform Data Overview  (v9)
Requirements: pip install plotly pandas
Usage       : python chart1_overview_dashboard.py
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── Load ───────────────────────────────────────────────────────────────────
df = pd.read_csv("cleaned_ecommerce_churn_dataset.csv")
df["age_group"] = pd.cut(
    df["age"],
    bins=[17, 25, 35, 45, 55, 70],
    labels=["18–25", "26–35", "36–45", "46–55", "56–70"],
)

# ── Palette ────────────────────────────────────────────────────────────────
C_BG    = "#EFEFEF"
C_TITLE = "#1A1A2E"
C_GREY  = "#777777"
C_GRID  = "#E0E0E0"
C_TEAL  = "#2A9D8F"
C_RUST  = "#E76F51"
C_GOLD  = "#E9A820"
C_BLUE  = "#3A7CA5"
C_SLATE = "#4A6FA5"
C_LIGHT = "#90C8C2"
FONT    = "Arial, sans-serif"

AGE_COLORS = [C_LIGHT, C_TEAL, C_SLATE, C_RUST, C_TITLE]

CONTINENT = {
    "Germany": C_BLUE,  "UK": C_BLUE,
    "Pakistan": C_GOLD, "India": C_GOLD,
    "USA": C_TEAL,      "Canada": C_TEAL,
}

CAT_COLORS = ["#E76F51", "#F4A261", "#E9A820", "#2A9D8F", "#3A7CA5"]

# ── Pre-compute ────────────────────────────────────────────────────────────
total       = len(df)
churn_rate  = (df["subscription_status"] == "cancelled").sum() / total * 100
ltv_median  = df["monetary"].median()
total_rev   = df["monetary"].sum()
avg_tenure  = df["tenure_days"].mean()

n_active    = (df["subscription_status"] == "active").sum()
n_cancelled = (df["subscription_status"] == "cancelled").sum()
n_paused    = (df["subscription_status"] == "paused").sum()
churned_rev = df[df["subscription_status"] == "cancelled"]["monetary"].sum()
paused_rev  = df[df["subscription_status"] == "paused"]["monetary"].sum()
exposure    = churned_rev + paused_rev

gender_vc  = df["gender"].value_counts()
age_vc     = df["age_group"].value_counts().sort_index()
country_vc = df["country"].value_counts()
cat_vc     = df["preferred_category"].value_counts().sort_values()

# ── Subplots ───────────────────────────────────────────────────────────────
fig = make_subplots(
    rows=2, cols=3,
    column_widths=[0.34, 0.26, 0.40],
    row_heights=[0.38, 0.62],
    specs=[
        [{"type": "xy"},     {"type": "domain"}, {"type": "xy", "rowspan": 2}],
        [{"type": "xy"},     {"type": "domain"}, None                        ],
    ],
    horizontal_spacing=0.08,
    vertical_spacing=0.20,
)

# ════════════════════════════════════════════════════════════════════════════
# ROW 1 COL 1 — Customer Age Group Distribution
# ════════════════════════════════════════════════════════════════════════════
age_labels = age_vc.index.tolist()
age_vals   = age_vc.values.tolist()

fig.add_trace(go.Bar(
    y=age_labels, x=age_vals,
    orientation="h", width=0.5,
    marker=dict(color=AGE_COLORS, line=dict(width=0)),
    text=[f"  {v:,} ({v/total*100:.0f}%)" for v in age_vals],
    textposition="outside",
    textfont=dict(size=10, family=FONT, color=C_TITLE),
    hovertemplate="<b>Age %{y}</b><br>Count: %{x:,}<extra></extra>",
    showlegend=False,
), row=1, col=1)

fig.update_xaxes(
    range=[0, 780], showgrid=False,
    showticklabels=True, tickfont=dict(size=9, color=C_GREY, family=FONT),
    zeroline=False, showline=True, linecolor="#1A1A2E", linewidth=1.5,
    title_text="No. of Customers",
    title_font=dict(size=10, color=C_GREY, family=FONT),
    row=1, col=1,
)
fig.update_yaxes(
    showgrid=False, zeroline=False,
    showline=True, linecolor="#1A1A2E", linewidth=1.5,
    tickfont=dict(size=10, color=C_TITLE, family=FONT),
    row=1, col=1,
)

# ════════════════════════════════════════════════════════════════════════════
# ROW 1 COL 2 — Customer Gender Breakdown
# ════════════════════════════════════════════════════════════════════════════
fig.add_trace(go.Pie(
    labels=["Female", "Male", "Other"],
    values=[gender_vc.get("Female", 0),
            gender_vc.get("Male",   0),
            gender_vc.get("Other",  0)],
    hole=0.50,
    marker=dict(colors=[C_TEAL, C_RUST, C_GOLD],
                line=dict(color=C_BG, width=3)),
    textinfo="label+percent",
    textfont=dict(size=11, family=FONT),
    insidetextorientation="radial",
    hovertemplate="<b>%{label}</b><br>Count: %{value:,}<br>%{percent}<extra></extra>",
    showlegend=False,
), row=1, col=2)

# ════════════════════════════════════════════════════════════════════════════
# ROW 2 COL 1 — Customer Distribution by Country
# ════════════════════════════════════════════════════════════════════════════
countries = country_vc.index.tolist()
c_vals    = country_vc.values.tolist()

fig.add_trace(go.Bar(
    y=countries, x=c_vals,
    orientation="h", width=0.5,
    marker=dict(color=[CONTINENT.get(c, C_GREY) for c in countries],
                line=dict(width=0)),
    text=[f"  {v:,} ({v/total*100:.0f}%)" for v in c_vals],
    textposition="outside",
    textfont=dict(size=10, family=FONT, color=C_TITLE),
    hovertemplate="<b>%{y}</b><br>Count: %{x:,}<extra></extra>",
    showlegend=False,
), row=2, col=1)

fig.update_xaxes(
    range=[0, 490], showgrid=False,
    showticklabels=True, tickfont=dict(size=9, color=C_GREY, family=FONT),
    zeroline=False, showline=True, linecolor="#1A1A2E", linewidth=1.5,
    title_text="No. of Customers",
    title_font=dict(size=10, color=C_GREY, family=FONT),
    row=2, col=1,
)
fig.update_yaxes(
    showgrid=False, zeroline=False,
    showline=True, linecolor="#1A1A2E", linewidth=1.5,
    tickfont=dict(size=10, color=C_TITLE, family=FONT),
    row=2, col=1,
)

# Continent legend
for i, (label, color) in enumerate([
    ("■  Europe",        C_BLUE),
    ("■  South Asia",    C_GOLD),
    ("■  North America", C_TEAL),
]):
    fig.add_annotation(
        x=i * 0.115, y=-0.06,
        xref="paper", yref="paper",
        text=f"<span style='color:{color};font-size:10px'>{label}</span>",
        showarrow=False, align="left",
        font=dict(family=FONT),
    )

# ════════════════════════════════════════════════════════════════════════════
# ROW 2 COL 2 — Subscription Status Overview
# ════════════════════════════════════════════════════════════════════════════
fig.add_trace(go.Pie(
    labels=["Active", "Cancelled", "Paused"],
    values=[n_active, n_cancelled, n_paused],
    hole=0.55,
    marker=dict(colors=[C_TEAL, C_RUST, C_GOLD],
                line=dict(color=C_BG, width=3)),
    textinfo="label+percent",
    textfont=dict(size=10, family=FONT),
    hovertemplate="<b>%{label}</b><br>Customers: %{value:,}<br>%{percent}<extra></extra>",
    showlegend=False,
    domain=dict(x=[0.355, 0.595], y=[0.08, 0.44]),
), row=2, col=2)

# Revenue at Risk — LEFT of donut, no overlap with Category
fig.add_annotation(
    x=0.40, y=0.42,
    xref="paper", yref="paper",
    xanchor="right",
    text=(
        f"<b style='color:{C_RUST};font-size:11px'>⚠  Revenue at Risk</b><br>"
        f"<span style='font-size:10px;color:{C_TITLE}'>"
        f"Churned: <b>${churned_rev/1e6:.3f}M</b> ({churned_rev/total_rev*100:.1f}%)<br>"
        f"Paused:  <b>${paused_rev/1e6:.3f}M</b> ({paused_rev/total_rev*100:.1f}%)<br>"
        f"<b style='color:{C_RUST}'>Total: ${exposure/1e6:.3f}M (40.0%)</b>"
        f"</span>"
    ),
    showarrow=False, align="left",
    bordercolor=C_RUST, borderwidth=1.5,
    borderpad=9, bgcolor="#FFF4F2",
    font=dict(family=FONT),
)

# ════════════════════════════════════════════════════════════════════════════
# ROW 1+2 COL 3 — Product Category Preference
# ════════════════════════════════════════════════════════════════════════════
cat_labels = cat_vc.index.tolist()
cat_vals   = cat_vc.values.tolist()

fig.add_trace(go.Bar(
    y=cat_labels, x=cat_vals,
    orientation="h", width=0.40,
    marker=dict(color=CAT_COLORS, line=dict(width=0)),
    text=[f"  {v:,} ({v/total*100:.0f}%)" for v in cat_vals],
    textposition="outside",
    textfont=dict(size=10, family=FONT, color=C_TITLE),
    hovertemplate="<b>%{y}</b><br>Count: %{x:,}<extra></extra>",
    showlegend=False,
), row=1, col=3)

fig.update_xaxes(
    range=[0, 560], showgrid=False,
    showticklabels=True, tickfont=dict(size=9, color=C_GREY, family=FONT),
    zeroline=False, showline=True, linecolor="#1A1A2E", linewidth=1.5,
    title_text="No. of Customers",
    title_font=dict(size=10, color=C_GREY, family=FONT),
    row=1, col=3,
)
fig.update_yaxes(
    showgrid=False, zeroline=False,
    showline=True, linecolor="#1A1A2E", linewidth=1.5,
    tickfont=dict(size=11, color=C_TITLE, family=FONT),
    range=[-0.8, 4.8],
    row=1, col=3,
)

# ════════════════════════════════════════════════════════════════════════════
# CHART TITLES
# ════════════════════════════════════════════════════════════════════════════
chart_titles = [
    (0.17,  1.06, "Customer Age Group Distribution"),
    (0.475, 1.06, "Customer Gender Breakdown"),
    (0.82,  1.06, "Product Category Preference by Customer Count"),
    (0.17,  0.54, "Customer Distribution by Country"),
    (0.475, 0.54, "Subscription Status Overview"),
]
for x, y, text in chart_titles:
    fig.add_annotation(
        x=x, y=y, xref="paper", yref="paper",
        text=f"<b style='font-size:12px;color:{C_TITLE}'>{text}</b>",
        showarrow=False, align="center", xanchor="center",
        font=dict(family=FONT),
    )

# ════════════════════════════════════════════════════════════════════════════
# KPI CARDS
# ════════════════════════════════════════════════════════════════════════════
kpis = [
    ("Overall Churn Rate",  f"{churn_rate:.1f}%",       C_RUST,  "Cancelled customers"),
    ("Life Time Value",     f"${ltv_median:,.0f}",       C_TITLE, "Monetary median"),
    ("Total Revenue",       f"${total_rev/1e6:.2f}M",    C_TITLE, "All customers"),
    ("Avg Customer Tenure", f"{avg_tenure/365:.1f} yrs", C_TEAL,  f"≈ {avg_tenure:.0f} days"),
]
kpi_xs = [0.11, 0.37, 0.63, 0.89]

for x, (title, value, color, sub) in zip(kpi_xs, kpis):
    fig.add_annotation(
        x=x, y=1.235, xref="paper", yref="paper",
        text=f"<b style='font-size:28px;color:{color}'>{value}</b>",
        showarrow=False, align="center", font=dict(family=FONT),
    )
    fig.add_annotation(
        x=x, y=1.150, xref="paper", yref="paper",
        text=f"<b style='font-size:11px;color:{C_TITLE}'>{title}</b>",
        showarrow=False, align="center", font=dict(family=FONT),
    )
    fig.add_annotation(
        x=x, y=1.095, xref="paper", yref="paper",
        text=f"<span style='font-size:9px;color:{C_GREY}'>{sub}</span>",
        showarrow=False, align="center", font=dict(family=FONT),
    )

fig.add_shape(
    type="line", x0=0.0, x1=1.0, y0=1.060, y1=1.060,
    xref="paper", yref="paper",
    line=dict(color="#CCCCCC", width=1),
)

# ════════════════════════════════════════════════════════════════════════════
# GLOBAL LAYOUT
# ════════════════════════════════════════════════════════════════════════════
fig.update_layout(
    title=dict(
        text="<b>E-Commerce Platform Data Overview</b>",
        x=0.5, xanchor="center", y=0.987,
        font=dict(size=24, color=C_TITLE, family=FONT),
    ),
    paper_bgcolor=C_BG,
    plot_bgcolor=C_BG,
    font=dict(family=FONT, color=C_TITLE, size=11),
    showlegend=False,
    bargap=0.4,
    height=750,
    margin=dict(t=200, b=70, l=60, r=60),
)

fig.write_html("chart1_overview_dashboard.html")
print("✅  Saved: chart1_overview_dashboard.html")
