def c_to_f(temp_c):
    new_temp_f = float(temp_c) * (9 / 5) + 32
    return new_temp_f

temp_c = input("Input Temp in °C to Convert to °F: ")
print (c_to_f(temp_c))
