#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=int(input())
b=int(input())
A=int(input())
B=int(input())
msg_x=int(input())

M=(a*b)-1
e=(A*M)+a
d=(B*M)+b
n=((e*d)-1)/M


encrypt=(msg_x*e)
cypher_y=int(encrypt%n)

decrypt=cypher_y*d
plaintext=(decrypt%n)

print(cypher_y)




# In[ ]:




