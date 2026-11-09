###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#


temp_C = float(input("Enter temperature in Celsius: "))
temp_F = temp_C *9/5 + 32
temp_K = temp_C + 273.15
print(f"Temperature in C: {temp_C}")
print(f"Temperature in F: {temp_F}")
print(f"Temperature in K: {temp_K}")
