#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())
ans = []
for i in range(n):
    r, c = map(int, input().split())
    if r > c:
        if r%2 == 0:
            ans.append(r**2 - (c-1))
        else:
            ans.append((r-1)**2 + c)
    else:
        if c%2 == 0:
            ans.append((c-1)**2 + r)
        else:
            ans.append(c**2 - (r-1))
for i in ans:
    print(i)

