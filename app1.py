import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("diabetes_prediction.pkl")

st.title("Diabetes Prediction App")

# Update feature names based on dataset
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, value=25.0)
glucose = st.number_input("Enter Fasting Blood Glucose", min_value=50, max_value=200, value=100)
age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)

# Replace placeholders with real dataset features (update based on actual column names)
insulin = st.number_input("Enter Insulin Level")
blood_pressure = st.number_input("Enter Blood Pressure")
cholesterol = st.number_input("Enter Cholesterol Level")
skin_thickness = st.number_input("Enter Skin Thickness")
diabetes_pedigree = st.number_input("Enter Diabetes Pedigree Function")
pregnancies = st.number_input("Enter Number of Pregnancies")
physical_activity = st.number_input("Enter Physical Activity Score")
sleep_hours = st.number_input("Enter Average Sleep Hours")
smoking_status = st.number_input("Enter Smoking Status")
diet_score = st.number_input("Enter Diet Score")
family_history = st.number_input("Enter Family History of Diabetes")

# Collect input values in the correct order
features = np.array([bmi, glucose, age, insulin, blood_pressure, cholesterol, skin_thickness, 
                     diabetes_pedigree, pregnancies, physical_activity, sleep_hours, smoking_status, 
                     diet_score, family_history]).reshape(1, -1)

# Ensure prediction executes
if st.button("Predict Diabetes"):
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("High risk of diabetes! Consult a doctor.")
    else:
        st.success("Low risk of diabetes. Keep maintaining a healthy lifestyle!")
