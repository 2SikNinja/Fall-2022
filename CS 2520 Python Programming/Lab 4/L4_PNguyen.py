#Authors: Peter Nguyen
#Assignment: Lab #4
#Completed (or last revision): 09/22/2022

import math


#Task 1
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
#sum is less accurate than fsum resulting in sum being .99999999 and fsum being 1.0


#Task 2
#Before Output: it will just print i for the iteration and space them
def prob2() :
    for i in range (4) :
        print(i, end = ' ' )
print(prob2())
#After Output: The end prints None since there is no return

#Task 3
def fun (x = 1, y = 2):
    x = x + y
    y += 1
    return x*y
print(fun(3,2))
print(fun(x=3))
print(fun(y=2))
print(fun(x=3, y=2))
print(fun())
print(fun(10))
print(fun(y=2, x=3))

#Task 4
letterGrade = "F"
def grade(testScore):
    if testScore<0:
        letterGrade = "You inputted an incorrect score!"
    elif 0<=testScore<60:
        letterGrade = "You got an F"
    elif testScore<70:
        letterGrade = "You got a D"
    elif testScore<80:
        letterGrade = "You got a C"
    elif testScore<90:
        letterGrade = "You got a B"
    elif testScore<=100:
        letterGrade = "You got an A"
    else:
        letterGrade = "You inputted an incorrect score!"
    return letterGrade
userInput = int(input("What did you get on your test? (Please Type Your Score): "))
score = grade(userInput)
print(score)

# Outputs for Task #4
# 1)  What did you get on your test? (Please Type Your Score): -5
#     You got an F
    
# 2)  What did you get on your test? (Please Type Your Score): 105
#     You got an A and extra credit!
    
# 3)  What did you get on your test? (Please Type Your Score): 100
#     You got an A
    
# 4)  What did you get on your test? (Please Type Your Score): 87
#     You got a B
    
# 5)  What did you get on your test? (Please Type Your Score): 69
#     You got a D
    
# 6)  What did you get on your test? (Please Type Your Score): 158
#     You got an A and extra credit!
    
# 7)  What did you get on your test? (Please Type Your Score): 84
#     You got a B