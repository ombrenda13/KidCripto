#!/usr/bin/env python
# coding: utf-8

# In[18]:

ED=input()
a=int(input())
b=int(input())
A=int(input())
B=int(input())
msg_x=int(input())

M=(a*b)-1


e=(A*M)+a
d=(B*M)+b
n=((e*d)-1)/M

if ED=='E':
    
    encrypt=(msg_x*e)%n
    
    print(encrypt)

else:
    
    decrypt=(msg_x*d)%n
    print(decrypt)    
    
    


    




# In[ ]:




