# Convert the number 145 to octal representation 
def format_number(num, rep):
    return format(num, rep)

result = format_number(145, 'o')
print(result)


# Calculating area of a circular pond and amount of water it can hold
pi = 3.14
r = 84
# Area of the pond
area = pi * r * r
# Water in the pond
water = area * 1.4
print("Area of pond:", int(area))
print("Total water in pond:", int(water))


# Calculating speed of a vehicle
distance = 490
time = 7 * 60   # seconds
speed = distance / time
print(int(speed))

