import astropy.coordinates as coord
from astropy.time import Time
import astropy.units as u
from .fusion_solar_py import client
from os import getenv

ps = client.FusionSolarClient(
        username=getenv("HUAWEI_USERNAME"),
        password=getenv("HUAWEI_PASSWORD"),
        huawei_subdomain="region03eu5")


def get():
    _stats = ps.get_power_status()
    stats = {
            'current_power_kw': _stats.current_power_kw,
            'total_power_today_kwh': 123,
            'total_power_kwh': 123,
            }
    time = Time('2023-10-04 10:00')
    time = Time.now()
    normalized_time = (time.datetime.time().hour * 60 + time.datetime.time().minute)/(60*24)-.25
    loc = coord.EarthLocation(lon=0 * u.deg,
                          lat=59.334591 * u.deg)

    altaz = coord.AltAz(location=loc, obstime=time)
    sun = coord.get_sun(time)

    return {
            'sun_x': normalized_time,
            'sun_y': sun.transform_to(altaz).alt.radian,
            'stats': stats,
            }
