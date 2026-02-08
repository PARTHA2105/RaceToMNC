import sys

#single line comment user '#'
"""
Use to create multiple line comment.
"""

# print("Hi Partha",end=" ")
# print("What are you doing.")
# print("Im Partha",24,"Years old young man")
# print("Hii"); print("Parthasarathi ")

"""
#Global variable declaration
x= str(10)
y= 20
z= 10.4

print(y);print(z)
global yy
yy=49
g= bool(x)
print(g)
def myFun():
    #global yy
    yy=200
    print(x)


myFun()
print(yy) #global variable declared inside the fuction .
#If you want to bind the global variable inside the function also possible to access to the other places. like ' global x' now you can call x anywhere

"""
#Data Type Constructor :

""" Data types values
hello
4
40.5
['A', 'B']
range(0, 5)
{'name': 'Partha', 'age': 24}
{'A', 'D'}
frozenset({1, 3})
True
b'\x00\x00\x00\x00\x00'
bytearray(b'\x00\x00\x00\x00\x00')
<memory at 0x106f02dc0>

class 'str'>

class  'int'>
class  'float'>
class  'comples'>

<class 'list'>
<class 'tuple'>
<class 'range'>

<class 'dict'>

<class 'set'>
<class 'frozenset'>

<class 'bool'>

<class 'bytes'>
<class 'bytearray'>
<class 'memoryview'>

<class 'NoneType'>

None = NO TYPE - 

"""
"""
#complex
a=str('hello')
print(type(a))

b=int(4)
c= float(40.5)
d= list(("A","B"))
print(type(d))


e= tuple((1,4,))
print(type(e))

f= range(5)
print(type(f))

g= dict(name="Partha",age=24)
print(type(g))

h= set(("A","D"))

print(type(h))

j= frozenset((1,3))

print(type(j))

k= bool(4)

print(type(k))

l= bytes(5)

print(type(l))

m= bytearray(5)

print(type(m))

n= memoryview(bytes(5))
print(type(n))

c= None
print(type(c))


print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)
print(j)
print(k)
print(l)
print(m)
print(n)

#Data type region end here.

#Numbers : int, float, complex

x= 1
y= 10.3
v= 1j

nn = float(x)
mm= complex(x)

## can't convert complex to float or int kk= float(v)

print(nn)
print(mm)

import random

print(random.randrange(2,5)) # start with 2 to 4 not inlude 5 

for i in range(5): #0,1, 2,3,4
    print(i)


"""


# Strings

# Strings in python are array of unicode.
# You can access the string 'char' through 'square brackets'
# since string are array type we can use all the loops to get the characters.


"""

name= "Parthasarathi"

for char in name:
    print(char,end="")
print()

if("P" in name): #like that 'not in' also can use.
    print("Yes")
    print(len(name))

print(f"Parthasarathi {56}")
print(f"price of the product {50:.2f}")
print(f"price of the product {50+2}")
print("Parthasarathi {initial}".format(initial="U"))

txt = "Print value {val}".format_map({"val": 50}) #Pass it as a Dictionary
print(txt)
"""

#operator:
x = 15
y = 4

print(x + y) #19
print(x - y) #11 
print(x * y) #60
print(x / y) #3.75
print(x % y) # 3
print(x ** y)  #50625
print(x // y) #3


#print the second index item

val = list(("a","dd","hh"))
v= ["d","dd","tt"]
print(val[-1]) #reverse order start from the end.

print(val[1])
print(val[:3])
