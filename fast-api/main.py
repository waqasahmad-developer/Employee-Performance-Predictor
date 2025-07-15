from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal, Annotated
import pickle
import pandas as pd
import uvicorn

# Load the trained model
import joblib
model = joblib.load('model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define the input data model
class UserInput(BaseModel):
    Department: Literal['HR', 'Finance', 'IT', 'Marketing', 'Customer Support', 'Engineering', 'Operations', 'Sales'] = Field(..., description="Department of the person")
    Age: Annotated[int, Field(..., description="Age of the person")]
    Gender: Literal['Male', 'Female', 'Other'] = Field(..., description="Gender of the person")
    Job_Title: Literal['Manager', 'Specialist', 'Analyst', 'Engineer', 'Developer', 'Technician', 'Consultant'] = Field(..., description="Job title of the person")
    Years_At_Company: Annotated[int, Field(..., description="Years of experience at the company")]
    Education_Level: Literal['High School', "Bachelor's", "Master's", 'PhD'] = Field(..., description="Education level of the person")
    Monthly_Salary: Annotated[float, Field(..., description="Monthly salary")]
    Work_Hours_Per_Week: Annotated[int, Field(..., description="Work hours per week")]
    Projects_Handled: Annotated[int, Field(..., description="Projects handled")]
    Overtime_Hours: Annotated[int, Field(..., description="Overtime hours per week")]
    Sick_Days: Annotated[int, Field(..., description="Sick days taken")]
    Remote_Work_Frequency: Annotated[int, Field(..., description="Remote work frequency (0–100)")]
    Team_Size: Annotated[int, Field(..., description="Team size")]
    Training_Hours: Annotated[int, Field(..., description="Training hours")]
    Promotions: Annotated[int, Field(..., description="Promotions received")]
    Employee_Satisfaction_Score: Annotated[float, Field(..., description="Satisfaction score (0–5)")]

@app.post("/predict")
def predict(user_input: UserInput):
    # Convert the input to a DataFrame
    input_df = pd.DataFrame([user_input.dict()])

    try:
        # Make prediction
        Performance = model.predict(input_df)
        return {"Performance": round(float(Performance[0]), 3)}
    except Exception as e:
        return {"error": str(e)}
