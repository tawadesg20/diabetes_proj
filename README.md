# 🩺 **Diabetes Prediction using Machine Learning** 🚀  
### **📢 About the Project**  
This project predicts diabetes risk using **machine learning models** trained on health-related data. It includes:  
✔**Flask API** to handle predictions via HTTP requests.  
✔ **Streamlit Web App** for an interactive user experience.  


## **🔹 Features**  
✔ **Data Preprocessing** (handling missing values, scaling, feature selection).  
✔ **Machine Learning Models** (Random Forest, Logistic Regression, XGBoost).  
✔ **Deployment with Flask (API) & Streamlit (UI).**  

## **🚀 Flask API Implementation**  

### **1️⃣ Setup & Installation**  
Clone the repository:
```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### **2️⃣ Run Flask Server**
Start the Flask API:
```bash
python app.py
```

### **3️⃣ Test API with Sample Input**
Use `curl` or Postman to send a request:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2, ..., 2.4]}'
```
✔️ **Returns `0` (No Diabetes) or `1` (Diabetes)** based on model prediction.

## **🖥️ Streamlit Web App Implementation**  

### **1️⃣ Setup & Installation**  
Install required dependencies:
```bash
pip install -r requirements.txt
```

### **2️⃣ Run Streamlit Web App**  
```bash
streamlit run app1.py
```
✔️ This will open an **interactive web page** where users can enter health details and receive predictions.

