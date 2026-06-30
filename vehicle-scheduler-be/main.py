from fastapi import FastAPI
import requests
from config import BASE_URL, TOKEN
app = FastAPI()
@app.get("/")
def home():
    return{
        "message": "Vehicle Maintainence"

    }
@app.get("/depots")
def get_depots():
    headers = {
        "Authorization" : f"Bearer {TOKEN}" 
    }

    response = requests.get(
        f"{BASE_URL}/depots",
        headers = headers
    )

    return response.json()