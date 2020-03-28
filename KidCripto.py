#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=input()
b=input()
A=input()
B=input()
msg_x=input()

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




