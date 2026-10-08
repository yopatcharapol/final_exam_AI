import json
from urllib.request import urlopen

sdate = '2023-11-06'
edate = '2023-11-06'
stime = 12
etime = 15
sensors = ['PM25','PM10','O3','CO','NO2','SO2','WS','WD','TEMP','RH','BP','RAIN']
sensortxt = ','.join(sensors)

domain = 'http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t'
url = f'{domain}&param={sensortxt}&type=hr&sdate={sdate}&edate={edate}&stime={stime}&etime={etime}'

obj = json.load(urlopen(url))

print(f'station ID: {obj['stations'][0]['stationID']:s}')

print('Time', end = ' | ')
for sensor in sensors:
    print(sensor, end=" | ")

alldata = obj['stations'][0]['data']

for data in alldata:

    print(data['DATETIMEDATA'], end = " | ")
    for sensor in sensors:
        print(data[sensor], end = " | ")
    print()
    