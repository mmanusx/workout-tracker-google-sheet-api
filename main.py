# https://sheety.co/ api üzerinden googlesheet e veri kaydetip silmek için
# https://www.w3schools.com/python/ref_string_title.asp # .title()
# https://www.w3schools.com/python/python_datetime.asp # .strftime()

import requests
import datetime
import os
# .env variable
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

# Date Time Todays Dat
today = datetime.datetime.now()
today_formated = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

# Nutritionix
GENDER = "male"
WEIGHT_KG = 92
HEIGHT_CM = "176"
AGE = 31


nutritionix_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety
sheety_end_point = SHEET_ENDPOINT
TOKEN = "Basic bWFudXM6MTYxODE2MTgxNjE4TWhzLg=="

exercise_text = input("Tell me wich exercises you did: ")

#### Nutritionix App ######
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nut_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": WEIGHT_KG,
    "age": AGE
}

nut_response = requests.post(url=nutritionix_end_point, json=nut_params, headers=headers)
nut_response.raise_for_status()
print(nut_response.json())

###### Sheety App #######
# sheety ayarlarından authentication none seçili
sheety_headers = {
    "Authorization": TOKEN
}

sheety_params = {
    "workout":{
        "date": today_formated,
        "time": time,
        "exercise": nut_response.json()["exercises"][0]["user_input"],
        "duration": nut_response.json()["exercises"][0]["duration_min"] ,
        "calories": nut_response.json()["exercises"][0]["nf_calories"]
    }
}
sheety_response = requests.post(url=sheety_end_point, json=sheety_params, headers=sheety_headers )
sheety_response.raise_for_status()

### .env with os
# APP_ID = os.environ["APP_ID"]
# API_KEY = os.environ["API_KEY"]
### .env dosyasında zaten olan bizim tanımlamadığımız değişkenleri almak için
# APP_ID = os.environ.get("APP_ID")
# API_KEY = os.environ.get("API_KEY")