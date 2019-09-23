api_address = 'https://airapi.airly.eu/v2/'

headers = {
    'Accept': 'application/json',
    'apikey': 'your_airly_api_key',
}

my_stations = [
    {
        "address": "street 1",
        "coordinates": {"lat": "20.876123", "lng": "11.123124"},
        "distance_from_station": "1"
    },
    {
        "address": "street 2",
        "coordinates": {"lat": "20.876123", "lng": "11.123124"},
        "distance_from_station": "2"
    },
    {
        "address": "street 3",
        "coordinates": {"lat": "20.876123", "lng": "11.123124"},
        "distance_from_station": "2"
    },
]
