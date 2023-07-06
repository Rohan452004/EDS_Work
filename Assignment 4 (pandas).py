#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q.1 Print whole dataset using pandas ?

import pandas as pd

df = pd.read_csv("titanic.csv")

print(df)


# In[2]:


#Q.2 Print all attributes like count,mean,std,min of numerical columns using one function ?

print(df.describe())


# In[3]:


#Q.3 Print mean of all the columns seperately ?

print(df.mean())


# In[25]:


#Q.4 Print maximum number of family size from family size column ?

a = df['Family_Size'].max()
print("Maximum family size is",a)


# In[27]:


#Q.5 Print maximum and minimum fare from fare column ?

a = df['Fare'].max()
b = df['Fare'].min()
print("Maximum Fare is",a)
print("Minimum Fare is",b)


# In[7]:


#Q.6 Print count of passengers who paid fare greater than 100 ?

count = len(df.loc[df['Fare']>100])
print("No of passangers who paid fare >100:" ,count)


# In[30]:


#Q.7 Print count of passengers who paid fare less than 10 ?

count = len(df.loc[df['Fare']<10])
print("No of passangers who paid fare <10:" ,count)


# In[9]:


#Q.8 Print count of passengers who survived ?

count = len(df.loc[df['Survived']==1])
print("No of passangers who survived:" ,count)


# In[10]:


#Q.9 Print count of passengers who didnt survived ?

count = len(df.loc[df['Survived']==0])
print("No of passangers who didnt survived:" ,count)


# In[31]:


#Q.10 Print count of passengers who were in 1st class, 2nd class, 3rd class ?

count_1 = len(df.loc[df['Pclass']==1])
count_2 = len(df.loc[df['Pclass']==2])
count_3 = len(df.loc[df['Pclass']==3])

print("No of passangers of 1st class:" ,count_1)
print("No of passangers of 2nd class:" ,count_2)
print("No of passangers of 3rd class:" ,count_3)


# In[38]:


#Q.11 Show 10 records from top of the dataset ?

print(df.head(10))


# In[15]:


#Q.12 Print the value of total fare collected ?

print(df['Fare'].sum())


# In[16]:


#Q.13 Use groupby function to count the number of passengers embarked from C,Q,S spot ?

a=df.groupby("Embarked").count()
print(a)


# In[18]:


#Q.14 Find the mean, max and min of the columns according to the embark point of the passengers ?

a=df.groupby("Embarked").agg(['mean', 'max', 'min'])
print(a)


# In[55]:


#Q.15 Find Correlation and Covarience between different columns ?

a = df.corr()
b = df.cov()
print("Correlation \n",a,"\n")
print("Covariance \n",b)


# In[50]:


#Q.16 Find 0.25,0.5,0.75 of fare column and age column ?

a = df['Fare'].quantile([0.25, 0.5, 0.75])
b = df['Age'].quantile([0.25, 0.5, 0.75])

print("Fare \n",a,"\n")
print("Age \n",b)


# In[52]:


#Q.17 Find missing data and fill it with 0 ?

b = df.isnull()
print(b)
print("\n")
d = df.fillna(0)  
print(d)


# In[53]:


#Q.18 Convert the datatype of Age column from float to integer ?

a = df['Age'] = df['Age'].astype('int')  
print(a)


# In[22]:


#Q.19 Concat name and title column and print it ?

df1 = df["Name"]
df2 = df["Title"]
merged_df = pd.concat([df1, df2], axis=0)
print(merged_df)


# In[29]:


#Q.20 Do square operation on fare column and print its output in a seperate new column ?

df['Value_square'] = df['Fare'] ** 2
print(df)


# In[ ]:




