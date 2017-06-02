def c_to_f(temp_c):
    new_temp_f = temp_c * (9 / 5) + 32
    return new_temp_f

Temperature = [10,-20,-289,100]

file=open("converted-temps.txt",'w')
file.close()

for temp_c in Temperature:
    if temp_c >= -273.15:
        file=open("converted-temps.txt",'a')
        file.write(str(c_to_f(temp_c))+"\n")
    else:
        file.close()

for temp_c in Temperature:
    if temp_c >= -273.15:
        print (c_to_f(temp_c),"°F")
    else:
        print("Temperature cannot be below absolute zero (-273.15 °C)!")
