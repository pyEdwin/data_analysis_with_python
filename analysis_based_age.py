#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import matplotlib.pyplot as pt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data_df = pd.read_csv('titanic_data_set.csv')

#General overview of the data
#data_df.describe()


# In[3]:


# passengers' age under 19
passengers_under_19 = data_df[data_df.Age <19]

# passengers' age under 19 that survived
passengers_under_19_survived = passengers_under_19[passengers_under_19.Survived ==1] # 1 or True

#Percentage of passengers' age under 19 that survived
passengers_under_19_percent_survived =( passengers_under_19_survived.Age.count() / passengers_under_19.Age.count() )


# In[4]:


# passengers' age between  20-49
passengers_between_20_and_49 =data_df[(data_df.Age >= 20) & (data_df.Age < 50)]

# passengers' age between  20-49 that survived
passengers_between_20_and_49_survived = passengers_between_20_and_49[passengers_between_20_and_49.Survived == 1]


#Percentage of passengers' age between  20-49 that survived
passengers_between_20_and_49__percent_survived = passengers_between_20_and_49_survived.Age.count() / passengers_between_20_and_49.Age.count()


# In[5]:


# passengers' age between  50-81
passengers_between_50_and_81 =data_df[(data_df.Age >= 50) & (data_df.Age < 81)]

# passengers' age between 50-81 that survived
passengers_between_50_and_81_survived = passengers_between_50_and_81[passengers_between_50_and_81.Survived == 1]


#Percentage of passengers' age between  50-81 that survived
passengers_between_50_and_81__percent_survived = passengers_between_50_and_81_survived.Age.count() / passengers_between_50_and_81.Age.count()


# In[6]:


# Some statistics

print(f'Under 19:{passengers_under_19.Age.count()}\t{passengers_under_19_percent_survived}')
print(f'20-49:\t{passengers_between_20_and_49.Age.count()}\t{passengers_between_20_and_49__percent_survived}')
print(f'50-81:\t{passengers_between_50_and_81.Age.count()}\t{passengers_between_50_and_81__percent_survived}')


# In[7]:


# Create a bar graph
x = ( 'under 19' , '20-49' , '50-81')
y = [0.50 , 0.39 , 0.36]
pt.bar(x , y , align ='center' , alpha = 0.5)
pt.ylabel('Percent Survived')
pt.title ('Titanic survival by group Age')

# Based on the graph, I can infer that passengers'age under 19 has been given priority.

