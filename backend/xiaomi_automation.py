import miio
from miio.airpurifier import AirPurifier, OperationMode


def establish_connection(xiaomi_type, ip, token):
    device = xiaomi_type(ip=f'{ip}',
                         token=f'{token}',
                         start_id=0,
                         debug=0,
                         lazy_discover=True)
    return device


def check_air_at_home_and_decide(air_outside):
    device = establish_connection(miio.airpurifier.AirPurifier,
                                  '192.168.0.206', 'e3aae83f4464e44bea3584363c6b2de6')

    if(air_outside >= 40):
        if device.status().aqi > 10:
            device.on()
        else:
            device.off()
    else:
        device.off()
