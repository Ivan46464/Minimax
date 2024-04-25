import csv
import pandas as pd
import requests

response = requests.get("http://api.openweathermap.org/data/2.5/air_pollution/history?lat=43.2&lon=27.9&start=1063801161&end=1680116269&appid=063552b68d5f5d26401c400bf9f5580b")

if response.status_code == 200:
    data = response.json()
    if data:
        # Extract the coordinate values
        coord = data.get('coord', {})  # Get coord dictionary, default to empty dict if not present
        coord_lon = coord.get('lon', '')  # Get lon value, default to empty string if not present
        coord_lat = coord.get('lat', '')  # Get lat value, default to empty string if not present

        # Extract the list of data points
        data_list = data.get('list', [])

        # Write Data to CSV
        with open('output.csv', 'w', newline='') as csvfile:
            fieldnames = ['coord_lon', 'coord_lat', 'dt', 'aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write header row

            # Write data rows
            for item in data_list:
                writer.writerow({
                    'coord_lon': coord_lon,
                    'coord_lat': coord_lat,
                    'dt': item['dt'],
                    'aqi': item['main']['aqi'],
                    'co': item['components']['co'],
                    'no': item['components']['no'],
                    'no2': item['components']['no2'],
                    'o3': item['components']['o3'],
                    'so2': item['components']['so2'],
                    'pm2_5': item['components']['pm2_5'],
                    'pm10': item['components']['pm10'],
                    'nh3': item['components']['nh3']
                })

        # Read CSV file using pandas
        df = pd.read_csv("output.csv")
        print(df.head())
        print(df.columns)
        print(df.info())
        print(df.describe())
        print(df["aqi"].unique())
    else:
        print("No data records found in the response.")
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)
