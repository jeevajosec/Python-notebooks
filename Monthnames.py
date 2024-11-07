#!/usr/bin/env python
# coding: utf-8

# Exercise 1
# Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

# In[24]:


months=["January", "February", "March", "April", "May","June","July","August", "September", "October", "November", "December"]


# In[25]:


n=int(input("Enter an integer between 1 an 12:") )


# In[26]:


if n<1 or n>12:
        print("Entry error")
else:
        print(f" month {n} is {months[n-1]}")    


# Exercise 2
# A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user)

# In[104]:


age=int(input("Enter your age:"))


# In[105]:


if age<16:
    print("your ticket cost is 3 pounds")
elif age>=60:
    print("your ticket cost is 2 pounds")
else:
    print("your ticket cost is 36 pounds")
    


# Exercise 3
# Name your file: BodyMassIndex.py
# Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
# BMI= weight(kg)/height2(m2)
# BMI Weight Status Categories table
# BMI range - kg/m2   Category
# Below 18.5                    Underweight
# 18.5 -24.9         Normal
# 25 - 29.9          Overweight
# 30 & Above     Obese

# In[38]:


weight=float(input("Enter your weight in kg"))
height=float(input("Enter your height in meter"))


# In[40]:


BMI=weight/height**2
print(f"Your BMI is {BMI}")
if BMI<18.5:
    print('You are in the “underweight" range')
elif BMI>=18.5 and BMI<25:
    print('You are in the “Normal" range')
    
elif BMI>=25 and BMI<30:
    print('You are in the “overweight" range')
else:
    print('You are in the “obese" range')
    


# Exercise 4
# Write a Python program to receive 3 numbers from the user and print the greatest among them.
# 

# In[106]:


num1 = (input("Enter the first number: "))
num2 = (input("Enter the second number:"))
num3 = (input("Enter the third number: "))


# In[107]:


if num1>=num2:
    if num1>=num3:
        print(f"{num1} is largest")
    else:
        print(f"{num3} is largest")
else:
    if num3>=num2:
        print(f"{num3} is largest")
    else:
        print(f"{num2} is largest")

        


# Exercise 5
# Find the factorial of a given number using loops(note the number is received from the user)

# In[55]:


n=int(input("enter a non negative integer"))
i=1
fact=1
if n==0:
    print("0!=1")
else:
    while i<(n+1):
        fact=fact*i
        i=i+1
print(f"{n}!={fact}")



# Exercise 6
# Reverse a number using while loop
# 

# In[71]:


n=int(input("Enter a number"))


# In[72]:


num_rev=""
while(n>0):
    rem=n%10
    num_rev+=str(rem)
    n=n//10
print(num_rev)   


# Exercise 7
# Finding the multiples of a number using loop

# In[73]:


x=int(input("Enter a number"))


# In[76]:


for i in range(1,21):
    print(x*i)
    


# Exercise 8
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.

# In[77]:


value=input("enter a value")


# In[83]:


while True:
    value=input("enter a value")
    if value=='done':
        break
    else:
        print(value)
print("loop exit")


# Exercise 9
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

# In[89]:


for i in range(1,11):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


# In[ ]:


Exercise 10
Write a program to print the following pattern:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


# In[103]:


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print("")
        
        
    


# In[ ]:




