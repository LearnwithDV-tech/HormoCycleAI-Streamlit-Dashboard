import os

# ============================================================
# PUBLIC STREAMLIT DEPLOYMENT CONFIGURATION
# ============================================================

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE, "data")

DASHBOARD_DATASET = os.path.join(
    DATA_DIR,
    "dashboard_dataset.csv"
)

XAI_CONTEXT = os.path.join(
    DATA_DIR,
    "xai_context.csv"
)

MODEL_COMPARISON = os.path.join(
    DATA_DIR,
    "model_comparison.csv"
)

APP_TITLE = "HormoCycleAI"
APP_SUBTITLE = (
    "Explainable Multimodal Reproductive Health "
    "Forecasting — Research Demonstration"
)

PUBLIC_DEMO = True
PUBLIC_DATASET_IS_SYNTHETIC = True

ARHI_NAME = "AI-based Reproductive Health Index (ARHI)"
ARHI_SCALE_MIN = 0
ARHI_SCALE_MAX = 100

CLINICAL_USE_SUPPORTED = False
DIAGNOSTIC_USE_SUPPORTED = False
TREATMENT_USE_SUPPORTED = False
FERTILITY_INTERPRETATION_SUPPORTED = False
