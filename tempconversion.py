temp = float(raw_input("Please enter the temperature (ex. 12.0): "))
measurement = raw_input("Please enter temperature measurement you would like to convert to (F or C): ")

def tempconv(temp, measurement):
    if measurement == "f" or measurement == "F":
        return ((temp*9)/5)+32
    elif measurement == "c" or measurement == "C":
        return ((temp-32)*5)/9
    else:
        return "You did not enter F or C. The current temp is " + str(temp) #Cannot concatenate strings and float objects 
        
print tempconv(temp, measurement)