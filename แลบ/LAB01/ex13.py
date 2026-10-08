import json
from urllib.request import urlopen 
  
obj = json.load(urlopen('http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?stationID=70t'))

print("Station " + obj['stationID'])
print("Name %s (%s)" % (obj['nameTH'], obj['nameEN']))
print("Name %(nameTH)s (%(nameEN)s)" % obj)
print(f"Name {obj['nameTH']} ({obj['nameEN']})")
print(f"Address {obj['areaTH']}({obj['areaEN']})")
print(f"Latitude Longtitude ({obj['lat']},{obj['long']})")

for k,v in obj['AQILast'].items():
    print(k, v)