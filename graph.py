import pandas as pd
import matplotlib.pyplot as plt

# Correct file location
file_location = r'C:\Users\Lenovo\OneDrive\Desktop\yogesh TCS\Yogesh_tcs\salary_data.csv'

# Read the CSV file
df = pd.read_csv(file_location)

# Check the unique values in the 'Job_Title' column to understand its distribution
print(df['Job_Title'].value_counts())

# Plot the distribution of job titles
plt.figure(figsize=(12, 8))
df['Job_Title'].value_counts().plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Job Title Distribution')
plt.xlabel('Job Title')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()