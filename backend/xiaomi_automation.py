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
    current_hour = datetime.now().hour
    print("------------------------------")
    print("air_outside " + str(air_outside))
    print("current_hour " + str(current_hour))
    print("air_in_room " + str(device.status().aqi))
    if(air_outside >= 40):
        if current_hour in range(16, 23):
            if device.status().aqi > 30:
                print("1mode")
                device.on()
                device.set_mode(OperationMode.Favorite)
            elif device.status().aqi > 15:
                print("2mode")
                device.on()
                device.set_mode(OperationMode.Auto)
            else:
                device.off()
        if current_hour == 23 or current_hour in range(0, 8):
            print("3mode")
            device.set_mode(OperationMode.Silent)
        else:
            print("4mode")
            device.off()
    else:
        print("5mode")
        device.off()
    print("------------------------------")



check_air_at_home_and_decide(40)