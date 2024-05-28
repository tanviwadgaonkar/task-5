#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Tanvi\Downloads\heart.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.hist(bins=25,grid=True,figsize=(20,25))


# In[6]:


df.describe()


# In[7]:


df.columns.values


# In[8]:


df.describe


# In[9]:


df.isna().sum()


# In[10]:


df.info()


# In[11]:


question=["1.how many people have heart diseases and how many do not have heart disease"]


# In[12]:


question


# In[13]:


df.target.value_counts()


# In[14]:


df['target'].value_counts().plot(kind='bar', color=['orchid', 'salmon'])
plt.title('Heart Disease')
plt.xlabel('1 = heart disease, 0 = no heart disease')
plt.ylabel('Amount')
plt.show()


# In[15]:


df['target'].value_counts().plot(kind='pie')
plt.title('heart diseses')
plt.xlabel('  heart disease,  no heart disease')

plt.show()


# In[16]:


df.sex.value_counts()


# In[17]:


df['sex']. value_counts().plot(kind='pie')
plt.title('male female ratio')
plt.legend('male','female')


# In[18]:


pd.crosstab(df['sex'],df['target'])


# In[19]:


sns.countplot(x='target',hue='sex',data=df)
plt.title('heart disesase with different sex')
plt.xlabel('target')
plt.ylabel('count')
plt.show()


# In[20]:


df


# In[21]:


#3'people of which sex has which type of chest problem
df.cp.value_counts()


# In[27]:


df.cp.value_counts().plot(kind='bar',color=['salmon','lightskyblue','red','orange'])
plt.title('cp vs count')
plt.xlabel('cp')
plt.ylabel('count')
plt.show()


# In[23]:


pd.crosstab(df['cp'],df['target'])


# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt
#4.people with which chest pain are more prone to have heart disease?
sns.countplot(data=df, hue='target', x='cp')
plt.title('People with Both Heart Disease and Chest Problems')
plt.xlabel('Target')
plt.ylabel('Count')
plt.show()


# In[33]:


pd.crosstab(df.cp,df.sex)


# In[37]:


pd.crosstab(df.sex,df.cp).plot(kind='bar',color=['red','khaki','pink','lightblue'])
plt.title('type of chest pain for sex')
plt.xlabel('0=Female,1=Male')
plt.show()


# In[39]:


sns.displot(x='age',data=df,bins=25,kde=True)


# In[44]:


sns.displot(x='trestbps',data=df,bins=25,kde=False,color='orange')


# In[ ]:




