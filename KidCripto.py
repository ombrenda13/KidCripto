#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=float(int(input()))
b=float(int(input()))
A=float(int(input()))
B=float(int(input()))
msg_x=float(int(input()))

M=(a*b)-1
e=(A*M)+a
d=(B*M)+b
n=((e*d)-1)/M


encrypt=(msg_x*e)
cypher_y=float(encrypt%n)

decrypt=cypher_y*d
plaintext=(decrypt%n)

print(cypher_y)




# In[ ]:




