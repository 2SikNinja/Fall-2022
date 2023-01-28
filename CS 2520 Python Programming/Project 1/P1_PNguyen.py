#Authors: Peter Nguyen
#Assignment: Project #1
#Completed (or last revision): 09/16/2022

from math import *
#Task1
print("This program will calculate your BMI using either the Imperial or Metric System")
system = input("Please enter your system preferred using either 'US' or 'Metric': ")

if(system == 'US' or system.lower() == 'us'):
    weight = float(input("Please enter your Weight in pounds: "))
    height = float(input("Please enter your Height in inches: "))
    BMI = 703*float((weight/height**2))
    if(weight < 6 or height < 18): #searched up average baby weight and heights and went down a bit for abnormal
        print("Your height or weight is invalid")
    else:
        if(18<BMI<25):
            print("Your BMI is", round(BMI,2),"and is normal!")
        elif(BMI<18):
            print("Your BMI is", round(BMI,2),"and your may be underweight")
        else:
            print("Your BMI is", round(BMI,2),"and your may be overweight")
elif(system == 'Metric' or system.lower() == 'metric'):
    weight = float(input("Please enter your Weight in kilograms: "))
    height = float(input("Please enter your Height in meters: "))
    if(weight < 6 or height < .3): #searched up average baby weight and heights and went down a bit for abnormal
        print("Your height or weight is invalid")
    else:
        BMI = float((weight/height**2))
        if(18<BMI<25):
            print("Your BMI is", round(BMI,2),"and is normal!")
        elif(BMI<18):
            print("Your BMI is", round(BMI,2),"and your may be underweight")
        else:
            print("Your BMI is", round(BMI,2),"and your may be overweight")
else:
    print("You gave an incorrect input")
    
#OUTPUTS FOR TASK 1
# 1) USA 150 lbs, 72 inch
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': US
# Please enter your Weight in pounds: 150
# Please enter your Height in inches: 72
# Your BMI is 20.34 and is normal!

# 2) USA 175 lbs, 68 inch
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': us
# Please enter your Weight in pounds: 175
# Please enter your Height in inches: 68 
# Your BMI is 26.61 and your may be overweight

# 3) Metric 72 kg, 1.83m
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': metric
# Please enter your Weight in kilograms: 72
# Please enter your Height in meters: 1.83
# Your BMI is 21.5 and is normal!

# 4) Metric 50.5 kg, 1.68m
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': metric
# Please enter your Weight in kilograms: 50.5
# Please enter your Height in meters: 1.68
# Your BMI is 17.89 and your may be underweight

# 5) USA 167 lbs, 60 inch
# Please enter your system preferred using either 'US' or 'Metric': us 
# Please enter your Weight in pounds: 167
# Please enter your Height in inches: 60
# Your BMI is 32.61 and your may be overweight

# 6) USA 129 lbs, 49 inch
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': us
# Please enter your Weight in pounds: 129 
# Please enter your Height in inches: 49
# Your BMI is 37.77 and your may be overweight

# 7) Metric 68 kg, 1.72m
# Please enter your system preferred using either 'US' or 'Metric': metric
# Please enter your Weight in kilograms: 68
# Please enter your Height in meters: 1.72
# Your BMI is 22.99 and is normal!

# 8) Metric 40 kg, 1.43m
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': metric
# Please enter your Weight in kilograms: 40 
# Please enter your Height in meters: 1.43
# Your BMI is 19.56 and is normal!

# 9) US 0 lb, 70 inch
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': us
# Please enter your Weight in pounds: 0
# Please enter your Height in inches: 70
# Your height or weight is invalid

# 10) Metric 50 kg, 0m
# This program will calculate your BMI using either the Imperial or Metric System
# Please enter your system preferred using either 'US' or 'Metric': metric
# Please enter your Weight in kilograms: 50
# Please enter your Height in meters: 0
# Your height or weight is invalid





#Task 2
print("This formula is for the Taylor formula")
x = eval(input("Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): ")) #input receival
sinFromLibrary = sin(x) #stores sin from the library into variable
mySin = 0
testCases = []
confirmation = "Y"
while(confirmation == "Y" or confirmation == "y"):
    for i in range(100000):
        mySin += ((-1) ** i) * (x ** (2 * i + 1)) /factorial(2 * i + 1) #equation execution
        testCases.append(mySin)
        if(i<1):
            finalMySin = mySin
        if (abs(mySin - sinFromLibrary) < 0.000001): #ends loop if the value is less than .000001
            break
        while(abs(mySin - sinFromLibrary) < 0.000001): #stores test cases
            testCases += mySin       
    abs(mySin - sinFromLibrary)
    print("When x = " + str(finalMySin) + ", the approximation when utilizing Taylor's Formula for sin(x) = " + str(mySin))
    print("The number of loops used to achieve the value was: ", (i+1))
    print("The stored iterations are " + str(testCases))
    confirmation = input('Would you like to iterate another time? Y/N: ')
    if (confirmation == 'N' or confirmation == 'n'): #if the user wants to continue, they enter this control statement to continue the iterations while storing cases in an array and printing it out
        break
    else:
        loops = i+1
        while(confirmation == "Y" or confirmation == "y"):
            i+1
            loops +=1
            mySin += ((-1) ** i) * (x ** (2 * i + 1)) /factorial(2 * i + 1)
            testCases.append(mySin)
            print("When x = " + str(finalMySin) + ", the approximation when utilizing Taylor's Formula for sin(x) = " + str(mySin))
            print("The number of loops used to achieve the value was: ", (loops))
            print("The stored iterations are " + str(testCases))
            confirmation = input('Would you like to iterate another time? Y/N: ')
        if confirmation == "N":
            break
        else:
            break
        
        
        
        
#OUTPUTS FOR TASK 2
# 1) x = pi/3
# This formula is for the Taylor formula
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): pi/3
# When x = 1.0471975511965976, the approximation when utilizing Taylor's Formula for sin(x) = 0.8660254450997811
# The number of loops used to achieve the value was:  5
# The stored iterations are [1.0471975511965976, 0.8558007815651173, 0.8662952837868347, 0.8660212716563725, 0.8660254450997811]
# Would you like to iterate another time? Y/N: N

# 2) x = -pi/6
# This formula is for the Taylor formula
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): -pi/6 
# When x = -0.5235987755982988, the approximation when utilizing Taylor's Formula for sin(x) = -0.4999999918690232
# The number of loops used to achieve the value was:  4
# The stored iterations are [-0.5235987755982988, -0.49967417939436376, -0.5000021325887924, -0.4999999918690232]
# Would you like to iterate another time? Y/N: N

# 3) x = 0.112
# This formula is for the Taylor formula
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): 0.112
# When x = 0.112, the approximation when utilizing Taylor's Formula for sin(x) = 0.11176584533333334
# The number of loops used to achieve the value was:  2
# The stored iterations are [0.112, 0.11176584533333334]
# Would you like to iterate another time? Y/N: N

# 4) x = pi
# This formula is for the Taylor formula
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): pi
# When x = 3.141592653589793, the approximation when utilizing Taylor's Formula for sin(x) = -7.727858894306387e-07
# The number of loops used to achieve the value was:  8
# The stored iterations are [3.141592653589793, -2.0261201264601763, 0.5240439134171688, -0.07522061590362306, 0.006925270707505135, -0.00044516023820921277, 2.1142567558399565e-05, -7.727858894306387e-07]
# Would you like to iterate another time? Y/N:

# 5) x = pi/2
# This formula is for the Taylor formula
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): pi/2
# When x = 1.5707963267948966, the approximation when utilizing Taylor's Formula for sin(x) = 0.999999943741051
# The number of loops used to achieve the value was:  6
# The stored iterations are [1.5707963267948966, 0.9248322292886504, 1.0045248555348174, 0.9998431013994987, 1.0000035425842861, 0.999999943741051]
# Would you like to iterate another time? Y/N:

# 6) x = pi/8
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): pi/8
# When x = 0.39269908169872414, the approximation when utilizing Taylor's Formula for sin(x) = 0.38268371750550756
# The number of loops used to achieve the value was:  3
# The stored iterations are [0.39269908169872414, 0.382605892675189, 0.38268371750550756]
# Would you like to iterate another time? Y/N: N

# 7) x = pi/10
# This formula is for the Taylor formula
# Please enter the x value you would like to solve for (Please user 'pi' rather than 3.14): pi/10
# When x = 0.3141592653589793, the approximation when utilizing Taylor's Formula for sin(x) = 0.3090170542193281
# The number of loops used to achieve the value was:  3
# The stored iterations are [0.3141592653589793, 0.30899155257892935, 0.3090170542193281]
# Would you like to iterate another time? Y/N: N