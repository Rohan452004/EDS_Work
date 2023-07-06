#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv("titanic.csv")

print(df)


# In[2]:


import matplotlib.pyplot as plt

# Sample data
x = df["Age"]
y = df["Fare"]

# Create a bar plot
plt.bar(x, y)

# Customize the plot
plt.title("Age and Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

# Display the plot
plt.show()


# In[3]:


import matplotlib.pyplot as plt

# Sample data
x = df["Age"]
y = df["Family_Size"]

# Create a bar plot
plt.bar(x, y)

# Customize the plot
plt.title("Age and family size")
plt.xlabel("Age")
plt.ylabel("Family Size")

# Display the plot
plt.show()


# In[4]:


import matplotlib.pyplot as plt

# Sample data
x = df["Age"]
y = df["Embarked"]

# Create a bar plot
plt.bar(x, y)

# Customize the plot
plt.title("Embark point vs age")
plt.xlabel("Age")
plt.ylabel("Embark point")

# Display the plot
plt.show()


# In[5]:


# Count the number of passengers in each class
passenger_counts = df['Pclass'].value_counts()

# Create a bar chart
plt.bar(passenger_counts.index, passenger_counts.values)
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.title('No of passenger and Class')
plt.show()


# In[6]:


import matplotlib.pyplot as plt

# Count the number of survivors and non-survivors
survivor = df['Survived'].value_counts()

# Create a pie chart
plt.pie(survivor.values, labels=survivor.index, autopct='%1.1f%%')
plt.title('Passenger Survival Rate')
plt.show()


# In[5]:


import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
age_data = df['Age']

plt.hist(age_data, bins=20)
plt.xlabel('Age')
plt.ylabel('Number')
plt.title('Passenger Age Distribution')
plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Group the data by age and count the number of passengers in each age group
age = df['Age'].value_counts().sort_index()

# Create a line graph
plt.plot(age.index, age.values)
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.title('Passenger Count by Age')
plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

class_counts = df['Pclass'].value_counts()

plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
plt.title('Passenger Class Distribution')
plt.show()


# In[8]:


import seaborn as sns
# Load the example Titanic dataset
titanic = sns.load_dataset('titanic')
# Create a FacetGrid with two categorical variables: class and sex
grid = sns.FacetGrid(titanic, row='class', col='sex')
# Map a plot type to the grid using the desired variable: age
grid.map(sns.histplot, 'age')
# Set common labels for y-axis and x-axis
grid.set_axis_labels('Age', 'Count')

grid.set_titles(row_template='{row_name} Class', col_template='{col_name}')
plt.show() # Show the plot


# In[30]:


# Group Plot

import pandas as pd
import matplotlib.pyplot as plt

# Read the Titanic dataset
df = pd.read_csv("titanic.csv")

# Group the data by a column (e.g., 'Sex')
grouped_data = df.groupby('Sex')

# Plotting for each group
for group_name, group_data in grouped_data:
    plt.figure()
    group_data['Age'].plot(kind='hist', bins=20)
    plt.title(f"Age distribution for {group_name}")
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.legend()
    plt.show()


# In[36]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the Titanic dataset
df = pd.read_csv("titanic.csv")

# Group the data by a column (e.g., 'Pclass')
grouped_data = df.groupby('Pclass')

# Plotting for each group
for group_name, group_data in grouped_data:
    plt.figure()
    group_data['Age'].plot(kind='hist', bins=20)
    plt.title(f"Age distribution for Class {group_name}")
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.legend()
    plt.show()


# In[37]:


#Panel Plot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Titanic dataset
df = pd.read_csv("titanic.csv")

# Create a FacetGrid object with multiple panels
g = sns.FacetGrid(df, col='Sex', row='Pclass', height=4, aspect=1.5)

# Specify the type of plot for each panel
g.map(sns.histplot, 'Age', bins=20)

# Add labels and titles to the plot
g.set_axis_labels('Age', 'Count')
g.set_titles('Sex: {col_name}, Pclass: {row_name}')

# Adjust the plot layout
plt.tight_layout()

# Show the panel graph
plt.show()


# In[39]:


import seaborn as sns

sns.countplot(data=df, x='Survived')
plt.xlabel('Survival')
plt.ylabel('Count')
plt.title('Survival Count')
plt.show()


# In[44]:


import seaborn as sns

sns.countplot(data=df, x='Embarked', hue='Survived')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.title('Embarked and Survival')
plt.show()


# In[ ]:




