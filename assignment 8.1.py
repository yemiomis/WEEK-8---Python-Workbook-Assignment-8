#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")


# In[5]:


df.head()


# In[6]:


df.hist()


# In[11]:


df.hist(column="hours", by="gender")


# In[ ]:




