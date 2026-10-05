"""
HormoCycleAI — Public Streamlit Dashboard Configuration
"""

import os

# Repository root
BASE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DATA_DIR = os.path.join(BASE, "data")

# Public synthetic dashboard dataset
DASHBOARD_DATASET = os.path.join(
    DATA_DIR,
    "dashboard_dataset.csv"
)

# Global XAI context
XAI_CONTEXT = os.path.join(
    DATA_DIR,
    "xai_context.csv"
)

# Validated aggregate model comparison
MODEL_COMPARISON = os.path.join(
    DATA_DIR,
    "model_comparison.csv"
)

APP_TITLE = "HormoCycleAI"

APP_SUBTITLE = (
    "Explainable Multimodal AI for Personalized "
    "Menstrual and Reproductive Health Forecasting"
)

RESEARCH_ONLY = True
CLINICAL_USE_SUPPORTED = False
DIAGNOSTIC_USE_SUPPORTED = False
TREATMENT_DECISION_SUPPORTED = False

PUBLIC_DEMO = True
PUBLIC_DATASET_IS_SYNTHETIC = True
