import math
import sys
import os



ab=int(input())
bc=int(input())

x= math.atan(ab/bc)
sinx= math.sin(x)
cosx= math.cos(x)

ac= ((ab**2)+(bc**2))**(0.5)

h= (ac/2)*sinx
b= (ac/2)*cosx

bn= bc-b

th= math.atan(h/bn)


th= math.degrees(th)
thr=round(th)
print(thr,end="")
print('°')

