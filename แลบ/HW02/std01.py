import json
from urllib.request import urlopen

obj = json.load(
    urlopen('http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16'))

print("Station : " + obj['stations'][0]["stationID"])
#อันนี้ code จะไม่สวย เลยเอามันมาทำมาก่อนเลย
print("*" * 50)
print("\nข้อมูลสภาพอากาศย้อนหลัง ตั้งแต่ 2023-10-01 ถึง 2023-11-06\n")
print("*" * 50)

while True:
    year1 = input("\nป้อนวันที่ต้องการเริ่มต้น(YY-MM-DD): ")
    print("-" * 30)
    year2 = input("\nป้อนวันที่ต้องการสิ้นสุด(YY-MM-DD): ")
    print("-" * 30)
    time1 = input("\nป้อนเวลาที่ต้องการเริ่ม(HH:MM:SS): ")
    print("-" * 30)
    time2 = input("\nป้อนเวลาที่ต้องการสิ้นสุด(HH:MM:SS): ")
    print("-" * 30)

    #ส่วนต่อไปนี้ใช้ chatGPT ช่วยเพื่อให้โค้ดออกมามีคุณภาพ
    # ตรวจสอบข้อมูลใน year1 และ year2
    if (
        not all(c.isdigit() or c == '-' for c in year1) or
        not all(c.isdigit() or c == '-' for c in year2)
    ):
        print("\033[91mข้อมูลบางส่วนไม่ถูกต้อง(วันที่) กรุณากรอกใหม่\033[0m\n")
        continue  # ถ้าข้อมูลไม่ถูกต้อง ให้วนไปให้ผู้ใช้กรอกใหม่

    # ตรวจสอบข้อมูลใน time1 และ time2
    if (
        not all(c.isdigit() or c == ':' for c in time1) or
        not all(c.isdigit() or c == ':' for c in time2)
    ):
        print("\033[91mข้อมูลบางส่วนไม่ถูกต้อง(เวลา) กรุณากรอกใหม่\033[0m\n")
        continue  # ถ้าข้อมูลไม่ถูกต้อง ให้วนไปห้ผู้ใช้กรอกใหม่

    # ตรวจสอบข้อมูลในฐานข้อมูล
    if any(
        data_point['DATETIMEDATA'].startswith(year1) or
        data_point['DATETIMEDATA'].startswith(year2)
        for data_point in obj['stations'][0]['data']
    ):
        break  # ถ้าข้อมูลถูกต้องและมีในฐานข้อมูล ให้ออกจากลูป
    else:
        print("\033[91mข้อมูลที่ระบุไม่มีในฐานข้อมูล กรุณากรอกใหม่\033[0m\n")

# ไปต่อเลยจ้า



params = [
    "PM25",
    "PM10",
    "O3",
    "CO",
    "NO2",
    "SO2",
    "WS",
    "WD",
    "TEMP",
    "RH",
    "BP",
    "RAIN"
]
#สร้าง list มาเก็บ params จะได้ดึงมาใช้ง่ายๆ

print("\nค่าสภาพอากาศที่สามารถดูได้ : " , params)
#ง่ายมั้ยล่ะ

selected_params = [] #ชื่อของ rarams ที่ถูกเลือกจะถูกเพิ่มเข้าไปตรงนี้




while True:
    param = input(f"\nป้อนค่าสภาพอากาศที่ต้องการ (พิมพ์ all เพื่อเลือกทั้งหมดทันที หรือ พิมพ์ done เมื่อเพิ่มค่าที่ต้องการครบแล้ว):\n ")
    if param.lower() == 'done':
        break
    elif param.lower() == 'all':
        selected_params = params.copy()
        print("\nเลือกค่าทั้งหมดแล้ว.\n")
        break
    elif param.upper() in params:
        selected_params.append(param)
        print(f"\nค่า '{param}' ได้ถูกเพิ่มแล้ว.")
    else:
        print(f"\n\033[91mเอ๊ะ เหมือนจะพิมพ์ผิดนะ ตรวจสอบดูให้ดีว่าพิมพ์ถูก หรือค่าที่ต้องการหาไม่มีในระบบ.\033[0m1")

print("\nค่าที่คุณเลือกคือ :\n", selected_params)



#ส่วนนี้เป็นการกรองข้อมูลจากวันที่และเวลา
filtered_data = [
    data_point
    for data_point in obj['stations'][0]['data']
    if year1 <= data_point['DATETIMEDATA'][:10] <= year2 and time1 <= data_point['DATETIMEDATA'][11:]
] 

while True:
    tarang = input(f"\nแสดงผลแบบแถว กด 1 แสดงผลแบบตาราง กด 2 และเมื่อเสร็จสิ้นแล้วและต้องการออก กด 3 : ")
    if tarang == '1' :
      print("\n---- แบบแถว ----\n", )
      for data_point in filtered_data:
        print(f"{data_point['DATETIMEDATA']} :")
        for param in selected_params:  
          print(f"  {param}: {data_point.get(param, 'N/A')}")
        
      print("-" * 30)

    elif tarang=='2':

      print("\n---- แบบตาราง ----\n", )



      max_datetime_length = max(len(data_point['DATETIMEDATA']) for data_point in filtered_data)


      max_param_lengths = {param: max(len(str(data_point.get(param, ''))) for data_point in filtered_data) for param in selected_params}


      print(f"| {'Date & Time':<{max_datetime_length}} |", " | ".join([f"{param:<{max_param_lengths[param]}}" for param in selected_params]), "|")

      for data_point in filtered_data:
        row = f"| {data_point['DATETIMEDATA']:<{max_datetime_length}} |"
        for param in selected_params:
            value = data_point.get(param, '---') if data_point.get(param) is not None else '---'
        
            formatted_value = f"{value:<{max_param_lengths[param]}}"
            row += f" {formatted_value} |"
        print(row)
    elif tarang=='3':
      print(" * " * 30)
      print("-" * 30)
      print("-" * 30)
      print("\n\n\033[91mThank\033[0m You \033[94mKubฟู่วว\033[0m\n\n")
      print("-" * 30)
      print("-" * 30)
      print(" * " * 30)
      break
      
    else :
      print("\033[91mไม่มีตัวเลือกนี้ กรอกใหม่นะครับ\033[0m")
      continue





