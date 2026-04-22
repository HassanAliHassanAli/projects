Sure! Here is a step-by-step guide to creating a production-ready Python application using FastAPI and Scikit-Learn for anomaly detection in financial transactions:

1. **Setup Environment:**

First, create an environment with all necessary dependencies installed:
```bash
pip install fastapi uvicorn sqlalchemy pandas scikit-learn numpy typing
```
2. **Import Dependencies:**
```python
from typing import List
import fastapi
from fastapi.encoders import jsonable_encoder
from sklearn.ensemble import IsolationForest
import joblib

app = fastapi.FastAPI()
```

3. **Define the Model:**

Load your trained model (Isolation Forest) into memory.
```python
model_path = 'path_to_your_trained_model'
trained_model = joblib.load(model_path)
```
4. **Create the REST API Endpoint:**
```python
@app.post('/predict_fraud')
async def predict_fraud(transaction_data: Dict[str, Any]) -> Dict[str, Any]:
    transaction_data_encoded = jsonable_encoder(transaction_data)  # Convert to JSON-serializable format
    
    # Simulate data preprocessing using pandas DataFrame
    df = pd.DataFrame.from_dict(transaction_data_encoded, orient='index').T
    preprocessed_data = preprocess_data(df)
    
    # Predict fraud probability
    anomaly_score = trained_model.predict(preprocessed_data)[0]
    
    return {'fraud_probability': anomaly_score}
```
5. **Define Data Preprocessing Function:**
```python
def preprocess_data(transaction_df):
    # Here you would implement data preprocessing logic, such as feature scaling or encoding categorical variables.
    # For example:
    preprocessed_df = (transaction_df - transaction_df.mean()) / transaction_df.std()
    return preprocessed_df
```
6. **Run the Application:**
```python
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

This code provides a basic structure for creating a production-ready application using FastAPI and Scikit-Learn to detect anomalies in financial transactions. Please replace `'path_to_your_trained_model'` with the actual path to your trained model file.

Remember to adjust the data preprocessing logic based on the specific features of your dataset and the requirements of your application.