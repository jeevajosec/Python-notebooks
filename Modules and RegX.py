#!/usr/bin/env python
# coding: utf-8

# Exercise 1: (score : 2)
# Write a Python program to calculate the square root of a number using the math module.
# 

# In[4]:


import math
n=float(input("Enter a number:"))
sqrt_n = math.sqrt(n)
print(f"Square root of {n} is {sqrt_n}")


# Exercise 2: (score : 2)
# Write a Python program to generate a random number between 1 and 10 using the random module.

# In[8]:


import random
r=random.randint(1,10)
print(r)


# Exercise 3: (score : 2)
# Write a Python program to calculate the factorial of a number using the math module.

# In[12]:


n=int(input("Enter a integer"))
fact=math.factorial(n)
print(f"{n}!={fact}")


# Exercise 4: (score : 2)
# Create a Python module named math_operations that contains functions to calculate the area of a circle, the area of a rectangle and the area of a triangle. Write a program to use this module to perform area calculations.
# 

# # File: Math_Operations.py
# 
# 
# pi=3.14
# #area of a circle
# def area_circle(r):
#     area=pi*r*r
#     return area
# 
# #area of a rectangle
# def area_rectangle(l,b):
#     area=l*b
#     return area
# 
# #the area of a triangle.
# def area_triangle(b,h):
#     area=.5*b*h
#     return area
# 

# In[22]:


import Math_Operations
r=1
Area_of_circle=Math_Operations.area_circle(r)
print("Area of circle=",Area_of_circle)

l=5
b=10
Area_of_Rectangle=Math_Operations.area_rectangle(l,b)
print("Area of rectangle=",Area_of_Rectangle)

b=5
h=6
Area_of_Triangle=Math_Operations.area_triangle(b,h)
print("Area of triangle=",Area_of_Triangle)


# Exercise 5: (score : 2)
# Create a Python module named temperature_conversion that contains functions to convert Celsius to Fahrenheit and Fahrenheit to Celsius. Write a program to use this module to perform temperature conversions.
# 

# # File:temperature_conversion.py
# 
# #celsius to fahrenheit
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
# 
# #fahrenheit to celsius
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# In[24]:


import temperature_conversion

celsius1 = 25

fahrenheit = temperature_conversion.celsius_to_fahrenheit(celsius)
print(f"{celsius1}°C is {fahrenheit}°F")


fahrenheit1 = 77
celsius = temperature_conversion.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit1}°F is {celsius}°C")


# In[ ]:




