import streamlit as st
import requests
import json

# Set the title of the application
st.title("Employee Performance Predictor")

# ... (your existing input widgets and prediction logic) ...

department = st.selectbox("Department", 
                          ['HR', 'Finance', 'IT', 'Marketing', 
                           'Customer Support', 'Engineering', 
                           'Operations', 'Sales'])
age = st.number_input("Age", min_value=18, max_value=100)
gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
job_title = st.selectbox("Job Title", 
                          ['Manager', 'Specialist', 'Analyst', 
                           'Engineer', 'Developer', 'Technician', 
                           'Consultant'])
years_at_company = st.number_input("Years at Company", min_value=0)
education_level = st.selectbox("Education Level", 
                                 ['High School', "Bachelor's", 
                                  "Master's", 'PhD'])
monthly_salary = st.number_input("Monthly Salary In (USD)", min_value=0.0)
work_hours_per_week = st.number_input("Work Hours Per Week", min_value=0)
projects_handled = st.number_input("Projects Handled", min_value=0)
overtime_hours = st.number_input("Overtime Hours", min_value=0)
sick_days = st.number_input("Sick Days Taken", min_value=0)
remote_work_frequency = st.number_input("Remote Work Frequency (0-100)", min_value=0, max_value=100)
team_size = st.number_input("Team Size", min_value=1)
training_hours = st.number_input("Training Hours", min_value=0)
promotions = st.number_input("Promotions Received", min_value=0)
satisfaction_score = st.number_input("Employee Satisfaction Score (0-5)", min_value=0.0, max_value=5.0)

# Button to trigger the prediction
if st.button("Predict"):
    user_input = {
        "Department": department,
        "Age": age,
        "Gender": gender,
        "Job_Title": job_title,
        "Years_At_Company": years_at_company,
        "Education_Level": education_level,
        "Monthly_Salary": monthly_salary,
        "Work_Hours_Per_Week": work_hours_per_week,
        "Projects_Handled": projects_handled,
        "Overtime_Hours": overtime_hours,
        "Sick_Days": sick_days,
        "Remote_Work_Frequency": remote_work_frequency,
        "Team_Size": team_size,
        "Training_Hours": training_hours,
        "Promotions": promotions,
        "Employee_Satisfaction_Score": satisfaction_score,
    }

    # Call the FastAPI prediction endpoint
    try:
        #response = requests.post("https://employee-performance-predictor-br03.onrender.com", json=user_input)
        response = requests.post("http://localhost:8000/predict", json=user_input)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        result = response.json()
        if "Performance" in result:
            st.success(f"Predicted Performance: {result['Performance']}")
        elif "error" in result:
            st.error(f"Prediction failed: {result['error']}")
        else:
            st.error("Unexpected response format.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the prediction API. Make sure the FastAPI server is running at http://localhost:8000.")
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
    except json.JSONDecodeError:
        st.error("Failed to decode JSON response from the API.")

# Add GitHub and LinkedIn links in an expander
st.markdown("---") # Add a separator

with st.expander("Connect with me"):
    st.markdown("GitHub: [waqasahmad-developer](https://github.com/waqasahmad-developer)")
    st.markdown("LinkedIn: [waqasahmad-wa](https://www.linkedin.com/in/waqasahmad-wa/)")