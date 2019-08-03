from fractions import Fraction
p=int(input())
a=[][]
i=1
j=1
while i<=p:
    while j<=p:
        c=i+j-1
        a.append(Fraction(1,c))
        j=j+1
    i=i+1
print(a)
