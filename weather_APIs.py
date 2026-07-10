import requests

api_key = "ce2527faa11d2b5771c03c737b2cb2b5" 

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print(response.status_code)
print(response.text)

data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("City not found!")