# 🏥 OptiStay AI: Clinical Decision Support System

An AI-powered tool developed to predict hospital length of stay (LOS) with high precision using patient-specific clinical data.

## 🚀 Project Overview
This project was built for the **PSNA Hackathon**. It transitions from a simple "comorbidity count" to a specific **One-Hot Encoded** feature set, allowing the model to distinguish between different clinical risks (e.g., Heart Disease vs. Asthma).

## 🛠️ Features
- **Predictive Analytics:** Uses Random Forest Regression for accurate forecasting.
- **Explainable AI:** Dynamic "Local Impact" chart explains the *reasoning* behind each prediction.
- **Realistic Modeling:** Adjusted with a physiological baseline for healthy patients.

## 📊 Performance Metrics
- **Mean Absolute Error (MAE):** ~0.45 Days
- **R² Score:** ~0.94

## 🖥️ Tech Stack
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn
- **Data Handling:** Pandas & NumPy
- **Visuals:** Matplotlib
