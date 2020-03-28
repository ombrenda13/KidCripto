#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=input()
b=input()
A=input()
B=input()
msg_x=input()

M=(int(a)*int(b))-1
e=(int(A)*M)+int(a)
d=(int(B)*M)+int(b)
n=((e*d)-1)/int(M)


encrypt=(msg_x*e)
cypher_y=int(encrypt%n)

decrypt=cypher_y*d
plaintext=(decrypt%n)

print(cypher_y)




# In[ ]:




