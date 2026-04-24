import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
# THESE TWO LINES FIX THE ERRORS IN YOUR PHOTO:
from sklearn.metrics import mean_absolute_error, r2_score

# --- Page Configuration ---
st.set_page_config(page_title="OptiStay AI v2.3", layout="wide")

# --- 1. Realistic Data Generation ---
@st.cache_data
def load_data():
    np.random.seed(42)
    n = 2000 
    data = {
        'Age': np.random.randint(18, 90, n),
        'BMI': np.random.uniform(17, 35, n),
        'Surgery_Complexity': np.random.randint(1, 5, n),
        'Hemoglobin': np.random.uniform(10, 16, n),
        'Diabetes': np.random.choice([0, 1], n, p=[0.8, 0.2]),
        'Hypertension': np.random.choice([0, 1], n, p=[0.7, 0.3]),
        'Heart_Disease': np.random.choice([0, 1], n, p=[0.9, 0.1]),
        'CKD': np.random.choice([0, 1], n, p=[0.95, 0.05]),
        'Asthma': np.random.choice([0, 1], n, p=[0.85, 0.15]),
        'Smoker': np.random.choice([0, 1], n, p=[0.8, 0.2])
    }
    df = pd.DataFrame(data)
    
    df['LOS_Days'] = (
        2.0 +                               
        ((df['Age'] - 18) * 0.05) +         
        (df['Surgery_Complexity'] * 1.5) +  
        (np.maximum(0, df['BMI'] - 25) * 0.2) + 
        ((14 - df['Hemoglobin']) * 0.8) +   
        (df['Heart_Disease'] * 4.0) +       
        (df['CKD'] * 3.5) + 
        (df['Diabetes'] * 2.0) + 
        (df['Smoker'] * 1.5) +
        np.random.normal(0, 0.5, n)         
    ).clip(lower=1).round(1)
    
    # SPLIT DATA HERE
    X = df.drop('LOS_Days', axis=1)
    y = df['LOS_Days']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return df, X_train, X_test, y_train, y_test

# UNPACK ALL VARIABLES (This fixes the "Not Defined" errors)
df, X_train, X_test, y_train, y_test = load_data()
X = df.drop('LOS_Days', axis=1)
y = df['LOS_Days']

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)

# --- 2. Streamlit UI ---
st.title("🏥 OptiStay AI: Clinical Decision Support")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Patient Vitals")
    age = st.slider("Age", 18, 100, 45)
    bmi = st.slider("BMI", 15.0, 45.0, 24.0)
    surgery = st.selectbox("Surgery Complexity", [1, 2, 3, 4])
    hb = st.slider("Hemoglobin Level", 8.0, 18.0, 13.0)
    
    st.write("---")
    st.subheader("Comorbidities")
    diab = st.checkbox("Diabetes")
    hyp = st.checkbox("Hypertension")
    heart = st.checkbox("Heart Disease")
    ckd = st.checkbox("CKD")
    asthma = st.checkbox("Asthma")
    smoke = st.checkbox("Smoker")

with col2:
    # Prepare Data
    current_patient_data = pd.DataFrame([[
        age, bmi, surgery, hb, int(diab), int(hyp), int(heart), int(ckd), int(asthma), int(smoke)
    ]], columns=X.columns)
    
    prediction = model.predict(current_patient_data)[0]
    st.success(f"### Predicted Recovery: {prediction:.1f} Days")
    
    # Impact Chart
    st.subheader("Why this prediction?")
    avg_vals = X.mean()
    diffs = []
    for i, col in enumerate(X.columns):
        val = current_patient_data.iloc[0][col]
        contribution = (val - avg_vals[col]) * (model.feature_importances_[i] * 25)
        diffs.append(contribution)

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ['#ff4b4b' if x > 0 else '#00cc96' for x in diffs]
    ax.barh(X.columns, diffs, color=colors)
    ax.axvline(0, color='black', linewidth=0.8)
    st.pyplot(fig)

    # METRICS SECTION (This will now work!)
    st.divider()
    st.subheader("Model Accuracy (Validation)")
    y_pred = model.predict(X_test)
    m1, m2 = st.columns(2)
    m1.metric("Error Margin (MAE)", f"{mean_absolute_error(y_test, y_pred):.2f} Days")
    m2.metric("Model Confidence (R²)", f"{r2_score(y_test, y_pred):.2f}")