import json 

from urllib.request import urlopen 

obj = json.load(urlopen('http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,TEMP,RAIN&type=hr&sdate=2023-11-06&edate=2023-11-06&stime=12&etime=15')) 

print("Station ID: " + obj["stations"][0]["stationID"]) 

print("Parameters: " + ", ".join(obj["stations"][0]["params"])) 

print("\nData Table:") 

header = ["TIME"]+obj["stations"][0]["params"] 

print(" ".join(header)) 

for entry in obj["stations"][0]["data"]: 

    row = [entry["DATETIMEDATA"]] 

for param in obj["stations"][0]["params"]: 

    row.append(entry[param]) 

print(" ".join(map(str, row))) 