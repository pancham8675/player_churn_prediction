#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats


# In[2]:


df=pd.read_csv('E:/3rd/MP4/dataset.csv',sep=',',header=0)
df.shape


# In[3]:


df.index


# In[4]:


df.columns


# In[5]:


df.head(10)


# In[6]:


df.tail()


# In[7]:


df.dtypes


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.isna()


# In[11]:


df.corr()  # correlation between numerical values 


# # Check for unique Player IDs

# In[12]:


distinct= len(pd.unique(df['Player ID']))
distinct


# In[13]:


df.isnull().sum()


# # Data Cleaning

# In[14]:


df.info()


# In[15]:


df.drop(['OS Version','Reason for Contact', 'App Version'],axis=1, inplace=True)


# In[16]:


df['Purchase Type'].fillna('None', inplace=True)


# # Data Preprocessing

# In[17]:


Ptype=df.groupby(["Purchase Type"])["Player ID"].count()
Ptype


# In[18]:


Dtype=df.groupby(["Device Type"])["Player ID"].count()
Dtype


# In[19]:


FBConnect=df.groupby(["Facebook Connect Status"])["Player ID"].count()
FBConnect


# In[20]:


SocialE=df.groupby(["Social Engagement through Facebook"])["Player ID"].count()
SocialE


# In[21]:


from sklearn.preprocessing import LabelEncoder
label_encoders={}
for column in ['Device Type','Purchase Type','Facebook Connect Status','Daily Login','Social Engagement through Facebook']:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])
    
for column,encoder in label_encoders.items():
    print(f"Labels for {column} :")
    print(list(encoder.classes_))

    for idx,label in enumerate(encoder.classes_):
        print(f"{idx} : {label}")
    print()


# In[22]:


df.head()


# # Visualisation

# In[23]:


import pandas as pd
import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(5, 5))
plt.pie(Ptype, labels=Ptype.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Purchase Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(5, 5))
plt.pie(Dtype, labels=Dtype.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Device Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[25]:


import pandas as pd
import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(5, 5))
plt.pie(FBConnect, labels=FBConnect.index, autopct='%1.1f%%', startangle=100)
plt.title('Distribution of FB Connect')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[26]:


import pandas as pd
import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(5, 5))
plt.pie(SocialE, labels=SocialE.index, autopct='%1.1f%%', startangle=150)
plt.title('Social Engagement through Facebook')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[27]:


plt.figure(figsize=(5, 3))
plt.boxplot(df['Level Completion Time'])
plt.title('Boxplot of Level Completion Time')
plt.ylabel('Level Completion Time')
plt.grid(True)
plt.show()


# In[28]:


plt.figure(figsize=(8, 6))
plt.hist(df['Time Played'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Time Played')
plt.xlabel('Time Played')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[29]:


import seaborn as sns

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# In[30]:


numerical_features = ['Attempts', 'Time Played', 'Level Completion Time']
for feature in numerical_features:
    plt.figure(figsize=(8, 4))
    sns.histplot(data=df, x=feature, kde=True, bins=20, palette=['skyblue', 'salmon'])
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.show()


# In[31]:


categorical_features = ['Facebook Connect Status']
for feature in categorical_features:
    plt.figure(figsize=(4, 4))
    sns.countplot(data=df, x=feature, palette=['skyblue', 'salmon'])
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()


# In[ ]:




