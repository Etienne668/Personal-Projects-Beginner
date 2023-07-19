#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 5 
print('Before 5')
if x == 5 :
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print ('Afterwards 5') 
print('Before 6') 
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')


# In[3]:


astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print ('First', istr)

astr = '123'
try:
    istr = int(astr)
except: 
    istr = -1

print ('Second', istr)


# In[8]:


rawstr = input('Enter a number: ') 
try:
    val=int(rawstr)
except:
    val=-1

if val>0:
    print('Nice work')
else: 
    print('Not a number')


# In[ ]:




