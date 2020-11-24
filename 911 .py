#!/usr/bin/env python
# coding: utf-8

# In[1]:


#check for data file
import os


# In[2]:


print(os.listdir())


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


dataFrame = pd.read_csv('911.csv')


# In[5]:


dataFrame.info()


# In[18]:


#check head for our dataFrame
dataFrame.head()


# In[9]:


#top5 zipcodes
dataFrame['zip'].value_counts().head(5)


# In[14]:


#top 5 township reaching 911
dataFrame['twp'].value_counts().head()


# In[16]:


#unique resons for 911
dataFrame['title'].nunique()


# In[24]:


#top five specific reasons to call 911
dataFrame['SpecificReason'] = dataFrame['title'].apply(lambda title:title.split(':')[1])


# In[25]:


dataFrame


# In[26]:


dataFrame['SpecificReason'].value_counts().head(10)


# In[30]:


dataFrame['BroadReasons']=dataFrame['title'].apply(lambda title:title.split(':')[0])


# In[31]:


dataFrame.head()


# In[32]:


dataFrame['BroadReasons'].value_counts()


# In[34]:


#count plot for broad resons
sns.countplot(x ='BroadReasons',data=dataFrame)


# In[35]:


#changing column type fron obj to datatime 
dataFrame['timeStamp'] =pd.to_datetime(dataFrame['timeStamp'])


# In[36]:


dataFrame.info()


# In[38]:


type(dataFrame['timeStamp'].iloc[0])


# In[41]:


#create 3 columns Hour ,Month and day of week
dataFrame['Hours']=dataFrame['timeStamp'].apply(lambda time: time.hour)


# In[42]:


dataFrame.head()


# In[46]:


dataFrame['Month']=dataFrame['timeStamp'].apply(lambda months:months.month)


# In[47]:


dataFrame.head()


# In[57]:


dataFrame['Day']=dataFrame['timeStamp'].apply(lambda days:days.dayofweek)


# In[58]:


dataFrame.head()


# In[59]:


dataFrame['Day'].nunique()


# #### gives count of  unique value 

# In[103]:


#plot a graph for Month
g=sns.countplot(x='Month',data=dataFrame,hue='BroadReasons')

plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.title('BroadReasons')


# In[82]:


#use group_by
byMonth=dataFrame.groupby('Month').count()


# In[83]:


byMonth


# In[84]:


byMonth['twp'].plot()


# In[85]:


byday=dataFrame.groupby('Day').count()


# In[87]:


byday['twp'].plot()


# In[101]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# Load the long-form example gammas dataset
gammas = sns.load_dataset("gammas")

# Plot the response with standard error
sns.lineplot(data=gammas, x="timepoint", y="BOLD signal", hue="ROI")

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:




