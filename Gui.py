import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import joblib

# Define salary weightages for each job title (example values)
job_title_weightage = {
    "Software Engineer": 1.1,
    "Data Scientist": 1.2,
    "Product Manager": 1.15,
    "HR Manager": 1.0,
    # Add more job titles and weightages as needed
}

# Load model and label encoder
def load_model_and_le(model_path='model.pkl', le_path='le.pkl'):
    global model, le, job_titles
    try:
        model = joblib.load(model_path)
        le = joblib.load(le_path)
        job_titles = le.classes_.tolist()  # Get job titles from the label encoder
    except FileNotFoundError as e:
        messagebox.showerror("File Error", f"File not found: {e}")
        root.quit()  # Exit the application if files are not found
    except Exception as e:
        messagebox.showerror("Error", str(e))
        root.quit()  # Exit the application if there is any other error

# Predict salary based on input
def predict_salary():
    try:
        age = int(age_entry.get())
        years_of_experience = int(experience_entry.get())
        current_job_title = current_job_title_combobox.get()
        new_job_title = new_job_title_combobox.get()

        # Ensure both job titles are valid
        if current_job_title not in job_titles or new_job_title not in job_titles:
            raise KeyError("Invalid job title. Please select valid job titles.")

        # Encode job titles
        current_job_title_encoded = le.transform([current_job_title])[0]
        new_job_title_encoded = le.transform([new_job_title])[0]

        # Get weightages
        current_job_weightage = job_title_weightage.get(current_job_title, 1.0)
        new_job_weightage = job_title_weightage.get(new_job_title, 1.0)

        # Predict salary based on current job title
        features = np.array([[age, years_of_experience, current_job_title_encoded]])
        base_salary = model.predict(features)[0]

        # Adjust salary based on new job weightage
        predicted_salary = base_salary * (new_job_weightage / current_job_weightage)

        result_label.config(text=f"Predicted Salary for {new_job_title}: {predicted_salary:.2f} lakhs")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for age and years of experience.")
    except KeyError:
        messagebox.showerror("Input Error", "Invalid job title. Please select valid job titles.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the GUI
root = tk.Tk()
root.title("HR Salary Predictor")

# Define the size of the window
window_width = 450
window_height = 300

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for the window to be centered
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the dimensions of the window and its position
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create and place widgets
tk.Label(root, text="Age:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Years of Experience:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
experience_entry = tk.Entry(root)
experience_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Current Job Title:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
current_job_title_combobox = ttk.Combobox(root, state="readonly")
current_job_title_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="New Job Title:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
new_job_title_combobox = ttk.Combobox(root, state="readonly")
new_job_title_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

predict_button = tk.Button(root, text="Predict Salary", command=predict_salary)
predict_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Load the trained model and label encoder
load_model_and_le()

# Populate the Comboboxes with job titles
selected_job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "HR Manager"]
current_job_title_combobox['values'] = selected_job_titles
new_job_title_combobox['values'] = selected_job_titles

root.mainloop()
