# BU7156-Group5-Churn-Analytics
MSc Business Analytics (BU7156): E-commerce Customer Churn analysis using EDA, machine learning, and LLM integration. 

# Business Problem

This project aims to identify customer segments at the highest risk of churn in an e-commerce platform and recommend actionable interventions to reduce revenue loss. The analysis focuses on understanding key drivers of churn, including customer demographics (e.g., gender, country), purchasing behavior, and product categories. The primary metric of interest is the customer churn rate, along with supporting indicators that explain variations across segments.

**Primary metric:** Binary churn rate (subscription_status = cancelled)
**Secondary metric:** Revenue at risk = churned customers × average LTV ($1,025.85)

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
│   ├── processed/        # Cleaned and feature-engineered dataset ready for EDA/modelling
│   └── raw/              # Original Kaggle dataset
├── docs/                               # Contains project documentation produced by the teams
│   └── Data_Preparation_Description    # Full data cleaning and feature engineering notes
├── notebooks/                          # Contains all Jupyter notebooks and codes organised sequentially by project phase
│   └── 01_data_preparation.ipynb       # Data cleaning and feature engineering pipeline
├── outputs/              # Final exported charts and assets used in the presentation
├── prompts/              # LLM prompt logs (inputs, outputs, and critique)
└── visualizations/       # Charts and dashboards produced by the Visualisation team
```

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
See [`/prompts/LLM_Expert.pdf`](prompts/LLM_Expert_Report.pdf) for all 7 LLM prompts, full inputs, outputs, critiques, and GenAI acknowledgement per TCD guidelines.

## GenAI Acknowledgement
Generative AI tools, including Claude 3.5 Sonnet and Claude 3 Haiku (Anthropic) and GPT-4o (OpenAI), were used during the preparation of this group project across four specific workstreams: code generation for data engineering and EDA scaffolding, interpretation of model outputs into business language, drafting of 
business recommendations grounded in dataset-verified figures, and refinement of written narrative for executive communication.

All analytical decisions, model selections, feature engineering choices, and business judgements presented in this report were independently developed by the team based on our own understanding of the data, module material, and guest lecture sessions. The intellectual substance of the analysis - including the identification of churn drivers, RFM segmentation strategy, XGBoost model selection rationale, and the five targeted business recommendations - reflects the team's own critical evaluation and verification against the actual dataset.

Every LLM output was reviewed, validated, and corrected by team members before inclusion in any project deliverable. Where LLM outputs contained inaccurate figures, hallucinated insights, or statistically unverified claims, these were identified and removed. Generative AI was used as an analytical accelerant and writing-support tool and did not independently generate the core analysis, model outputs, visualisations, or conclusions presented in this submission.
