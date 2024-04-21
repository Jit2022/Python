import random
def testfunc():
    global x
    x="Subhojit"
    print (x)
testfunc()
print(x)
a=1
b=1.01
c="Subhojit"
d=1j
e=["Subhojit","Joy","Jiko"]
f={"Subhojit","Joy","Jiko"}
g=1.00234e45
h=float(a)

print(type(a))
print(type(b))
print(type(c))  
print(type(d))  
print(type(e))
print(type(f))
print(type(g))
print(random.randrange(1,100))
print(h)
print(type(h))

str="""Subhojit is studying 
Python to make himself ready"""
print(str)
print(str[0])

for i in "Subhojit":
    print (i)
    print ("Subhojit" in c)

if "Subhojit" in c:
    print ("true")
    
str1="Subhojit is a good boy"
if "sonali" not in str1:
    print("Fine")

print(str1[5:])
print(str1[:2])
print(str1.upper())
print(str1.lower())
print(str1.split(" "))
print(str1.replace(" ","_",3))
print(str+str1)

age=40
str3=f"Subhojit is {age} year old"
print(str3)

print("Subhojit is today \"40 Years\" old")
print(len(str1))
#print(str1.len())