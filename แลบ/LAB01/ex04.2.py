temp = int(input("Enter temperature\n"))

if temp >= 25 and temp <= 27:
    print("good weather")
elif temp >= 10:
    print("quite cold" if temp < 20 else "cold")
else:
    print("so cold")
