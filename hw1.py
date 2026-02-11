v = input("Enter speed in mph: ")
d = input("Enter distance in miles: ")
fmt = input("Enter output format (D or M): ")

if not v.isdigit() or not d.isdigit():
    print("Invalid input")
    exit()

v = int(v)
d = int(d)

if v <= 0 or d <= 0:
    print("Invalid input")
    exit()

fmt = fmt.upper()
if fmt not in ["D", "M"]:
    print("Invalid input")
    exit()

t = d / v

print(f"At {v} mph, it will take")

if fmt == "D":
    print(f"{t:.2f} hours to travel {d} miles.")

else:
    hours = int(t)
    minutes = int((t-hours) * 60)
    print(f"{hours} hours and {minutes} minutes to travel {d} miles.")
    
