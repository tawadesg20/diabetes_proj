from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load("diabetes_prediction.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get input JSON
        
        # Ensure correct number of features
        if 'features' not in data or len(data['features']) != 16:
            return jsonify({'error': 'Invalid input! Expected 16 features.'}), 400
        
        # Convert input to NumPy array
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        return jsonify({'prediction': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Send error response if something breaks

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode