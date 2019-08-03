# arctg(x)
import math
from mpmath import mp
from fractions import Fraction
mp.dps = 100
def arctg(x1, x2):
    x = Fraction(x1,x2)
    arctx = 0
    for n in range(1,200) :
        arctx = arctx + Fraction(((-1)**(n-1))*(x**(2*n-1)),(2*n-1))
    return float(arctx)
print(mp.mpf((arctg(1,2)+arctg(1,3))*4))
print(mp.pi)
