import pandas as pd
import numpy as np
from faker import Faker

# Set the seed for reproducibility
np.random.seed(42)

# Initialize the Faker library for generating fake Indian names in English
fake = Faker('en_IN')

# Define the number of samples
num_samples = 200000

# Base salary and increment per year in INR
base_salary = 3.0  # in lakhs
increment_per_year = 0.15  # in lakhs per year of experience

# Define a list of job titles
job_titles = ['Software Engineer', 'Data Scientist', 'Product Manager', 'Business Analyst', 'Project Manager', 
               'HR Manager', 'Graphic Designer', 'Marketing Specialist', 'Sales Executive', 'Financial Analyst']

# Generate random data
ages = np.random.randint(25, 60, num_samples)  # Age between 25 and 60
years_of_experience = np.random.randint(1, 35, num_samples)  # Experience between 1 and 35 years
job_titles_assigned = np.random.choice(job_titles, num_samples)  # Randomly assign job titles

# Calculate current salaries in lakhs
salaries = base_salary + (increment_per_year * years_of_experience)

# Format the salaries to two decimal places
formatted_salaries = [f"{salary:.2f} lakhs" for salary in salaries]

# Generate Indian names in English
names = [fake.name() for _ in range(num_samples)]

# Create a DataFrame
hr_data = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'Years_of_Experience': years_of_experience,
    'Job_Title': job_titles_assigned,
    'Current_Salary_in_Lakhs': formatted_salaries
})

# Display the dataset
print(hr_data.head())

# Save the dataset to a new CSV file
hr_data.to_csv('salary_data.csv', index=False)
