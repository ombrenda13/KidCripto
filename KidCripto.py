#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=input()
b=input()
A=input()
B=input()
msg_x=input()

M=(float(a)*float(b))-1
e=(float(A)*M)+float(a)
d=(float(B)*M)+float(b)
n=((e*d)-1)/float(M)


encrypt=(msg_x*e)
cypher_y=float(encrypt%n)

decrypt=cypher_y*d
plaintext=(decrypt%n)

print(cypher_y)




# In[ ]:




