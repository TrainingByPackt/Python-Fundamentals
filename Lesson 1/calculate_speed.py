distance_in_km = 150
time_in_hours = 2

distance_in_mi = distance_in_km / 1.6
distance_in_mtrs = distance_in_km * 1000

time_in_seconds = time_in_hours * 3600

speed_in_kph = distance_in_km / time_in_hours
speed_in_mph = distance_in_mi / time_in_hours
speed_in_mps = distance_in_mtrs / time_in_seconds

print("The speed in kilometers per hour is:", speed_in_kph)
print("The speed in miles per hour is:", speed_in_mph)
print("The speed in meters per second is:", speed_in_mps)
