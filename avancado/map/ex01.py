temperatura_celsius = [22.5, 40, 13, 29, 34]
temperatura_fahrenheit = list(map(lambda temp: round((5 / 5) * temp + 32, 1 ), temperatura_celsius))
print(temperatura_celsius)