import requests, json
zip = '24060'
payload = {'zip':zip,'APPID':'a336a6c918103af9bd7045bf9304caa3','cnt':'15'}
r = requests.get('http://api.openweathermap.org/data/2.5/forecast?us', params=payload)

response = r.json()
r_json = json.dumps(response['city'])
r_load = json.loads(r_json)
r_coord = json.dumps(r_load['coord'])
r_coord_load = json.loads(r_coord)

# the longitude string
longitude = json.dumps(r_coord_load['lon'])

# the latitude string
latitude = json.dumps(r_coord_load['lat'])

r_json2 = json.dumps(response['list'])
r_load2 = json.loads(r_json2)
r_weather = json.dumps(r_load2[0])
r_clouds_load = json.loads(r_weather)
r_clouds = json.dumps(r_clouds_load['clouds'])
r_all_load = json.loads(r_clouds)

# the cloudiness percentage
r_all = json.dumps(r_all_load['all'])

print(response)
