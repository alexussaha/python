import math
import mpmath as mp
from fractions import Fraction
mp.dps = 1000
f = lambda x: math.sin(x)
x = [3]
z = [4]
for n in range (1,200):
    if f(x[n-1])*f((x[n-1] + z[n-1])/2) < 0 :
                x.append(x[n-1])
                z.append(Fraction((x[n - 1] + z[n - 1]),2))
    else :
            x.append(Fraction((x[n - 1] + z[n - 1]),2))
            z.append(z[n-1])
a = float(x[199])
b = float(z[199])
print(mp.mpf(a))
print(mp.pi)
print(mp.mpf(b))
