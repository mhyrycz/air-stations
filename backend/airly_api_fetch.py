import requests
import json
from airly_credentials import headers, api_address, my_stations
from xiaomi_automation import check_air_at_home_and_decide


def get_nearest_air_stations(lat, lng, distance):
    params = (
        ('lat', lat),
        ('lng', lng),
        ('maxDistanceKM', distance),
        ('maxResults', '3'),
    )
    stations_info = requests.get('{}installations/nearest'.format(
        api_address), headers=headers, params=params).content.decode("utf-8")

    stations = []

    for station in json.loads(stations_info):
        stations.append(station["id"])
    return stations


def get_measurements(id):
    measurements = requests.get('{}measurements/installation?installationId={}'.format(
        api_address, id), headers=headers).content
    measurements_decoded = json.loads(measurements.decode(
        "utf-8"))
    return measurements_decoded


def get_highest_aqi_station(lat, lng, distance):
    stations = get_nearest_air_stations(lat, lng, distance)
    aqis = []
    for station in stations:
        measurements = get_measurements(station)
        aqi = measurements["current"]["indexes"][0]["value"]
        if aqi is not None:
            aqis.append(aqi)
    index_of_stations_list = aqis.index(max(aqis))
    return stations[index_of_stations_list]


def important_stations():
    stations = []
    for station in my_stations:
        airly_station = {
            "address": station["address"],
            "id": get_highest_aqi_station(station["coordinates"]["lat"], station["coordinates"]["lng"], station["distance_from_station"])
        }
        stations.append(airly_station)
    return stations


def get_specific_param(air_param, otherParams):
    return next(param["value"] for param in otherParams if param["name"]
                == air_param) if otherParams else "unknown"


def get_air_params():
    air_params = []

    for station in important_stations():
        measurements = get_measurements(station["id"])
        aqi = measurements["current"]["indexes"][0]
        otherParams = measurements["current"]["values"]

        station_data = {
            "address": station["address"],
            "air": {
                "aqi": {
                    "value": aqi["value"],
                    "color": aqi["color"],
                },
                "airPressure": get_specific_param("PRESSURE", otherParams),
                "temperature": get_specific_param("TEMPERATURE", otherParams),
                "humidity": get_specific_param("HUMIDITY", otherParams),
            }
        }
        air_params.append(station_data)

    check_air_at_home_and_decide(air_params[0]["air"]["aqi"]["value"])

    return air_params
