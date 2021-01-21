#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())
a = list(map(int, input().split()))
c = a[0]
ans = 0
for i in range(1, len(a)):
    if c > a[i]:
        ans += c - a[i]
    else:
        c = a[i]
print(ans)


# In[ ]:




