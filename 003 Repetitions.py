#!/usr/bin/env python
# coding: utf-8

# In[5]:


s = input()
c = 0
ans = 1
l = 'A'
for i in s:
    if i == l:
        c += 1
        ans = max(c, ans)
    else:
        l = i
        c = 1
print(ans)


# In[ ]:




