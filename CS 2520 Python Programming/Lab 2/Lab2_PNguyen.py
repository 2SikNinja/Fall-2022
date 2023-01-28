#Authors: Peter Nguyen
#Assignment: Lab #2
#Completed (or last revision): 09/03/2022

#Task 1

#Problem 1
print("This Program will average the age of 3 people!")
user1 = int(input("Please Enter the First Person's Age: "))
user2 = int(input("Please Enter the Second Person's Age: "))
user3 = int(input("Please Enter the Third Person's Age: "))
print((user1 + user2 +user3)//3)
'''This Program will average the age of 3 people!
Please Enter the First Person's Age: 18
Please Enter the Second Person's Age: 22
Please Enter the Third Person's Age: 19
19'''

#Problem 1 Part 2
print("This Program will average the age of 3 people!")
user1 = int(input("Please Enter the First Person's Age: "))
user2 = int(input("Please Enter the Second Person's Age: "))
user3 = int(input("Please Enter the Third Person's Age: "))
result = ((user1 + user2 +user3)/3)
print(round(result,1))
'''This Program will average the age of 3 people!
Please Enter the First Person's Age: 41
Please Enter the Second Person's Age: 53
Please Enter the Third Person's Age: 24
39.3'''

#Problem 2
pV = 1000
intRate = 5
years = 30
finalValue = pV *(1+float(intRate/100))**int(years)
print(finalValue)
'''4321.942375150667'''



#Problem 3
if("Hi" > "bye"):
    word1 = "Hi"
    word2 = "bye"
else:
    word1 = "bye"
    word2 = "Hi"

print(word1 + word2)
print(word1 *3)

if("Python" > "Java"):
    word1 = "Python"
    word2 = "Java"
else:
    word1 = "Java"
    word2 = "Python"

print(word1 + word2)
print(word1 *3)
'''byeHi
byebyebye
PythonJava
PythonPythonPython'''




#Problem 4
total = 10
count = 5
count -= 2
total += count
print(count)
print(total)
'''3
13'''



#Problem 5
iLY = "I love Python, hoho"
substring1 = iLY[7:13]
substring2 = iLY[15:19]
print(substring1)
print(substring2)

myPhrase = "I love my family and friends"
substring1 = myPhrase[10:16] #returns family
substring2 = myPhrase[21:28] #returns friends
print(substring1)
print(substring2)
'''Python
hoho
family
friends'''








#Task 2 Part 1
#This input asks for the user's name
Name = input("Please enter your name: ")

#This input asks for the user's age
Age = input("Please enter your age: ")

#This input asks the user's dream company
companyName = input("Enter the company you wish to work for: ")

#This input asks the salary the user wishes for in their job
Salary = input("Enter monthly salary you wish to earn in dollars: ")

#This print statement creates a sentence using the user's inputs
print("My name is " + Name + ", my age is " + Age + ". " + "I hope to work for Google and earn $" + Salary + " a year.")
'''Please enter your name: Peter Nguyen
Please enter your age: 20
Enter the company you wish to work for: Google
Enter monthly salary you wish to earn in dollars: 1000000
My name is Peter Nguyen, my age is 20. I hope to work for Google and earn $1000000 a year.'''





#Task 2 Part 2
#This input asks for the user's name
Name = input("Please enter your name: ")

#This input asks for the user's best friend's name
bestFriend = input("Enter your best friend's name: ")

#This input asks the user what city they met their best friend in
city = input("Please enter the city you two met: ")

#This input asks what school they went to together
school = input("What elementary school did you two go to: ")

#This print statement creates a sentence using the user's inputs
print("Hello, my name is " + Name + " and my best friend's name is " + bestFriend + ". We met in the city of " + city + " and went to " + school + ".")
'''Please enter your name: Peter Nguyen
Enter your best friend's name: Ryan
Please enter the city you two met: Temple City
What elementary school did you two go to: Savannah
Hello, my name is Peter Nguyen and my best friend's name is Ryan. We met in the city of Temple City and went to Savannah.'''