import requests
import smtplib
import os

#API parameters
weather_api_endpoint = "http://api.weatherapi.com/v1/forecast.json"
API_KEY  = os.environ["W_API_KEY"]
ZIPCODE = "Laredo"
DAYS = 1

#constants
weather_condition_code_for_rain = 1153
will_rain = False
my_email = "angelggo2004@gmail.com"
password = os.environ["GMAIL_PASSWORD"]


parameters = {
    "key": API_KEY,
    "q": ZIPCODE,
    "days": DAYS,
}

#function helper
def send_email(msg):
    print("\nSending Umbrella Email!")
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="angelgomezortega@dusty.tamiu.edu",
            msg=(f"Subject:Weather Reminder!"
                 f"\n\n{msg}")
        )






response = requests.get(
    url=weather_api_endpoint,
    params=parameters,
)

response.raise_for_status()

weather_data = response.json()

for i in range(8, 19):
    condition_code = weather_data["forecast"]["forecastday"][0]["hour"][i]["condition"]["code"]
    if condition_code >= weather_condition_code_for_rain:
        will_rain = True



daily_chance_of_rain = weather_data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
  

if will_rain:
    message = f"Chance of rain is {daily_chance_of_rain}% today. Don't forget to take an umbrella!"
    send_email(message)

else:
    message = f"Chance of rain is {daily_chance_of_rain}% today. No need to take an umbrella!"
    send_email(message)
    









