#!/usr/bin/env python
# coding: utf-8

# # Practice Python Program- Basic

# # Syntax

# In[1]:


# Example -1

print("Hello Python User")


# In[2]:


# Example -2
if 10 > 5:
    print("Ten is Greater than Five")


# In[10]:


# Example -3
if 10 > 5 :
    print("Ten is less than Five")
    
if  5<10 :
    print('Five is less than ten')


# # Variable Local /Global

# In[12]:


# Example -1
x = 10
y = "Python"
print(x)
print(y)


# In[13]:


# Example -2
a = 10   # a is type int
a ="Welcome To Python world"  # a is now type str
print(a)


# In[16]:


# Example -3
x = str(10)  # x will be '10
y = int(20)  # y will be '20'
z = float(30)  # z will be 30.0


print(x,y,z)


# In[17]:


# Example -4 : Get the Type
a =10
b = "Python"
print(type(a))
print(type(b))


# In[19]:


# Example -5 - Single or Double Quotes
a ="Python"
b='Python'

print(a)
print(b)


# In[20]:


# Example -6 Varible Names are Case-Sensitive

a =100
A= "Hello"  # A will not Overwrite a

print(a)
print(A)


# In[24]:


# Example -7 
myvar = "Pyhton"
my_var = "Python"
_my_var = "Python"
myVar = "Python"
MYVAR = "Python"
myvar2 = "Python"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


# In[25]:


# Example -8  Many valuse to Multiple Variables

a,b,c = "Welcome","Python","world"
print(b,c,a)


# In[26]:


# Example -9 One Valuse to Multiple Variables

a=b=c= "Python"
print(b)
print(a)
print(c)


# In[27]:


# Example -10 Unpack a Collection

name = ["mahesh","Ram","Mukesh"]
a,c,v = name

print(v)
print(c)
print(a)


# In[29]:


# Example -11 Output Variables

a = "Easy"
print("Python is " +a)


# In[31]:


# Example -12
x = "Python is "
y = "Awesome"
z = x + y
print(z)


# In[33]:


# Example -13

x = 5
y = 10

print(x + y)


# In[35]:


# Example -14
# If you try to combine a string and number, Python will give you an error
x = 5
y = "Python"
print(x + y)


# In[40]:


# Example -15 Global Variables

a = "Python"
def myfunc():
    print(a + " is Easy To Learn")
    
myfunc()


# In[43]:


# Example -16 Create a vairable inside a function,
# with the same name as the global Variable
a = "Easy"        # this is Global Variable

def myfunc():
    a = "Not Hard" # Variable inside function
    print("Python is " + a )
    
myfunc()
print("Python is "+a)


# In[51]:


# Example -17 If you use the global keyword, the variable
# belong to the global scope :

def myfunc():
    global a
    a = "Easy"
    
myfunc()
print("Python is "+a)


# In[56]:


# Example -18 : To change the value of a global variable
# refer to the variable by using the global Keyword:

a = "Easy"

def myfunc():
    global a
    a = "Not Hard"

myfunc()
print("python is " +a)


# In[57]:


# Example -19 Create a Global Variable
x = "global"

def foo():
    print("x inside",x)

foo()
print("x outside",x)


# In[62]:


# Example -20 : Accessing Local Variable Outside the Scope

def myFun():
    B ="Local Variable"
    
myFun()
print(B)

# Will get the Name B is not Defined Error


# In[ ]:




