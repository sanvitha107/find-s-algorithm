#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[24]:


data = pd.read_csv("play.csv")
data


# In[28]:


d = np.array(data)[:,:-1]
d


# In[29]:


target = np.array(data)[:,-1]
target


# In[27]:


conc=np.array(data)[:,:-1]
conc


# In[50]:


def train(con, tar):
    for i, val in enumerate(tar):
        if val == 'yes':
            specific_h = con[i].copy()
            break
            
    for i, val in enumerate(con):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
            print(specific_h) 
           


# In[51]:



       print(train(conc, target))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




