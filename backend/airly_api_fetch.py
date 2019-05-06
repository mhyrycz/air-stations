#pip3 install requests
#pip3 install geocoder

import requests
import json
from airly_credentials import headers

# auth

api_address = 'https://airapi.airly.eu/v2/'
 
headers = {
    'Accept': 'application/json',
    'apikey': 'yvK3KkJPex9PJYS3n2reZ1L2c7GUNhas',
}

params = (
    ('lat', '50.04951'),
    ('lng', '19.93734'),
    ('maxDistanceKM', '1'),
    ('maxResults', '3'),
)

def get_air_stations():

    stations_info = requests.get('{}installations/nearest'.format(api_address), headers=headers, params=params).content.decode("utf-8")

    stations = []

    for station in json.loads(stations_info):
        station_adress = station["address"]
        combined_address = station_adress["city"] + " " + station_adress["street"] + " " + station_adress["number"]
        stations.append(
            {
                "id": station["id"],
                "address": combined_address
            }
        )

    return stations


def get_air_params():

    stations = [
        {
            "address": "Kordeckiego 9",
            "id": 820
        },
        {
            "address": "Slowackiego 44",
            "id": 179
        },
        {
            "address": "Puszkarska 7j",
            "id": 1026
        },
    ]
   
    air_params = []

    for station in stations:
        measurements = requests.get('{}measurements/installation?installationId={}'.format(api_address, station["id"]), headers=headers).content
        aqi = json.loads(measurements.decode("utf-8"))["current"]["indexes"][0]
        aqi_value = aqi["value"]
        aqi_color = aqi["color"]
        otherParams = json.loads(measurements.decode("utf-8"))["current"]["values"] 
        address = station["address"]
        airPressure = next(param["value"] for param in otherParams if param["name"] == "PRESSURE") if otherParams else "unknown"
        temperature = next(param["value"] for param in otherParams if param["name"] == "TEMPERATURE") if otherParams else "unknown"
        humidity = next(param["value"] for param in otherParams if param["name"] == "HUMIDITY") if otherParams else "unknown"

        station_data = {
            "address": address, 
            "air": {
                "aqi": {
                            "value": aqi_value,
                            "color": aqi_color,
                        },
                "airPressure": airPressure,
                "temperature": temperature,
                "humidity": humidity,
            }
        }

        air_params.append(station_data)

    return air_params