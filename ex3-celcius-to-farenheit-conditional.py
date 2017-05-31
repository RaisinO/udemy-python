def c_to_f(temp_c):
    new_temp_f = temp_c * (9 / 5) + 32
    return new_temp_f

temp_c = float(input("Input Temp in °C to Convert to °F: "))

if temp_c >= float(-273.15):
    print (c_to_f(temp_c),"°F")
else:
    print("Temperature cannot be below absolute zero (-273.15 °C)!")
