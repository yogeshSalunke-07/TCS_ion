import pandas as pd
import matplotlib.pyplot as plt

# Correct file location
file_location = r"C:\Users\rawoo\Documents\Yogesh_tcs\salary_data.csv"

# Read the CSV file
df = pd.read_csv(file_location)

# Convert 'Age' to numeric and handle errors
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Drop rows with NaN values in 'Age'
df = df.dropna(subset=['Age'])

# Plot the age distribution as a histogram with red color
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, edgecolor='black', color='red')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
