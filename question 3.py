Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
#a
print((3+4)*5)

#b
n = int(input("Enter Number"))
ans = (n*(n-1))/2
print(ans)

#c
r = int(input("Enter Number"))
m = 4*math.pi*(r**2)        
print(m)

#d
r_1 = int(input("Enter Number"))
a = int(input("Enter Angle in Radians"))
b = math.cos(a)
c = math.sin(a)
answ = (r_1*(b)*2 + r_1(c)*2)*(1/2)
print(answ)

#e
y1 = int(input("Enter Number y1"))
y2 = int(input("Enter Number y2"))
x1 = int(input("Enter Number x1"))
x2 = int(input("Enter Number x2"))
ansr = (y1 - y2)/(x1 - x2)
print(ansr)