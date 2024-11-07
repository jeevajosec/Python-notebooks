#!/usr/bin/env python
# coding: utf-8

# Exercise 1: (score : 1) 
# Write a Python program to read a file and display its contents
#          

# In[15]:


f=open("details.txt","r")
f.read()


# Exercise 2: (score : 1) 
# Write a Python program to copy the contents of one file to another file

# In[19]:


f1=open("details.txt","r")
f2=open("Personal Details.txt", "w") 
contents = f1.read()
    
f2.write(contents)
f2.close()

print("File content copied successfully")


# Exercise 3: (score : 1) 
# Write a Python program to read the content of a file and count the total number of words in that file.

# In[24]:


f3=open("Personal Details.txt", "r") 
content=f3.read()
words=content.split()
count=len(words)
print(count)


# Write a Python program to read the content of a file and count the number of occurrences of a specific word in that file

# In[26]:


f3=open("Personal Details.txt", "r") 
content=f3.read()
words=content.split()
num=words.count("is") #looking no of times "is" is used.
print(num)


# Exercise 5: (score : 1) 
# Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occur

# In[8]:


value=input("Enter a number")
try:
    int_value=int(value)
    print(f"Integer value is {int_value}")
except:
    print("Value cannot be converted to integer")
    


# Exercise 6: (score : 1) 
# Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.

# In[35]:


L = input("Enter some integers separated by space: ")
L_new=L.split()
try:
    int_L_new=[int(x) for x in L_new]
    for i in int_L_new:
        if i<0:
            raise Exception
    
except ValueError:
    print("Integers are only allowed")

except Exception:
    print("Negative integer found")


# Exercise 7: (score : 1) 
# Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running.
# 

# In[41]:


import math
L = input("Enter some integers separated by space: ")
L_new=L.split()
try:
    int_L_new=[int(x) for x in L_new]
    Average=sum(int_L_new) / len(int_L_new)
    print(Average)
except ValueError:
    print("Integers are only allowed")
except Exception:
    print(f"An unexpected error occurred")
finally:
    print("The program has finished running.")

    


# Exercise 8 : (score : 1) 
# Write a Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
# 

# In[45]:


file=input("Enter a file name")
try:
    f1=open(file,'w')
    f1.write("Hi how are you")
    print("Welcome")

except FileNotFoundError:
    print("Error: The file was not found.")
except:
    print("Something went wrong")

    


# Exercise 9 : (score : 1)
# Build a program to manage a university's course catalogue. You want to define a base class Course that has the following properties:
# course_code: a string representing the course code (e.g., "CS101")
# course_name: a string representing the course name (e.g., "Introduction to Computer Science")
# credit_hours: an integer representing the credit hours for the course (e.g., 3)
# You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
# CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major.
# ElectiveCourse should have an additional property elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").

# In[70]:


class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name    
        self.credit_hours = credit_hours  
    def describe(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major
    
        
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
         super().__init__(course_code, course_name, credit_hours)
         self.elective_type=elective_type
    


    


# In[71]:


course1=Course("Py121","Python",3)
print(course1.describe())


# In[72]:


class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code  # Correctly set course code
        self.course_name = course_name    # Correctly set course name
        self.credit_hours = credit_hours    # Correctly set credit hours

    def describe(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"

# Subclass for CoreCourse
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major  # Correctly set required for major

# Subclass for ElectiveCourse
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type  # Corrected variable name

# Example usage

    course1= CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    course2 = ElectiveCourse("ART101", "Introduction to Art", 3, "liberal arts")
    course3 = CoreCourse("Py121", "Python For Data Science", 5, True)
    # Print the course information
    print(course1.describe())
    print(course2.describe())


# Exercise 10: (score : 1)
# Create a Python module named employee that contains a class Employee with attributes name, salary and methods get_name() and get_salary(). Write a program to use this module to create an object of the Employee class and display its name and salary.
# 
File: employee.py

class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def get_name():
        return f"Employee name: {self.name}"
        
    def get_salary():
        return f"Salary: {self.salary}"
        
# In[2]:


from employee import employee
employee1 = employee("Jeeva", 500000)
print(employee1.get_name())
print(employee1.get_salary())


# In[ ]:




