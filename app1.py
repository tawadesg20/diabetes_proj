import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("diabetes_prediction.pkl")

st.title("Diabetes Prediction App")

# Collect user input for selected features
age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, value=25.0)
waist_circumference = st.number_input("Enter Waist Circumference", value=0.00)
fasting_blood_glucose = st.number_input("Enter Fasting Blood Glucose", min_value=50, max_value=200, value=100)
hba1c = st.number_input("Enter HbA1c Level", value=0.00)
blood_pressure_systolic = st.number_input("Enter Systolic Blood Pressure", value=0.00)
blood_pressure_diastolic = st.number_input("Enter Diastolic Blood Pressure", value=0.00)
cholesterol_total = st.number_input("Enter Total Cholesterol Level", value=0.00)
cholesterol_hdl = st.number_input("Enter HDL Cholesterol Level", value=0.00)
cholesterol_ldl = st.number_input("Enter LDL Cholesterol Level", value=0.00)
ggt = st.number_input("Enter GGT Level", value=0.00)
serum_urate = st.number_input("Enter Serum Urate Level", value=0.00)
physical_activity = st.number_input("Enter Physical Activity Level", value=0.00)
dietary_intake = st.number_input("Enter Dietary Intake Calories", value=0.00)
smoking_status = st.number_input("Enter Smoking Status", value=0.00)
family_history = st.number_input("Enter Family History of Diabetes", value=0.00)

# Convert input values into numpy array
features = np.array([age, bmi, waist_circumference, fasting_blood_glucose, hba1c,
                     blood_pressure_systolic, blood_pressure_diastolic, cholesterol_total, cholesterol_hdl,
                     cholesterol_ldl, ggt, serum_urate, physical_activity, dietary_intake,
                     smoking_status, family_history]).reshape(1, -1)

# Ensure prediction executes
if st.button("Predict Diabetes"):
    if features.shape[1] != model.n_features_in_:
        st.error(f"Feature mismatch! Model expects {model.n_features_in_} features, but got {features.shape[1]}.")
    else:
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.error("High risk of diabetes! Consult a doctor.")
        else:
            st.success("Low risk of diabetes. Keep maintaining a healthy lifestyle!")