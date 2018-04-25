# Fahrenheit to Celsius conversion

# Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
# Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C

celsius = map(lambda x: (x - 32) * float(5)/9, [y for y in map(float, input("Enter Fahrenheit values comma seperated: ").split(","))])
print(' '.join(map(str, celsius)))
