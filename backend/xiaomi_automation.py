import miio
from miio.airpurifier import AirPurifier, OperationMode
from xiaomi_credentials import my_xiaomi
from datetime import datetime


def establish_connection():
    device = miio.airpurifier.AirPurifier(ip=my_xiaomi['ip'],
                                          token=my_xiaomi['token'],
                                          start_id=0,
                                          debug=0,
                                          lazy_discover=True)
    return device


def check_air_at_home_and_decide(air_outside):
    device = establish_connection()
    if(air_outside >= 40):
        if datetime.now().hour in range(16, 23):
            if device.status().aqi > 30:
                device.on()
                device.set_mode(OperationMode.Favorite)
            elif device.status().aqi > 15:
                device.on()
                device.set_mode(OperationMode.Auto)
            else:
                device.off()
        if datetime.now().hour in range(23, 7):
            device.set_mode(OperationMode.Silent)
        else:
            device.off()
    else:
        device.off()
