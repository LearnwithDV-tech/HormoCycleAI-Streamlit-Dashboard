
import os
import sys
import pandas as pd
import streamlit as st


# ============================================================
# PATHS
# ============================================================

BASE = "/content/drive/MyDrive/HormoCycleAI_New"

DASHBOARD_DATASET = os.path.join(
    BASE,
    "18_ARHI_Dashboard",
    "step18_6_final_publication_dashboard_dataset.csv"
)

XAI_CONTEXT = os.path.join(
    BASE,
    "18_ARHI_Dashboard",
    "step18_5_corrected_xai_dashboard_context.csv"
)

MODEL_COMPARISON = os.path.join(
    BASE,
    "16_Evaluation_Comparison",
    "step16_1_final_model_comparison.csv"
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HormoCycleAI",
    page_icon="🌸",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title(
    "🌸 HormoCycleAI"
)

st.subheader(
    "Explainable Multimodal Reproductive Health Forecasting"
)

st.info(
    """
    **Research-use dashboard**

    This dashboard presents validated research outputs from the
    HormoCycleAI experimental pipeline. It is not a diagnostic
    system, clinical health score, fertility predictor, or
    treatment-decision tool.
    """
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_dashboard_data():

    df = pd.read_csv(
        DASHBOARD_DATASET
    )

    return df


@st.cache_data
def load_xai_data():

    if os.path.exists(XAI_CONTEXT):

        return pd.read_csv(
            XAI_CONTEXT
        )

    return pd.DataFrame()


@st.cache_data
def load_model_comparison():

    if os.path.exists(MODEL_COMPARISON):

        return pd.read_csv(
            MODEL_COMPARISON
        )

    return pd.DataFrame()


df = load_dashboard_data()
xai_df = load_xai_data()
comparison_df = load_model_comparison()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Dashboard Controls"
)

participants = sorted(
    df["participant_id"]
    .dropna()
    .unique()
)

selected_participant = st.sidebar.selectbox(
    "Participant",
    participants
)

participant_df = df[
    df["participant_id"]
    == selected_participant
].copy()

participant_df = participant_df.sort_values(
    "sequence_end_day"
)

available_days = (
    participant_df[
        "sequence_end_day"
    ]
    .astype(int)
    .tolist()
)

selected_day = st.sidebar.selectbox(
    "Sequence end day",
    available_days
)

selected_row = participant_df[
    participant_df["sequence_end_day"]
    == selected_day
].iloc[0]


analyze = st.sidebar.button(
    "Analyze selected sequence",
    type="primary"
)


# ============================================================
# LANDING
# ============================================================

if not analyze:

    st.markdown(
        """
        ### How to use

        1. Select a participant.
        2. Select a validated sequence end day.
        3. Click **Analyze selected sequence**.
        4. Explore the forecast, ARHI, XAI interpretation,
           cycle information and research recommendation.

        The dashboard uses the **validated held-out research
        outputs** generated during the HormoCycleAI evaluation
        pipeline.
        """
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Held-out sequences",
        f"{len(df):,}"
    )

    c2.metric(
        "Held-out participants",
        f"{df['participant_id'].nunique():,}"
    )

    c3.metric(
        "Predicted onset",
        f"{int(df['predicted_menstrual_onset_14d'].sum()):,}"
    )

    c4.metric(
        "Research ARHI mean",
        f"{df['ARHI_research_monitoring_index'].mean():.1f}"
    )

    st.stop()


# ============================================================
# SELECTED SEQUENCE
# ============================================================

st.success(
    f"Validated research sequence selected: "
    f"Participant {selected_participant}, "
    f"sequence end day {selected_day}."
)


# ============================================================
# 1. MENSTRUAL FORECAST
# ============================================================

st.header(
    "1. Menstrual Forecast"
)

forecast = int(
    selected_row[
        "predicted_menstrual_onset_14d"
    ]
)

forecast_component = float(
    selected_row[
        "menstrual_forecast_component"
    ]
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "14-day onset forecast",
    "Possible onset"
    if forecast == 1
    else "Continue monitoring"
)

c2.metric(
    "Forecast component",
    f"{forecast_component:.1f}/100"
)

c3.metric(
    "Sequence end day",
    str(selected_day)
)

if forecast == 1:

    st.write(
        "The validated multimodal research model predicts "
        "possible menstrual onset within the next 14 days."
    )

else:

    st.write(
        "The validated multimodal research model does not "
        "predict menstrual onset within the next 14 days."
    )


# ============================================================
# 2. CYCLE CHARACTERISTICS
# ============================================================

st.header(
    "2. Menstrual Cycle Characteristics"
)

participant_history = participant_df.sort_values(
    "sequence_end_day"
)

cycle_days = participant_history[
    "sequence_end_day"
].astype(int)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Observed sequence count",
    f"{len(participant_history):,}"
)

c2.metric(
    "Earliest sequence day",
    f"{cycle_days.min()}"
)

c3.metric(
    "Latest sequence day",
    f"{cycle_days.max()}"
)

st.caption(
    "Cycle characteristics shown here are descriptive "
    "research observations and are not clinical cycle assessments."
)


# ============================================================
# 3. ARHI
# ============================================================

st.header(
    "3. AI-based Reproductive Health Index (ARHI)"
)

arhi = float(
    selected_row[
        "ARHI_research_monitoring_index"
    ]
)

band = str(
    selected_row[
        "ARHI_descriptive_band"
    ]
)

c1, c2 = st.columns(2)

c1.metric(
    "ARHI",
    f"{arhi:.1f}/100"
)

c2.metric(
    "Descriptive band",
    band
)

st.progress(
    min(
        max(
            arhi / 100,
            0.0
        ),
        1.0
    )
)

st.warning(
    """
    ARHI is a **provisional research monitoring index**.
    It is not a validated clinical health score and has no
    diagnostic, fertility, treatment or clinical-risk interpretation.
    """
)


# ============================================================
# ARHI COMPONENTS
# ============================================================

st.subheader(
    "ARHI Components"
)

component_cols = [
    (
        "Menstrual Forecast",
        "menstrual_forecast_component"
    ),
    (
        "Hormonal Monitoring",
        "hormonal_monitoring_component"
    ),
    (
        "Physiological Monitoring",
        "physiological_monitoring_component"
    ),
    (
        "Lifestyle / Wellness",
        "lifestyle_wellness_component"
    )
]

cols = st.columns(4)

for col, (
    label,
    column
) in zip(
    cols,
    component_cols
):

    value = float(
        selected_row[column]
    )

    col.metric(
        label,
        f"{value:.1f}"
    )


st.caption(
    "Only the menstrual-forecast component currently has an "
    "empirically derived sequence-level value. The other "
    "components use neutral reference values because validated "
    "clinical score transformations were not established."
)


# ============================================================
# 4. EXPLAINABLE AI
# ============================================================

st.header(
    "4. Explainable AI"
)

st.subheader(
    "Major model-reliance patterns"
)

st.write(
    """
    XAI results describe which inputs the validated multimodal
    model relied on most strongly. These are model-attribution
    results and should not be interpreted as causal or clinical
    relationships.
    """
)

xai_cols = st.columns(3)

xai_cols[0].metric(
    "Top modality",
    "Hormonal / Menstrual"
)

xai_cols[1].metric(
    "Second modality",
    "Sleep"
)

xai_cols[2].metric(
    "Third modality",
    "Cardiovascular HRV"
)

st.markdown(
    """
    **Top feature-level attributions**

    - Phase
    - Cramps
    - Headaches
    - Mood swing
    - Flow color
    - Indigestion
    - Bloating
    - Sore breasts
    - Stress
    - Flow volume
    """
)

st.info(
    "XAI identifies model reliance, not causation."
)


# ============================================================
# 5. PERSONALIZED RECOMMENDATION
# ============================================================

st.header(
    "5. Personalized Research Recommendation"
)

recommendation_category = str(
    selected_row[
        "recommendation_category"
    ]
)

recommendation_text = str(
    selected_row[
        "recommendation_text"
    ]
)

st.subheader(
    recommendation_category
)

st.write(
    recommendation_text
)

st.caption(
    "Recommendations are informational and non-diagnostic. "
    "Persistent or concerning symptoms should be discussed "
    "with a qualified healthcare professional."
)


# ============================================================
# 6. MODEL PERFORMANCE
# ============================================================

st.header(
    "6. Model Performance Context"
)

if not comparison_df.empty:

    learned = comparison_df[
        comparison_df[
            "model_type"
        ]
        .astype(str)
        .str.lower()
        == "learned"
    ].copy()

    if not learned.empty:

        learned = learned.sort_values(
            "learned_rank"
        )

        st.dataframe(
            learned[
                [
                    "model",
                    "balanced_accuracy",
                    "f1",
                    "roc_auc"
                ]
            ].rename(
                columns={
                    "model": "Model",
                    "balanced_accuracy": "Balanced Accuracy",
                    "f1": "F1",
                    "roc_auc": "ROC-AUC"
                }
            ),
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "The multimodal fusion model is the strongest learned "
            "model. The conventional phase-persistence baseline "
            "remains the strongest overall benchmark."
        )


# ============================================================
# 7. RESEARCH METHODOLOGY NOTE
# ============================================================

st.header(
    "Research Methodology Note"
)

st.markdown(
    """
    **Primary validated task:** 14-day menstrual-onset forecasting.

    **Best learned model:** Multimodal Fusion.

    **Overall benchmark:** Phase Persistence Baseline.

    **Evaluation design:** Participant-independent held-out test set.

    **XAI:** Modality occlusion and Gradient × Input attribution.

    **ARHI:** Provisional research monitoring index.

    **Clinical use:** Not supported.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "HormoCycleAI | Research prototype | "
    "Validated outputs from Steps 12–18"
)
