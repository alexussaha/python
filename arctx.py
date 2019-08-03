# arctg(x)
from fractions import Fraction
print('сначала числитель, потом знаменатель')
x1 = int(input())
x2 = int(input())
x = Fraction(x1,x2)
arctx = 0
for n in range(1,100) :
    arctx = arctx + Fraction(((-1)**(n-1))*(x**(2*n-1)),(2*n-1))
res = float(arctx)
print(res)
