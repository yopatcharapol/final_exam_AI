temp = int(input("Enter temperature\n"))

if temp >= 25 and temp <= 27:
    print("good weather")
elif temp >= 20:
    print("quite cold")
elif temp >= 10:
    print("cold")
else:
    print("so cold")

