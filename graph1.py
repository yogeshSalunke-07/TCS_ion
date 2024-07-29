import pandas as pd
import matplotlib.pyplot as plt

# Correct file location
file_location = r'C:\Users\Lenovo\OneDrive\Desktop\yogesh TCS\Yogesh_tcs\salary_data.csv'

# Read the CSV file
df = pd.read_csv(file_location)

# Get the value counts for 'Current_Salary_in_Lakhs'
salary_counts = df['Current_Salary_in_Lakhs'].value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(salary_counts, labels=salary_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral'], startangle=140, wedgeprops=dict(edgecolor='black'))
plt.title('Current Salary Distribution (in Lakhs)')
plt.show()