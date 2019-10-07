import requests
import json
from airly_credentials import headers, api_address, my_locations
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
    print("dupa")
    measurements = requests.get('{}measurements/installation?installationId={}'.format(
        api_address, id), headers=headers).content
    measurements_decoded = json.loads(measurements.decode(
        "utf-8"))
    return measurements_decoded


def get_highest_aqi_station(lat, lng, distance):
    nearests = get_nearest_air_stations(lat, lng, distance)
    active_stations = []
    for station in nearests:
        measurements = get_measurements(station)
        aqi = measurements["current"]["indexes"][0]
        if aqi["value"] is not None:
            active_stations.append({
                "aqi": aqi,
                "otherParams": measurements["current"]["values"]
            })
    most_polluted = max(
        [station["aqi"]["value"] for station in active_stations])
    return [station for station in active_stations if station["aqi"]["value"] == most_polluted][0]


def crucial_stations():
    stations = []
    for location in my_locations:
        the_most_polluted_station = {
            "address": location["address"],
            "airly_measurements": get_highest_aqi_station(
                location["coordinates"]["lat"], location["coordinates"]["lng"], location["distance_from_station"])
        }
        stations.append(the_most_polluted_station)
    return stations


def get_specific_param(air_param, otherParams):
    return next(param["value"] for param in otherParams if param["name"]
                == air_param) if otherParams else "unknown"


def get_structured_for_api(station):
    aqi = station["airly_measurements"]["aqi"]
    other_params = station["airly_measurements"]["otherParams"]
    return {
        "address": station["address"],
        "air": {
            "aqi": {
                "value": aqi["value"],
                "color": aqi["color"],
            },
            "airPressure": get_specific_param("PRESSURE", other_params),
            "temperature": get_specific_param("TEMPERATURE", other_params),
            "humidity": get_specific_param("HUMIDITY", other_params),
        }
    }


def get_air_params():
    air_near_my_locations = []
    for station in crucial_stations():
        air_near_my_locations.append(get_structured_for_api(station))
    check_air_at_home_and_decide(
        air_near_my_locations[0]["air"]["aqi"]["value"])
    return air_near_my_locations
