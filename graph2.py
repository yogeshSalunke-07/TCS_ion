import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Specify the full paths to the model and label encoder
model_path = r'C:\Users\Lenovo\OneDrive\Desktop\yogesh TCS\Yogesh_tcs\model.pkl'
le_path = r'C:\Users\Lenovo\OneDrive\Desktop\yogesh TCS\Yogesh_tcs\le.pkl'

# Load the saved model and label encoder
model = joblib.load(model_path)
le = joblib.load(le_path)

# Load and preprocess the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    if 'Job_Title' not in data.columns or 'Current_Salary_in_Lakhs' not in data.columns:
        raise ValueError("CSV file must contain 'Job_Title' and 'Current_Salary_in_Lakhs' columns.")
    
    data['Job_Title'] = le.transform(data['Job_Title'])
    
    # Remove ' lakhs' and convert salary to float
    data['Current_Salary_in_Lakhs'] = data['Current_Salary_in_Lakhs'].str.replace(' lakhs', '').astype(float)
    
    X = data[['Age', 'Years_of_Experience', 'Job_Title']]
    y = data['Current_Salary_in_Lakhs']
    
    return X, y

# Evaluate the model
def evaluate_model(csv_file):
    X, y = load_data(csv_file)
    y_pred = model.predict(X)
    
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    
    print(f"R^2 score: {r2}")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    
    # Visualize predictions vs actual values
    plt.figure(figsize=(10, 6))
    plt.scatter(y, y_pred, alpha=0.3)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r', lw=2)
    plt.xlabel("Actual Salary in Lakhs")
    plt.ylabel("Predicted Salary in Lakhs")
    plt.title("Actual vs Predicted Salary")
    plt.show()

# Main function
if __name__ == "__main__":
    csv_file = r"C:\Users\Lenovo\OneDrive\Desktop\yogesh TCS\Yogesh_tcs\salary_data.csv"
    evaluate_model(csv_file)
