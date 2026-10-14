
import streamlit as st
from datetime import date, timedelta

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HormoCycleAI",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff7fb 0%, #f8f4ff 50%, #f4f8ff 100%);
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #5b2c83;
    margin-bottom: 4px;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-bottom: 25px;
}

.hero {
    padding: 28px;
    border-radius: 22px;
    background: linear-gradient(135deg, #7b2cbf, #d63384);
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(100, 40, 130, 0.18);
}

.hero h1 {
    color: white;
    margin-bottom: 5px;
}

.hero p {
    color: #fdf3ff;
    font-size: 17px;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    margin: 12px 0;
    box-shadow: 0 5px 18px rgba(70, 30, 90, 0.08);
    border: 1px solid #eee5f5;
}

.score {
    font-size: 42px;
    font-weight: 800;
    color: #7b2cbf;
}

.big-percent {
    font-size: 42px;
    font-weight: 800;
    color: #d63384;
}

.section-title {
    color: #5b2c83;
    font-size: 25px;
    font-weight: 750;
    margin-top: 10px;
}

.reason {
    padding: 10px 14px;
    border-radius: 10px;
    background: #faf6ff;
    margin: 6px 0;
    color: #333;
}

.good {
    color: #16803c;
    font-weight: 650;
}

.warn {
    color: #b45309;
    font-weight: 650;
}

.info {
    color: #5b2c83;
    font-weight: 650;
}

.small-note {
    font-size: 13px;
    color: #777;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <h1>🌸 HormoCycleAI</h1>
    <p>
        Personalized menstrual and reproductive health insights
        designed to help you understand your patterns.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Enter a few simple details to generate your personalized AI-assisted insights.</div>',
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR INPUTS
# ============================================================

st.sidebar.markdown("## 🌸 Your Information")

age = st.sidebar.number_input(
    "Age",
    min_value=13,
    max_value=70,
    value=25
)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=220.0,
    value=165.0
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=30.0,
    max_value=200.0,
    value=60.0
)

last_period = st.sidebar.date_input(
    "First day of your last period",
    value=date.today() - timedelta(days=14)
)

cycle_length = st.sidebar.number_input(
    "Typical cycle length (days)",
    min_value=15,
    max_value=90,
    value=28
)

period_duration = st.sidebar.number_input(
    "Typical period duration (days)",
    min_value=1,
    max_value=15,
    value=5
)

regularity = st.sidebar.selectbox(
    "Cycle regularity",
    ["Very regular", "Mostly regular", "Sometimes irregular", "Often irregular"]
)

flow = st.sidebar.selectbox(
    "Current menstrual flow",
    ["None", "Light", "Moderate", "Heavy"]
)

cramps = st.sidebar.selectbox(
    "Cramps",
    ["None", "Mild", "Moderate", "Severe"]
)

headache = st.sidebar.selectbox(
    "Headache",
    ["None", "Mild", "Moderate", "Severe"]
)

food_cravings = st.sidebar.selectbox(
    "Food cravings",
    ["None", "Mild", "Moderate", "Strong"]
)

sleep_hours = st.sidebar.slider(
    "Average sleep (hours)",
    3.0,
    12.0,
    7.0,
    0.5
)

sleep_quality = st.sidebar.selectbox(
    "Sleep quality",
    ["Poor", "Fair", "Good", "Very good"]
)

activity = st.sidebar.selectbox(
    "Physical activity level",
    ["Low", "Light", "Moderate", "High"]
)

# ============================================================
# OPTIONAL ADVANCED INFORMATION
# ============================================================

with st.sidebar.expander("🔬 Optional advanced information"):

    hrv = st.number_input(
        "HRV",
        min_value=0.0,
        max_value=300.0,
        value=0.0
    )

    resting_hr = st.number_input(
        "Resting heart rate",
        min_value=20.0,
        max_value=150.0,
        value=60.0
    )

    respiratory = st.number_input(
        "Respiratory rate",
        min_value=5.0,
        max_value=40.0,
        value=16.0
    )

    estrogen = st.number_input(
        "Estrogen",
        min_value=0.0,
        max_value=1000.0,
        value=0.0
    )

    lh = st.number_input(
        "LH",
        min_value=0.0,
        max_value=300.0,
        value=0.0
    )

    pdg = st.number_input(
        "PDG",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

analyze = st.sidebar.button(
    "✨ Generate My AI Insights",
    use_container_width=True
)

# ============================================================
# CALCULATIONS
# ============================================================

if analyze:

    # --------------------------------------------------------
    # Cycle information
    # --------------------------------------------------------

    today = date.today()
    cycle_day = max(1, (today - last_period).days + 1)

    next_period = last_period + timedelta(days=int(cycle_length))

    days_to_period = (next_period - today).days

    if days_to_period < 0:
        days_to_period = 0

    # --------------------------------------------------------
    # Numeric mappings
    # --------------------------------------------------------

    regularity_score = {
        "Very regular": 100,
        "Mostly regular": 80,
        "Sometimes irregular": 55,
        "Often irregular": 30
    }[regularity]

    sleep_quality_score = {
        "Poor": 35,
        "Fair": 60,
        "Good": 82,
        "Very good": 95
    }[sleep_quality]

    activity_score = {
        "Low": 50,
        "Light": 70,
        "Moderate": 85,
        "High": 90
    }[activity]

    flow_score = {
        "None": 90,
        "Light": 85,
        "Moderate": 80,
        "Heavy": 55
    }[flow]

    symptom_scores = {
        "None": 100,
        "Mild": 80,
        "Moderate": 55,
        "Severe": 30
    }

    cramps_score = symptom_scores[cramps]
    headache_score = symptom_scores[headache]

    # --------------------------------------------------------
    # 1. HORMONAL PATTERN PREDICTION
    # --------------------------------------------------------
    #
    # Research-monitoring estimate based on user-provided
    # pattern indicators. This is NOT a clinical diagnosis.
    # --------------------------------------------------------

    hormonal_variation_score = 20

    if regularity == "Very regular":
        hormonal_variation_score += 5
    elif regularity == "Mostly regular":
        hormonal_variation_score += 15
    elif regularity == "Sometimes irregular":
        hormonal_variation_score += 30
    else:
        hormonal_variation_score += 45

    if flow == "Heavy":
        hormonal_variation_score += 12
    elif flow == "Moderate":
        hormonal_variation_score += 5

    if cramps in ["Moderate", "Severe"]:
        hormonal_variation_score += 7

    if headache in ["Moderate", "Severe"]:
        hormonal_variation_score += 5

    if sleep_hours < 6:
        hormonal_variation_score += 8
    elif sleep_hours >= 7:
        hormonal_variation_score -= 3

    if sleep_quality == "Poor":
        hormonal_variation_score += 7

    if activity == "Low":
        hormonal_variation_score += 3

    provided_hormones = sum([
        estrogen > 0,
        lh > 0,
        pdg > 0
    ])

    if provided_hormones > 0:
        hormonal_variation_score -= min(5, provided_hormones * 2)

    hormonal_probability = max(
        5,
        min(95, int(round(hormonal_variation_score)))
    )

    if hormonal_probability < 35:
        hormonal_label = "Lower estimated probability"
    elif hormonal_probability < 65:
        hormonal_label = "Moderate estimated probability"
    else:
        hormonal_label = "Higher estimated probability"

    # --------------------------------------------------------
    # 2. ARHI
    # --------------------------------------------------------

    sleep_component = min(20, max(
        0,
        20 - abs(8 - sleep_hours) * 4
    ))

    sleep_quality_component = sleep_quality_score * 0.15

    regularity_component = regularity_score * 0.20

    activity_component = activity_score * 0.15

    flow_component = flow_score * 0.10

    symptom_component = (
        cramps_score * 0.10 +
        headache_score * 0.05
    )

    # Remaining weighting to reach 100
    baseline_component = 5.0

    advanced_component = 0.0

    if hrv > 0:
        advanced_component = 2.0

    arhi = (
        sleep_component +
        sleep_quality_component +
        regularity_component +
        activity_component +
        flow_component +
        symptom_component +
        baseline_component +
        advanced_component
    )

    arhi = max(0, min(100, arhi))

    # Normalize slightly so the displayed score remains intuitive
    arhi = round(arhi, 1)

    if arhi >= 75:
        arhi_band = "Good pattern consistency"
    elif arhi >= 55:
        arhi_band = "Moderate pattern consistency"
    else:
        arhi_band = "More variation to monitor"

    # --------------------------------------------------------
    # ARHI CONTRIBUTION DISPLAY
    # --------------------------------------------------------

    arhi_factors = [
        ("💤 Sleep duration", round(sleep_component, 1), 20),
        ("😴 Sleep quality", round(sleep_quality_component, 1), 15),
        ("🩸 Cycle regularity", round(regularity_component, 1), 20),
        ("🏃 Physical activity", round(activity_component, 1), 15),
        ("🩸 Flow pattern", round(flow_component, 1), 10),
        ("🤕 Reported symptoms", round(symptom_component, 1), 15),
        ("📊 Pattern consistency", round(baseline_component, 1), 5)
    ]

    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    explanations = []

    if regularity in ["Sometimes irregular", "Often irregular"]:
        explanations.append(
            "Your cycle regularity contributed to a lower consistency score."
        )
    else:
        explanations.append(
            "Your cycle regularity is supporting your overall pattern consistency."
        )

    if sleep_hours < 7:
        explanations.append(
            "Your reported sleep duration is contributing some variation."
        )
    else:
        explanations.append(
            "Your reported sleep duration is supporting your overall pattern."
        )

    if sleep_quality in ["Poor", "Fair"]:
        explanations.append(
            "Sleep quality is contributing some variation to the monitoring score."
        )

    if cramps in ["Moderate", "Severe"]:
        explanations.append(
            "Reported cramps contributed to the current pattern estimate."
        )

    if headache in ["Moderate", "Severe"]:
        explanations.append(
            "Reported headaches contributed to the current pattern estimate."
        )

    if activity in ["Moderate", "High"]:
        explanations.append(
            "Your physical activity level is supporting the monitoring score."
        )

    # --------------------------------------------------------
    # RECOMMENDATION
    # --------------------------------------------------------

    recommendations = []

    if sleep_hours < 7:
        recommendations.append(
            "Try to maintain a consistent sleep routine where possible."
        )

    if regularity in ["Sometimes irregular", "Often irregular"]:
        recommendations.append(
            "Continue tracking cycle dates so you can understand your personal pattern over time."
        )

    if cramps in ["Moderate", "Severe"] or headache in ["Moderate", "Severe"]:
        recommendations.append(
            "Keep track of symptoms and how they change across your cycle."
        )

    if activity in ["Low", "Light"]:
        recommendations.append(
            "Regular comfortable physical activity may support general wellbeing."
        )

    if not recommendations:
        recommendations.append(
            "Continue tracking your cycle and maintaining your current healthy routines."
        )

    # ========================================================
    # DISPLAY
    # ========================================================

    st.markdown(
        '<div class="section-title">🧬 Hormonal Pattern Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">
            <div class="big-percent">{hormonal_probability}%</div>
            <h3>{hormonal_label}</h3>
            <p>
                Estimated probability of a future hormonal-irregularity pattern
                based on the information you provided.
            </p>
            <p class="small-note">
                Research-monitoring estimate — not a medical diagnosis.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">🩸 Cycle Forecast</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Current cycle day", cycle_day)

    with col2:
        st.metric("Estimated next period", next_period.strftime("%d %b %Y"))

    with col3:
        st.metric("Estimated days remaining", days_to_period)

    st.markdown(
        """
        <div class="card">
        This forecast uses your reported typical cycle length and the
        first day of your last period.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # ARHI
    # ========================================================

    st.markdown(
        '<div class="section-title">💗 ARHI — AI-based Reproductive Health Index</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">
            <div class="score">{arhi} / 100</div>
            <h3>{arhi_band}</h3>
            <p>
                Your ARHI reflects consistency in the personal patterns
                you entered today.
            </p>
            <p class="small-note">
                This is a research-monitoring index, not a clinical health score.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # NEW: WHY ARHI SCORE?
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">🔎 Why is my ARHI this score?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
        The score is built from the patterns you entered. Each factor
        contributes to the overall monitoring index.
        </div>
        """,
        unsafe_allow_html=True
    )

    for name, contribution, maximum in arhi_factors:

        percentage = int(round(
            (contribution / maximum) * 100
        )) if maximum > 0 else 0

        if percentage >= 75:
            label = "supporting your score"
            css_class = "good"
        elif percentage >= 50:
            label = "moderately supporting your score"
            css_class = "info"
        else:
            label = "contributing more variation"
            css_class = "warn"

        st.markdown(
            f"""
            <div class="reason">
                <strong>{name}</strong><br>
                {contribution:.1f} / {maximum} points —
                <span class="{css_class}">{label}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="card">
            <strong>Overall explanation</strong>
            <p>
                Your ARHI of <strong>{arhi}/100</strong> reflects a combination
                of sleep, cycle regularity, activity, flow and reported symptoms.
                Higher contributions indicate greater consistency with the
                research-monitoring pattern used by this dashboard.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # EXPLANATION
    # ========================================================

    st.markdown(
        '<div class="section-title">🔍 Explanation</div>',
        unsafe_allow_html=True
    )

    for text in explanations:
        st.markdown(
            f'<div class="reason">• {text}</div>',
            unsafe_allow_html=True
        )

    # ========================================================
    # RECOMMENDATION
    # ========================================================

    st.markdown(
        '<div class="section-title">💡 Personalized Recommendation</div>',
        unsafe_allow_html=True
    )

    for rec in recommendations:
        st.markdown(
            f'<div class="reason">🌸 {rec}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="card">
        <strong>Important:</strong>
        These insights are intended for personal pattern monitoring and
        educational purposes. Persistent, severe or concerning symptoms
        should be discussed with a qualified healthcare professional.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.info(
        "👈 Enter your information and click "
        "**✨ Generate My AI Insights** to see your personalized results."
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#777;font-size:13px;">
        🌸 HormoCycleAI — Personalized menstrual & reproductive health insights
    </div>
    """,
    unsafe_allow_html=True
)
