#!/usr/bin/env python
# coding: utf-8

# # Variable Local /Global

# In[2]:


# Example -21 
# Python Program to Create Global Variable

x = "global"

def foo():
    print("x inside:",x)

foo()
print("x outside:",x)


# In[6]:


# Python Program to 
# Example -22
a = "easy"
def one():
    a =a*5
    print(a)
one()

#Will get error because we defined in function : UnboundLocalError: local variable 'a' referenced before assignment 


# In[7]:


# Python Program to Creat a Local Variable
# Example -23

def myFun():
    a = "Local Variable"
    print(a)

myFun()


# In[8]:


# Python Program to Using GLobal and Local Variable s in the same code
a = "Global Variable "
def myFun():
    global a
    b = "Local Variable "
    a = a * 2
    b = b * 2
    print(a)
    print(b)
myFun()


# In[11]:


# Python Program to Gloabl Variable and Local Variable with same Name
# Example -25
a = 10 # Global

def myfunone():
    a = 20  # Local Fun
    print("Print Local Variable a =", a)
    
myfunone()
print("Print Global Variable a =" , a)


# In[14]:


# Python Program to Create NonLocal Variable
# Example -26

def outer():
    a ="Local"
    
    def inner():
        nonlocal a
        a ="nonlocal"
        print("inner:",a)
    inner()
    print("outer:",a)
outer()


# In[15]:


# Python Program to 
# Example -27
c = 10  # global Variable

def add():
    print(c)
    
add()


# In[20]:


# Python Program to 
# Example -28

a = 10  # global Variable

def add():
    a = a+2 # increment a by 2
    print(a)
add()
## UnboundLocalError: local variable 'a' referenced before assignment


# In[24]:


# Python Program to  Changing Global Variable From Inside a Function using Global
# Example -29

a = 0 # global Variable

def add():
    global a
    a = a +2
    print("inside add():",a)
add()
print("In Main:",a)


# In[26]:


# Python Program to  using a Global Variable in Nested Function 
# Example -30

def A():
    a =10 
    
    def B():
        global a 
        a =20
        
    print("Before Calling B:",a)
    print("Calling B Now")
    B()
    print("After Calling B:",a)
    
A()
print("a in Main:",a)


# In[2]:


# Python Program to  Create a Global Variable 
# Example -31
a ="Global Variable"

def A():
    print("a inside:",a)
    
A()
print("a ouside:",a)


# In[6]:


# Python Program to Accessing Local Variable outside the Scope
# Example -32

def A():
    b ="Local"
A()
print(b)

# Get the Error : NameError: name 'b' is not defined


# In[7]:


# Python Program to Create a Local Variable
# Example -33
def A():
    a = "Local"
    print(a)
A()


# In[9]:


# Python Program to  Using Gloabl and Local Variables in the Same Code
# Example -34

a = "Global Variable"

def A():
    global a
    b = "Local Variable"
    a = a*2
    print(a)
    print(b)
A()


# In[11]:


# Python Program to Global Variable and Local Variable with same Name
# Example -35

a =15

def A():
    a =25
    print(a)
    
A()
print(a)


# In[13]:


# Python Program to 
# Example -36

def A():
    #Local Variable
    a ="Python Word"
    print(a)
    
A()
    


# In[17]:


# Python Program to get the Error
# Example -37

def A():
    #local Variable
    c ="Python World"
    print("inside Function",c)

A()
print(c)


# In[22]:


# Python Program to Global Variable
# Example -38

def A():
    print("Inside Function :",a)
    
a = "Python World"
A()
print("Outside Function:",a)


# In[23]:


# Python Program to 
# Example -39

def A():
    a ="Hello"
    print(a)
a= "Python World"  # global Scope
A()
print(a)


# In[25]:


# Python Program to  WIll Get the Error 
# Example -40

def A():
    a + =10
    print(a)
    
a = "Python world"  # Global Scope
A()


# In[29]:


# Python Program to  Using Global Keyword
# Example -41

def A():
    global a
    a +='HI'
    print(a)
    a = "I Love Python"
    print(a)

a ="PYthon World"  # Global Scope
A()
print(a)


# In[35]:


# Python Program to  Using Global And Local Variables
# Example -42

a = 10

def A():
    print("Function A:",a)
    
def B():
    a = 20
    print("Function B:",a)
def C():
    global a
    a = 30
    print(a)

print(a) # global Scope
A()
B()
print(a)
C()
print(a)


# In[37]:


# Python Program to  showing no need to use gloab keyyword for accessing a global value
# Example -43

# Global Variable
d = 20
v = 10

#function to perform addition
def add():
    n = d + v
    print(n)
#Calling a function
add()


# In[38]:


# Python Program to Without Global Keyword  WILL GET ERROR AS NOT DEFINED
# Example -44

# a Global Value without using global keyword

n = 15

# function to change a gloabl value
def change():
    
    #increment value of n by 5
    n = n+5
    print(n)
change()


# In[39]:


# Python Program to  Global Keyword
# Example -45

m = 10
def M():
    global m
    m = m +5
    print("inside Function:",m)
    
M()
print("outside Function:",m)
    


# In[40]:


# Python Program to  Showing a use of Global in Nested function
# Example -46

def X():
    x = 10
    def H():
        global x
        x = 20
    print("Before Change:",x)
    print("Making change")
    H()
    print("After Making Change:",x)
    
X()
print("value of x:",x)


# In[42]:


# Python Program to 
# Example -47

g = 50  # local variable
h = 20

def sum():
    b = g + h      #using global variable
    print(b)

def sub():
    d = g- h
    print(d)
#function call
sum()
sub()


# In[43]:


# Python Program to 
# Example -48

def N():
    q = "Python World"
    print(q)
N()
q ="Python is Easy"
print(q)


# In[44]:


# Python Program to  with Global Keyword
# Example -49

c  = 10 

def Y():
    global c
    c = c*2
    print("inside Function:",c)
    
Y()
print("Outside Function :",c)




# In[48]:


# Python Program to 
# Example -50
city = "pune"      # global variable

def Y():
    y = "AI"   # local Variable
    print("To Learn {}, we need {} programming in {} city".format(y,cl,city))
    
def U():
    u = "ML"   # local Variable
    print("To learn {}, we need {} programming in {} City".format(u,cl,city))
    
def I():
    i = "DL"   # Local Variable
    print("To Learn {}, we need {} Programming in {} city".format(i,cl,city))
    
cl = "Python"  # Global Variable
Y()
U()
I()


# In[49]:


# Python Program to 
# Example -51

r = 10  # global Variable


def update1():
    global r
    print(r)
    r = r + 10
    print(r)
    
def update2():
    global r
    r = r * 10
    print(r)
    
# Main Program
print("Val of r in main program = {}".format(r))   # 10
update1()

print("val of r in main program after update1() = {}".format(r))   # 20
update2()

print("val of r in main program after update2()={}".format(r))  # 200


# In[1]:


# Python Program to 
# Example -52
a = 10
b = 20

def modify1():
    global a,b
    print(a)  # 10
    print(b)  # 20
    a = a + 10
    b = b + 20
    print(a)
    print(b)
    
#main Program 
modify1()
print("val of a--global var after modification in main ={}".format(a))  # 20
print("val of b--global var after modificaiton in main ={}".format(b))  # 40


# In[2]:


# Python Program to 
# Example -53
a = 10 
b = 20
c = 30
d = 40  # here a,b,c,d are the Global Variable

def cal():
    global c,d
    c = c +10
    d = d + 20
    a = 50
    b = 100    # here a, b are local variable
    print("val of a (local Var)={}".format(a))
    print("val of b (Local var)={}".format(b))
    print("Val of a(global Var)={}".format(globals()['a']))
    print("val of b (gloabl var)={}".format(globals()['b']))
    print("-"*50)
    res = a +b+c+d+globals().get('a') + globals()['b']
    print("sum ={}".format(res))
    print("-" *50)
    
#main program
cal()


# In[4]:


# Python Program to 
# Example -54

q = 10
w = 20
e = 30
r = 40  # q,w,e,r are global variables

def calc():
    US = globals()
    for k, v in US.items():
        print("{}----{}".format(k,v))
        print("-----------------")
        print("val of q=",US['q'])
        print("val of w =",US.get('w'))
        print("val of e=",globals()['e'])
        print("val of r =",globals()['d'])
        print("sym={}".format(globals()['q']+globals()['w']+globals()['e']+globals()['r']))

# Main Program
calc()
                             


# In[6]:


# Python Program to 
# Example -55
x = 100
def A():
    global x 
    x = 200
    
A()
print(x)


# ## Display Output

# In[7]:


# Python Program to 
# Example -56
print("Python")
print("welcome to python world")



# In[11]:


# Python Program to 
# Example -57
a = 10 
print(a)

lst = [10,'HELLO', 23.45]
print(lst)

print(a,lst)


# In[13]:


# Python Program to 
# Example -58

a = 10
print("val of a =",a)
print(a,"val of a")


# In[14]:


# Python Program to 
# Example -59
a =10 
b = 20
c = a + b
print("sum of ", a, "and",b,"=",c)


# In[15]:


# Python Program to 
# Example -60

a = 10
b = 20
c = a + b
print("val of a ={}".format(a))
print("{} val of a".format(b))
print("sum of {} and {} ={}".format(a,b,c))


# In[16]:


# Python Program to 
# Example -61

a = 10 
b = 20
c = a + b 
print("sum of %d and %f =%f" % (a,b,c))


# In[ ]:





# In[ ]:




