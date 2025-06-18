from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from fastapi.middleware.cors import CORSMiddleware  # For allowing frontend access

app = FastAPI()

# Enable CORS so frontend can make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend domain here
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model pipeline
with open("LinearRegressionModel.pkl", "rb") as f:  # Make sure your model file is here
    pipe = pickle.load(f)

# Define the input schema for the API
class CarDetails(BaseModel):
    name: str
    company: str
    year: int
    kms_driven: int
    fuel_type: str

# Create a route to handle predictions
@app.post("/predict")
def predict(car: CarDetails):
    try:
        # Log input for debugging
        print("Received input:", car)

        # Convert input to pandas DataFrame
        car_df = pd.DataFrame([[car.name, car.company, car.year, car.kms_driven, car.fuel_type]],
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
        print("Converted DataFrame:", car_df)

        # Make the prediction using your pipeline
        prediction = pipe.predict(car_df)
        print("Prediction result:", prediction)

        # Return the prediction result
        return {"prediction": prediction[0]}
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": str(e)}
