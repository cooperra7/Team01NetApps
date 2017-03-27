_author_ = "sarah.kharimah"

import requests
import datetime
import json
from pyorbital.orbital import Orbital

"""
Login and query TLE satellite data given its NORAD ID and date.
This function will print the JSON string query to the console. Comment out or delete the for loop and print statements to stop printing.

NOTE: THE DATABASE DOESN'T UPDATE IN REAL TIME. Asking for the current date's satellite information will usually result in an empty list.

:param: norad_id: (String) Intended satellite ID
:param: date: (datetime or String) Intended date "YYYY-MM-DD" to query against the Space-Track database.

:return: (JSON list) TLE data list.

:example:

    norad_id = '25544'
    # Use this to get current date
    # date = datetime.datetime.now().date()
    date = '2017-03-25'

    # tle_results = "[{'OBJECT_NUMBER': '25544', 'INTLDES': '98067A', 'TLE_LINE2': '2 25544 051.6418 093.4538 0007279 338.2943 091.9717 15.54260139048806', 'BSTAR': '5.0029e-05', 'REV_AT_EPOCH': '4880', 'MEAN_MOTION_DOT': '2.847e-05', 'EPOCH_MICROSECONDS': '486400', 'TLE_LINE0': '0 ISS (ZARYA)', 'ELEMENT_SET_NO': '999', 'NORAD_CAT_ID': '25544', 'EPOCH': '2017-03-25 21:37:26', 'INCLINATION': '51.6418', 'MEAN_ANOMALY': '91.9717', 'COMMENT': 'GENERATED VIA SPACETRACK.ORG API', 'OBJECT_ID': '1998-067A', 'OBJECT_TYPE': 'PAYLOAD', 'EPHEMERIS_TYPE': '0', 'PERIGEE': '399.369', 'FILE': '2165129', 'ARG_OF_PERICENTER': '338.2943', 'ECCENTRICITY': '0.0007279', 'CLASSIFICATION_TYPE': 'U', 'ORIGINATOR': 'JSPOC', 'APOGEE': '409.243', 'OBJECT_NAME': 'ISS (ZARYA)', 'MEAN_MOTION': '15.54260139', 'MEAN_MOTION_DDOT': '0', 'RA_OF_ASC_NODE': '93.4538', 'SEMIMAJOR_AXIS': '6782.441', 'TLE_LINE1': '1 25544U 98067A   17084.90100100 +.00002847 +00000-0 +50029-4 0  9992', 'PERIOD': '92.648'}]"
    tle_results = get_tle_results(norad_id=norad_id, date=date)

    ################ CONSOLE ###########################################################
    #
    # ------------------------- JSON # 0 -------------------------
    # 2017-03-25 21:37:26
    # 0 ISS (ZARYA)                                                           # TLE_LINE0
    # 1 25544U 98067A   17084.90100100 +.00002847 +00000-0 +50029-4 0  9992   # TLE_LINE1
    # 2 25544 051.6418 093.4538 0007279 338.2943 091.9717 15.54260139048806   # TLE_LINE2
    #
    ################ CONSOLE ###########################################################

    for index in range(len(tle_data_list)):
        tle_line0 = tle_results[index].get('TLE_LINE0')
        tle_line1 = tle_results[index].get('TLE_LINE1')
        tle_line2 = tle_results[index].get('TLE_LINE2')

"""


def get_tle_results(norad_id, date):

    username = 'sarahkh@vt.edu'
    password = 'murasakishikibu1900'
    base_url = 'https://www.space-track.org/'
    login_url = base_url + 'ajaxauth/login'

    d = datetime.datetime.strptime(str(date), "%Y-%m-%d")
    d1 = d + datetime.timedelta(days=1)
    dstr = d.strftime("%Y-%m-%d")
    d1str = d1.strftime("%Y-%m-%d")

    query = base_url + "/basicspacedata/query/class/tle/NORAD_CAT_ID/" + \
            norad_id + \
            "/EPOCH/" + dstr + "%2000:00:00--" + d1str + "%2000:00:00"

    data = {'identity': username, 'password': password, 'query': query}

    # Makes a POST REST call to space-track.org and return the result as a list of JSON
    try:
        resp = requests.post(login_url, data=data)
    except requests.exceptions.RequestException as err:
        print("POST RESTful call unsuccessful - unable to obtain TLE : " + err)

    tle_data_list = json.loads(resp.text)

    # Prints the TLE_LINE values to the console
    # Note: Some dates will generate more than one JSON TLE information
    # print(tle_data_list[index].get('EPOCH')) to get the specific datetime that the JSON belongs to
    for index in range(len(tle_data_list)):
        print("------------------------- TLE JSON # " + str(index) + " -------------------------")
        print(tle_data_list[index].get('EPOCH'))
        print(tle_data_list[index].get('TLE_LINE0'))
        print(tle_data_list[index].get('TLE_LINE1'))
        print(tle_data_list[index].get('TLE_LINE2'))

    return tle_data_list


def get_satellite_lat_lon(norad_id, tle_line1, tle_line2, date_time):

    username = 'sarahkh@vt.edu'
    password = 'murasakishikibu1900'
    base_url = 'https://www.space-track.org/'
    login_url = base_url + 'ajaxauth/login'

    query = base_url + "/basicspacedata/query/class/satcat/NORAD_CAT_ID/" + \
            norad_id + \
            "/orderby/NORAD_CAT_ID asc/metadata/false"

    data = {'identity': username, 'password': password, 'query': query}

    # Makes a POST REST call to space-track.org and return the result as a list of JSON
    try:
        resp = requests.post(login_url, data=data)
    except requests.exceptions.RequestException as err:
        print("POST RESTful call unsuccessful - unable to obtain LAT/LON : " + err)

    tip_data_list = json.loads(resp.text)

    satellite_name = str(tip_data_list[0].get('SATNAME'))
    orb = Orbital(satellite=satellite_name, line1=tle_line1, line2=tle_line2)

    # Gets longitude, latitude and altitude of the satellite:
    lon, lan, alt = orb.get_lonlatalt(date_time)

    print("------------------------- DATE & TIME IN UTC : " + str(date_time) + " -------------------------")
    print("LONGITUDE = " + str(lon))
    print("LATITUDE = " + str(lan))

    return lon, lan
