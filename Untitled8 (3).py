#!/usr/bin/env python
# coding: utf-8

# In[1]:


word=input("please enter a string")
counter=dict()
for i in word:
	count=0
	for j in word:
		if j==i:
			count +=1
			counter[i]=count
sort_counter=dict()
sorted_keys=sorted(counter, key=counter.get, reverse=True)
for k in sorted_keys:
	sort_counter[k]=counter[k]
for key,value in sort_counter.items():
	print(key,"=",value)


# In[ ]:




