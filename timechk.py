import time
timestamp=int(time.strftime("%H%M%S"))
print(timestamp)
if timestamp>120000:
    print("Good Afternoon")
else:   print("Good Morning") 