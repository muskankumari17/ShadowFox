num = 145
formatted = format(num, 'o')
print("Formatted (octal):", formatted)   

r = 84
pi = 3.14
area = pi * (r ** 2)
print("Pond Area:", area)

water_per_sq_meter = 1.4
water = area * water_per_sq_meter
print("Water in pond (liters):", int(water))  

distance = 490
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds
print("Speed (m/s):", int(speed))  
