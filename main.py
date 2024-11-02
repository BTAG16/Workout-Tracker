import requests
import os
from datetime import datetime

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

sheety_sheet = "workouts"
google_sheet = "cosmosWorkouts"
sheety_url = "https://api.sheety.co"
sheety_api = os.environ['SHEETY_API']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

INPUT = input("Tell me which exercises you did: ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "Content-Type" : "application/json"
}

AUTH = os.environ['SHEETY_AUTH']

auth_headers = {
    "Authorization" : AUTH,
}

exercise_params = {
    "query": INPUT,
     "gender":"male",
     "weight_kg":80.05,
     "height_cm":185.00,
     "age":21
}

date = datetime.now()
DATE = date.strftime("%d/%m/%Y")
TIME = date.strftime("%H:%M:%S")

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercises = response.json()

for exercise in exercises["exercises"]:
    EXERCISE = exercise["name"].title()
    DURATION = exercise["duration_min"]
    CALORIES = exercise["nf_calories"]

    sheety_params = {
        "workout" : {
            "date" : DATE,
            "time" : TIME,
            "exercise" : EXERCISE,
            "duration" : DURATION,
            "calories" : CALORIES,
        }
    }

    sheety_endpoint = f"{sheety_url}/{sheety_api}/{google_sheet}/{sheety_sheet}"
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=auth_headers)
    print(sheety_response.text)