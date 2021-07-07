#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt  
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer  #importing differenet libraries needed in the project


# In[2]:


df = pd.read_csv('/home/reekraj/Downloads/covid_19_data.csv')  #using a pandas object the dataset is being read


# In[3]:


df.head(50)  #displaying the first 50 rows from the given dataset


# In[4]:


df.drop(['SNo','Last Update'],axis=1,inplace=True)  #dropping the S.No and Last Update column from the table
df.rename(columns={'ObservationDate':'Date','Province/State':'State','Country/Region':'Country'},inplace=True)
#renaming colmuns 


# In[5]:


df['Date'] = pd.to_datetime(df['Date'])  #changing date format from the default mm/dd/yyyy format to
                                        #the yyyy/mm/dd, the date format offered by Pandas library


# In[6]:


imputer = SimpleImputer(strategy='constant')  #imputing missing data
df2 = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)


# In[7]:


df3 = df2.groupby(['Country','Date'])[['Country','Date','Confirmed','Deaths','Recovered']].sum().reset_index()
#grouping data in the table for better arrangement of data


# In[8]:


df3.head(20)  #displaying the first 20 rows from the dataset following the new changes made


# In[9]:


countries = df3['Country'].unique()  #finding total number of countries present in the dataset
len(countries)


# In[10]:


for idx in range(0,len(countries)):    #running a for loop for the countries in alphabetical order 
    C = df3[df3['Country']==countries[idx]].reset_index()  #the plot is made using matplotlib       
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])  #setting country name as title of the plot
    plt.xlabel('Days since the first suspect')#x axis shows days since first case reported in a given country
    plt.ylabel('Number of cases')#y axis showing number of countries
    plt.legend()
    plt.show()#displaying the plot


# In[11]:


df4 = df3.groupby(['Date'])[['Date','Confirmed','Deaths','Recovered']].sum().reset_index()
#creating a new group for cumulative representation of data using a single plot


# In[12]:


C = df4
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('World')#title of plot is set as World
plt.xlabel('Days since the first suspect')#x axis represents days since first reported case
plt.ylabel('Number of cases')#y axis represents number of cases in order of 10^8
plt.legend()
plt.show()#displaying the plot


# In[ ]:




