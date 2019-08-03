from fractions import Fraction
import math
y = float(input())
#y = math.exp(1)
f = lambda x: x*math.exp(x)
x = [0]
z = [1]
for n in range (1,30):
    if f((z[n-1]+x[n-1])/2)>y:
        x.append(x[n-1])
        z.append((x[n-1]+z[n-1])/2)
    elif f((z[n-1]+x[n-1])/2)<y:
        x.append((x[n-1]+z[n-1])/2)
        z.append(z[n-1])
print(x[29])
print(z[29])
    
