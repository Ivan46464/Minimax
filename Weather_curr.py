import csv
import pandas as pd
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=43.2&lon=27.9&appid=063552b68d5f5d26401c400bf9f5580b")

if response.status_code == 200:
    data = response.json()
    if data:
        # Write Data to CSV
        with open('weather_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['lon', 'lat', 'weather_id', 'weather_main', 'weather_description', 'weather_icon',
                          'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity', 'visibility',
                          'wind_speed', 'wind_deg', 'wind_gust', 'rain_1h', 'clouds_all', 'dt', 'sys_type', 'sys_id',
                          'sys_country', 'sys_sunrise', 'sys_sunset', 'timezone', 'id', 'name', 'cod']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write header row

            # Write data row
            rain_1h = data.get('rain', {}).get('1h', '')  # Handle the case where 'rain' key is not present
            writer.writerow({
                'lon': data['coord']['lon'],
                'lat': data['coord']['lat'],
                'weather_id': data['weather'][0]['id'],
                'weather_main': data['weather'][0]['main'],
                'weather_description': data['weather'][0]['description'],
                'weather_icon': data['weather'][0]['icon'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'temp_min': data['main']['temp_min'],
                'temp_max': data['main']['temp_max'],
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'visibility': data.get('visibility', ''),
                'wind_speed': data['wind']['speed'],
                'wind_deg': data['wind']['deg'],
                'wind_gust': data['wind'].get('gust', ''),
                'rain_1h': rain_1h,
                'clouds_all': data['clouds']['all'],
                'dt': data['dt'],
                'sys_type': data['sys']['type'],
                'sys_id': data['sys']['id'],
                'sys_country': data['sys']['country'],
                'sys_sunrise': data['sys']['sunrise'],
                'sys_sunset': data['sys']['sunset'],
                'timezone': data['timezone'],
                'id': data['id'],
                'name': data['name'],
                'cod': data['cod']
            })
    else:
        print("No data records found in the response.")
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)

# Read CSV file using pandas
df = pd.read_csv("weather_data.csv")
print(df.head())
print(df.columns)