import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib  # For saving and loading models

# Load and preprocess data
def load_data(file_path):
    data = pd.read_csv(file_path)
    if 'Job_Title' not in data.columns or 'Current_Salary_in_Lakhs' not in data.columns:
        raise ValueError("CSV file must contain 'Job_Title' and 'Current_Salary_in_Lakhs' columns.")
    
    le = LabelEncoder()
    data['Job_Title'] = le.fit_transform(data['Job_Title'])
    
    # Remove ' lakhs' and convert salary to float
    data['Current_Salary_in_Lakhs'] = data['Current_Salary_in_Lakhs'].str.replace(' lakhs', '').astype(float)
    
    X = data[['Age', 'Years_of_Experience', 'Job_Title']]
    y = data['Current_Salary_in_Lakhs']
    
    return X, y, le

# Train the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Save the model and label encoder
def save_model_and_le(model, le, model_path='model.pkl', le_path='le.pkl'):
    joblib.dump(model, model_path)
    joblib.dump(le, le_path)

# Main function
def main(csv_file):
    X, y, le = load_data(csv_file)
    model = train_model(X, y)
    save_model_and_le(model, le)
    print("Model and label encoder saved successfully!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python train.py <path_to_csv>")
    else:
        main(sys.argv[1])
