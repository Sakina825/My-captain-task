#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[13]:


headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


# In[14]:


req=requests.get("https://www.oyorooms.com/",headers=headers)


# In[15]:


req.status_code


# In[16]:


req.text


# In[17]:


req.content


# In[ ]:





# In[ ]:




