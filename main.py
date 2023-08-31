# 1. Declare and assign the variables here:
shuttle_name = "Determination"
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
miles_per_kilometer = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(miles_per_kilometer))

# Code your solution to exercises C and D here:

miles_to_mars = distance_to_mars_km * miles_per_kilometer
print(miles_to_mars)

hours_to_mars = miles_to_mars / shuttle_speed_mph
print(hours_to_mars)

days_to_mars = hours_to_mars / 24
print(days_to_mars)

print(shuttle_name, "will take", days_to_mars, "days to get to Mars.")


# Code your solution to exercise E here:
miles_to_moon = distance_to_moon_km * miles_per_kilometer
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(shuttle_name + " will take " + str(days_to_moon) + " days to reach the Moon.")

#the book solution did not work, TypeError: can only concatenate str (not "float") to str
#print(shuttle_name + " will take " + days_to_moon + " days to reach the Moon.")


