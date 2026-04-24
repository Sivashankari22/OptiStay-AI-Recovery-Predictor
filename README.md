# 🏥 OptiStay AI: Clinical Decision Support System

OptiStay AI is a machine learning-driven platform designed to optimize hospital bed management by predicting patient Length of Stay (LOS). By transitioning from reactive scheduling to predictive discharge planning, the system helps hospitals reduce ER wait times and avoid delayed surgeries.

## 🎯 Project Objectives
- **Predictive Discharge Planning:** Utilize machine learning pipelines to provide precise LOS estimates from raw clinical inputs.
- **Operational Efficiency:** Mitigate "bed blocking" to reduce hospital operational expenses and improve patient throughput.
- **Explainable AI (XAI):** Surface the reasoning behind predictions (e.g., identifying low hemoglobin or specific comorbidities as delay factors) to build clinical trust.
- **Risk Identification:** Automatically flag "High-Risk Recovery" patients who may require early intervention or additional clinical attention.

## 🛠️ How It Works: The Pipeline

The system processes data through a structured four-stage pipeline:
1. **Data Collection:** Gathering patient profiles and clinical vitals including Age, BMI, and Hemoglobin levels.
2. **Feature Engineering:** Processing specific clinical variables and comorbidities (Diabetes, Hypertension, Heart Disease, etc.) using One-Hot Encoding.
3. **Model Training:** Utilizing **Random Forest Regressors** to capture complex, non-linear recovery patterns that linear models might miss.
4. **LOS Prediction:** Generating actionable discharge forecasts to enable proactive bed management.

## 🧪 Algorithms & Performance
- **Core Model:** Random Forest Regressor for high-precision forecasting in complex clinical cases.
- **Baseline:** Multiple Linear Regression used to establish clear relationships between features.
- **Key Metrics:**
    - **Mean Absolute Error (MAE):** Measures average prediction error. Target: < 1.5 days for clinical actionability.
    - **R² Score:** Quantifies the variance explained by clinical input features.
    - **RMSE:** Penalizes large errors to ensure high-risk stays are not underestimated.

## 📈 Social & Economic Impact
- **Clinical Benefit:** Improved patient satisfaction through proactive care and better discharge communication.
- **Economic Benefit:** Estimated 5–10% improvement in bed turnover, saving hospitals significantly in annual operational costs.

## 📖 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the app: `streamlit run app.py`
