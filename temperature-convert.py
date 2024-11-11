# Temperature Converter C <---> F
# Input
sName= input('Enter your Name: ') # Users name
print(f"Welcome to Temperature Converter, {sName}")
fTemp = float(input("Enter a temperature: ")) # Temperature Input
sC_f = input("Is the entered temperature in Celsius or Fahrenheit, please enter -> C or F: ").lower() # Was Celsius or Fahrenheit inputted

# Fahrenheit calculation and output
if sC_f == "c": # Entered temperature -> celsius
    if fTemp <= 100:
       convert_temp = fTemp * (9.0 / 5.0) + 32
       print(f"The Fahrenheit equivalent is: {convert_temp:.1f}") # Round to 1 Decimal
    else:
        print("Temp can not be > 100 ")
# Celsius calculation and output
elif sC_f == "f": # Entered temperature -> fahrenheit
    if fTemp <= 212:
        convert_temp = fTemp * (5.0 / 9.0) - 32
        print(f"The Celsius equivalent is: {convert_temp:.1f}") # Round to 1 Decimal
    else:
        print("Temp can not be > 212 ")
else:
    print("Must enter F or C")
    exit()
