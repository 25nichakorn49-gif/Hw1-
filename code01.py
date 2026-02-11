speed = int(input("Enter speed in mph: "))
distance = int(input("Enter distance in miles: "))
fmt = input("Enter output format (D or M): ")

if speed <= 0 or distance <= 0 or fmt not in ['D' or 'M']:
    print("Invalid input")
else :
    time_hours = distance / speed
    if fmt == 'D':
        print(f"At {speed} mph, it will take")
        print(f"{time_hours} hours to travel {distance} miles.")
    else:
        hours = int(time_hours)
        minutes = int((time_hours - hours)* 60)

        print(f"At {speed} mph, it will take")
        print(f"{hours} hours and {minutes} minutes to travel {distance} miles.")
      
