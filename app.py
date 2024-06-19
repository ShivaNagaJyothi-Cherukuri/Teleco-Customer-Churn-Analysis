from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.sav', 'rb'))

# Define the preprocessing function
def preprocess_input(data):
    # Convert input data to a DataFrame
    df = pd.DataFrame([data])

    # Drop unnecessary columns
    df.drop(['customerID'], axis=1, inplace=True)

    # Map categorical variables to binary
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
    df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
    df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})
    df['MultipleLines'] = df['MultipleLines'].map({'Yes': 1, 'No': 0})
    df['OnlineSecurity'] = df['OnlineSecurity'].map({'Yes': 1, 'No': 0})
    df['OnlineBackup'] = df['OnlineBackup'].map({'Yes': 1, 'No': 0})
    df['DeviceProtection'] = df['DeviceProtection'].map({'Yes': 1, 'No': 0})
    df['TechSupport'] = df['TechSupport'].map({'Yes': 1, 'No': 0})
    df['StreamingTV'] = df['StreamingTV'].map({'Yes': 1, 'No': 0})
    df['StreamingMovies'] = df['StreamingMovies'].map({'Yes': 1, 'No': 0})
    df['PaperlessBilling'] = df['PaperlessBilling'].map({'Yes': 1, 'No': 0})

    # Bin tenure into groups
    bins = [0, 12, 24, 36, 48, 60, 72]
    labels = ['1 - 12', '13 - 24', '25 - 36', '37 - 48', '49 - 60', '61 - 72']
    df['tenure_group'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=False)
    df.drop(['tenure'], axis=1, inplace=True)

    # Create dummy variables for remaining categorical features
    categorical_features = ['InternetService', 'Contract', 'PaymentMethod', 'tenure_group']
    df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
    
    # Ensure the DataFrame has all the columns the model expects, filling missing columns with 0
    expected_columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                        'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                        'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
                        'InternetService_DSL', 'InternetService_Fiber optic',
                        'InternetService_No', 'Contract_Month-to-month', 'Contract_One year',
                        'Contract_Two year', 'PaymentMethod_Bank transfer (automatic)',
                        'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 
                        'PaymentMethod_Mailed check', 'tenure_group_1 - 12', 'tenure_group_13 - 24',
                        'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 
                        'tenure_group_61 - 72']
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    # Ensure the column order matches the model input
    df = df[expected_columns]
    
    return df

@app.route('/')
def index():
    return render_template('index.html', show_result=False, prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    # Extracting inputs from the form
    form_data = {
        'customerID': request.form['customerID'],
        'gender': request.form['gender'],
        'SeniorCitizen': int(request.form['SeniorCitizen']),
        'Partner': request.form['Partner'],
        'Dependents': request.form['Dependents'],
        'tenure': int(request.form['tenure']),
        'PhoneService': request.form['PhoneService'],
        'MultipleLines': request.form['MultipleLines'],
        'InternetService': request.form['InternetService'],
        'OnlineSecurity': request.form['OnlineSecurity'],
        'OnlineBackup': request.form['OnlineBackup'],
        'DeviceProtection': request.form['DeviceProtection'],
        'TechSupport': request.form['TechSupport'],
        'StreamingTV': request.form['StreamingTV'],
        'StreamingMovies': request.form['StreamingMovies'],
        'Contract': request.form['Contract'],
        'PaperlessBilling': request.form['PaperlessBilling'],
        'PaymentMethod': request.form['PaymentMethod'],
        'MonthlyCharges': float(request.form['MonthlyCharges']),
        'TotalCharges': float(request.form['TotalCharges'])
    }

    # Preprocess the input data
    processed_data = preprocess_input(form_data)

    # Convert to numpy array for model prediction
    input_data = np.array(processed_data)

    # Make prediction
    prediction = model.predict(input_data)

    # Determine prediction message
    if prediction[0] == 1:
        prediction_text = 'Customer is likely to churn.'
    else:
        prediction_text = 'Customer is not likely to churn.'

    # Render the result
    return render_template('index.html', show_result=True, prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
