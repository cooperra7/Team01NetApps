_author_ = "sarah.kharimah"

from spacetrack import spacetrackaccess
import datetime

norad_id = '25544'
date = '2017-03-25'
# Use this to get current time in UTC
current_utc_time = datetime.datetime.utcnow()

tle_result = spacetrackaccess.get_tle_results(norad_id=norad_id, date=date)

latest_tle_entry = (len(tle_result)) - 1


try:
    lon, lan = spacetrackaccess.get_satellite_lat_lon(norad_id,
                                                      tle_result[latest_tle_entry].get('TLE_LINE1'),
                                                      tle_result[latest_tle_entry].get('TLE_LINE2'),
                                                      current_utc_time)
except IndexError as err:
    print("Unable to obtain LAN/LON. TLE entries not found : " + str(err))
