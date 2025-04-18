import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("diabetes_prediction.pkl")

st.title("Diabetes Prediction App")

# Collect **all 16 feature inputs** from the user
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, value=25.0)
glucose = st.number_input("Enter Fasting Blood Glucose", min_value=50, max_value=200, value=100)
age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)

# Add more fields (fill in placeholders based on actual dataset)
feature_4 = st.number_input("Enter Feature 4")
feature_5 = st.number_input("Enter Feature 5")
feature_6 = st.number_input("Enter Feature 6")
feature_7 = st.number_input("Enter Feature 7")
feature_8 = st.number_input("Enter Feature 8")
feature_9 = st.number_input("Enter Feature 9")
feature_10 = st.number_input("Enter Feature 10")
feature_11 = st.number_input("Enter Feature 11")
feature_12 = st.number_input("Enter Feature 12")
feature_13 = st.number_input("Enter Feature 13")
feature_14 = st.number_input("Enter Feature 14")
feature_15 = st.number_input("Enter Feature 15")
feature_16 = st.number_input("Enter Feature 16")

# Store inputs in an array
features = np.array([bmi, glucose, age, feature_4, feature_5, feature_6, feature_7, 
                     feature_8, feature_9, feature_10, feature_11, feature_12, feature_13, 
                     feature_14, feature_15, feature_16]).reshape(1, -1)

# Predict button
if st.button("Predict Diabetes"):
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("High risk of diabetes! Consult a doctor.")
    else:
        st.success("Low risk of diabetes. Keep maintaining a healthy lifestyle!")