#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
print(n, end=" ")
while n > 1:
    if n % 2 == 1:
            n = n*3+1
    else:
        n //= 2
    print(n, end=" ")

