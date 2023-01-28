#Authors: Peter Nguyen
#Assignment: Lab #3
#Completed (or last revision): 09/13/2022

#Task 1
print("This program will compare 3 entries and print the largest")
value1 = (input("Please Enter the First Entry: "))
value2 = (input("Please Enter the Second Entry: "))
value3 = (input("Please Enter the Third Entry: "))
if value1 is not float :
    if(value1>value2>value3) :
        print(value1)
    elif(value2>value3>value1) :
        print(value2)
    else :
        print(value3)
else :
    float(value1,value2,value3)
    if(value1>value2>value3) :
        print(value1)
    elif(value2>value3>value1) :
        print(value2)
    else :
        print(value3)
#Task 1 Output
# Please Enter the First Entry: hello
# Please Enter the Second Entry: how're you
# Please Enter the Third Entry: hoho
# how're you
# Please Enter the First Entry: 35.8
# Please Enter the Second Entry: 28
# Please Enter the Third Entry: -36.5
# 35.8
# Please Enter the First Entry: Peter
# Please Enter the Second Entry: Jim
# Please Enter the Third Entry: Johnson
# Johnson


#Task 2
count = int(input("Please enter the number of items purchased: "))
total = int(input("Please enter the total cost: "))
print("Average = ", count if count==0 else total/count)

#Task 2 Output
# Please enter the number of items purchased: 3
# Please enter the total cost: 78
# Average =  26.0



#Task 3
#First Set of Code of Task 3
#Part A
#I believe in part A, the code will print 3,7,9

#Part B
#Actual Output: 3 7 9 11
i = 1
while i < 10 :
   i = i + 2
   if i == 5 :
      continue
   print(i, end =  " ")

#Part C
#No, I did not count for the last iteration where 9 was less than 10 and could iterate 11 as an output



# Second Set of Code of Task 3
# Part A
# I believe for the second set of code the ouput 2 4 6 8 10

# Part B
# Actual Output: 2 3 4 5 6 7 8 9 10
for j in range (20) : 
    j = j+2
    print(j, end =  " ")
    if j == 10 : 
       break

# Part C
# I did not account for range incrementing the loop by 1 each time, so when it looped I didn't know it would be by 1 and print out that value as well,





#Task 4
number = int(input("Enter a number to check if it is a Prime or not: "))
i,count = 2,0
while(i<=number / 2):
    if((number % i) == 0):
        count+=1
        break
    i+=1

if(count == 0):
    print(int(number), "is prime number")
else:
    print(int(number), "is prime not number")

#Task 4 Output
#37 is prime number
#35 is not prime number

