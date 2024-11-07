#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Exercise 1: (Score : 1)
Create a numpy array containing the numbers from 1 to 10, and then reshape it to a 2x5 matrix.

# In[4]:


a=np.arange(1,11)
print("a=",a)


# In[7]:


a_new=a.reshape(2,5)
print(a_new)

Exercise 2: (Score : 1)
Create a numpy array containing the numbers from 1 to 20, and then extract the elements between the 5th and 15th index.
# In[10]:


b=np.arange(1,21)
b[5:16]

Exercise 3: (Score : 1)
Create a Pandas series with the following data: {'apples': 3, 'bananas': 2, 'oranges': 1}. Then, add a new item to the series with the key 'pears' and the value 4.
# In[11]:


data = {'apples': 3, 'bananas': 2, 'oranges': 1}
series = pd.Series(data)
series['pears']=4


# In[12]:


print(series)

Exercise 4: (Score : 1)
Create a dataframe with the following columns: name, age, and gender. The dataframe should have 10 rows of data.
# In[18]:


data1 = {
    'Name': ['Jeeva', 'Cinderella', 'Charlie', 'David', 'Eva','Selvy','Appu', 'Freddy', 'Julie', 'Kiran'],
    'Age': [25, 30, 35, 28, 22, 26, 29, 22, 23,24],
    'Gender': ['Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male','Female','Male']
}


# In[19]:


pd_data1=pd.DataFrame(data)
print(pd_data1)

Exercise 5: (Score : 1)
Add a new column to the data frame created in question 1, called occupation. The values for this column should be Programmer, Manager, and Analyst, corresponding to the rows in the dataframe.
# In[21]:


pd_data1['Occupation']=['Programmer', 'Manager', 'Analyst', 'Programmer', 'Programmer', 'Analyst', 'Analyst',  'Programmer', 'Analyst' , 'Programmer']


# In[22]:


print(pd_data1)

Exercise 6: (Score : 1)
Select the rows of the dataframe where the age is greater than or equal to 30.

# In[27]:


print(pd_data1[pd_data1['Age'] >= 30])

Convert this dataframe to a csv file and read that csv file, finally display the contents.
# In[33]:


pd_data1.to_csv('workers details.csv', index=False)


# In[34]:


file1=pd.read_csv('workers details.csv')
print(file1)

Exercise 8: (Score : 1)
Create a line plot using matplotlib pyplot that displays the population of four different cities over time. Each city should have its own line, and the x-axis should represent years (e.g. 2010, 2011, 2012, etc.) while the y-axis should represent the population.
The data for the four cities is provided below:
City A: [500000, 550000, 600000, 650000, 700000, 750000, 800000]
City B: [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
City C: [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000]
City D: [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]
# In[41]:


years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
city_a_popln = [500000, 550000, 600000, 650000, 700000, 750000, 800000]
city_b_popln = [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
city_c_popln = [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000]
city_d_popln = [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]

# Create the line plot
plt.figure(figsize=(6, 6))
plt.plot(years, city_a_popln, label='City A')
plt.plot(years, city_b_popln,  label='City B')
plt.plot(years, city_c_popln, label='City C')
plt.plot(years, city_d_popln,  label='City D')

plt.title('Population of Cities Over Time')
plt.xlabel('Year')
plt.ylabel('Population')  
plt.legend()
plt.show()

Exercise 9: (Score : 1)
Create a scatter plot using seaborn that shows the relationship between the number of hours studied and the test scores obtained by a group of students. Use the following data:
Hours Studied: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Test Scores: [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]
# In[4]:


Hours_Studied= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Test_Scores= [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]
sns.scatterplot(x=Hours_Studied, y=Test_Scores)
plt.title('Relationship between Hours Studied and Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')


Create a bar chart using matplotlib pyplot that shows the total sales for each month of the year. Use the following data:
Month: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Sales: [11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]
# In[45]:


Month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Sales=[11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]

plt.figure(figsize=(8, 4))
plt.bar(Month, Sales, label='sales')
plt.title('Sales of each month')
plt.xlabel('Months')
plt.ylabel('Sales')  
plt.legend()
plt.show()


# In[ ]:




