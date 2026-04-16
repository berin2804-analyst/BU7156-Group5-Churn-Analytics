# BU7156-Group5-Churn-Analytics
MSc Business Analytics (BU7156): E-commerce Customer Churn analysis using EDA, machine learning, and LLM integration. 

# Business Problem

This project aims to identify customer segments at the highest risk of churn in an e-commerce platform and recommend actionable interventions to reduce revenue loss. The analysis focuses on understanding key drivers of churn, including customer demographics (e.g., gender, country), purchasing behavior, and product categories. The primary metric of interest is the customer churn rate, along with supporting indicators that explain variations across segments.

**Primary metric:** Binary churn rate (subscription_status = cancelled)
**Secondary metric:** Revenue at risk = churned customers × average LTV (€1,025.85)

# Team Roles

| Name               | Role                 |
| ------------------ | -------------------- |
| Berin Biju Chandy  | Project Manager      |
| Patrick Madubuko   | Project Manager      |
| Sin You Tok        | Data Engineering     |
| Jia Hui Duan       | Data Engineering     |
| Su-Han Chang       | Modelling & Analysis |
| Fida Rao           | Modelling & Analysis |
| Akshat Srivastava  | Visualization        |
| Diyun Chen         | Visualization        |
| Yashvardhan Sharma | LLM Specialist       |
| Ka'Mia Mungo       | LLM Specialist       |

## Repository Structure

```
BU7156-Group5-Churn-Analytics/
├── README.md
├── data/                 # Contains all datasets used in this project 
│   ├── processed/
│   │   └── cleaned_ecommerce_churn_dataset.csv   # Cleaned, feature-engineered dataset
│   ├── raw/  # Original Kaggle dataset
│   │   └── E Commerce Customer Insights and Churn Dataset.csv   # Cleaned, feature-engineered dataset
├── docs/                               # Contains project documentation produced by the teams
│   └── Data_Preparation_Description    # Full data cleaning and feature engineering notes
│   └── Modelling_Documentation.pdf     # Full data cleaning and feature engineering notes
├── notebooks/
│   ├── 01_data_preparation.ipynb       # Step 1: Data ingestion, cleaning, feature engineering
│   ├── 02_eda.ipynb                    # Step 2: Exploratory data analysis
│   ├── 03_modelling.ipynb              # Step 3: Model training, SMOTE, evaluation, and feature importance
│   ├── 04_chart1_overview_dashboard.py # Interactive Plotly dashboard 
│   ├── 05_Chart 2_Heatmap.py           # Churn rate heatmap - country × preferred category
│   ├── 06_chart3_rfm_segments.py       # RFM segment bubble chart - churn rate vs. recency by segment
│   ├── 07_chart4_behavioral_signals.py # Violin plots - behavioural features vs. churn
│   ├── 08_Chart 5_Comparison.py        # Model performance comparison - before and after SMOTE across LR, RF, XGBoost
│   └── 09_Chart 6_FeatureImportance.py # XGBoost feature importance - top 10 churn predictors
├── outputs/              # Final exported charts and assets used in the presentation
├── prompts/              # LLM prompt logs (inputs, outputs, and critique)
│   └── LLM_Expert_Report.pdf  # Full LLM workstream - 7 prompts, exact inputs/outputs, critiques
└── visualizations/       # Charts and dashboards produced by the Visualisation team
│   └── Chart_2_Heatmap.png
│   ├── Chart_5_Comparison.png
│   ├── Chart_6_FeatureImportance.png
│   ├── chart1_overview.png
│   ├── chart3_rfm_segments.png
│   └── chart4_behavioral_signals.png
```
## How to Run

1. Clone the repository
```bash
   git clone https://github.com/berin2804-analyst/BU7156-Group5-Churn-Analytics.git
   cd BU7156-Group5-Churn-Analytics
```

2. Install dependencies
```bash
   pip install pandas scikit-learn xgboost imbalanced-learn plotly seaborn matplotlib scipy
```

3. Download the raw dataset from the Kaggle link above and place it in `data/raw/`

4. Run notebooks from `notebooks/` in order below
```bash
   notebooks/01_data_preparation.ipynb
   notebooks/02_eda.ipynb
   notebooks/03_modelling.ipynb
```
   
6. To reproduce individual charts, run the corresponding Python scripts from `notebooks/`
```bash
   python notebooks/04_chart1_overview_dashboard.py
   python notebooks/05_Chart 2_Heatmap.py
   python notebooks/06_chart3_rfm_segments.py
   python notebooks/07_chart4_behavioral_signals.py
   python notebooks/08_Chart 5_Comparison.py
   python notebooks/09_Chart 6_FeatureImportance.py
```

> **Note:** Chart scripts require the cleaned dataset at `data/processed/cleaned_ecommerce_churn_dataset.csv`. Run `01_data_preparation.ipynb` first.


## Data Preparation
- Raw dataset cleaned and processed by the Data Engineering team
- Key features engineered: `recency_days`, `tenure_days`, `monetary`, `purchase_intensity`, `inactivity_ratio`
- Outliers retained strategically - tree-based models handle variance
- Full preparation notes: [`docs/Data_Preparation_Description`](docs/Data_Preparation_Description)
    
## Key Findings
- Overall churn rate: **24.6%** (493 of 2,000 customers)
- Home category has the highest churn rate at **28.6%** — 6.9pp above Beauty (21.7%)
- India (29.3%) and Pakistan (28.0%) show the highest country-level churn risk
- Top risk combination: India × Clothing at **36.4%** churn rate
- Champions RFM segment churns at **27.8%** — even the most engaged customers are at risk
- All behavioural features (recency, frequency, monetary) returned **p > 0.05** — churn is driven by WHO the customer is, not HOW they transact
- XGBoost (SMOTE, n=20) selected as best model: **Recall = 0.68**, identifying €68,731 in recoverable revenue

## Prompts Log
See [`/prompts/LLM_Expert_Report.pdf`](prompts/LLM_Expert_Report.pdf) for all 7 LLM prompts, full inputs, outputs, critiques, and GenAI acknowledgement per TCD guidelines.

## GenAI Acknowledgement
Generative AI tools, including Claude 3.5 Sonnet and Claude 3 Haiku (Anthropic) and GPT-4o (OpenAI), were used during the preparation of this group project across four specific workstreams: code generation for data engineering and EDA scaffolding, interpretation of model outputs into business language, drafting of 
business recommendations grounded in dataset-verified figures, and refinement of written narrative for executive communication.

All analytical decisions, model selections, feature engineering choices, and business judgements presented in this report were independently developed by the team based on our own understanding of the data, module material, and guest lecture sessions. The intellectual substance of the analysis - including the identification of churn drivers, RFM segmentation strategy, XGBoost model selection rationale, and the five targeted business recommendations - reflects the team's own critical evaluation and verification against the actual dataset.

Every LLM output was reviewed, validated, and corrected by team members before inclusion in any project deliverable. Where LLM outputs contained inaccurate figures, hallucinated insights, or statistically unverified claims, these were identified and removed. Generative AI was used as an analytical accelerant and writing-support tool and did not independently generate the core analysis, model outputs, visualisations, or conclusions presented in this submission.
