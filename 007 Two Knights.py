#!/usr/bin/env python
# coding: utf-8

# In[8]:


n = int(input())
for k in range(1, n+1):
    a1 = k*k
    a2 = a1 * (a1-1)//2
    if a2 > 2:
        a2 -= 4 * (k-1) * (k-2)
    print(a2)


# In[ ]:




