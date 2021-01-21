#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input())
if n == 1:
    print(n)
if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            print(i, end=" ")
        for i in range(1, n, 2):
            print(i, end=" ")
    else:
        for i in range(n-1, 1, -2):
            print(i, end=" ")
        for i in range(n, 0, -2):
            print(i, end=" ")


# In[ ]:




