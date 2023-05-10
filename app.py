import requests

city = input("Enter City:")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={Enter your API key here}&units=metric'.format(city)

res = requests.get(url)
data = res.json()

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
tempc = data['main']['temp']
tempf =(tempc*9/5)+32

print('Temperature:',tempc,'°C')
print('Temperature:',tempf,'°F')
print('Wind:',wind)
print('Pressure: ',pressure)
print('Humidity: ',humidity)
print('Description:',description)