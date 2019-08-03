from fractions import Fraction
p = int(input())
a = [0] * p
i = 0
while i <= p-1:
    j=0
    a[i] = [0] * p
    while j <= p-1:
        a[i][j] = Fraction(1, (i+1) + (j+1)-1)
        j = j + 1
    i = i + 1
#print(*a)
i = 0
b = [0] * p
b[0] = 1
#print (*b)
l = 0
g = 1
while g <= p :
    i = g
    while i <= p-1:
        j = 0
        k = a[i][l]/a[l][l]
        while j <= p-1:
            a[i][j] = a[i][j] - k * a[l][j]
            j = j + 1
        b[i] = b[i] - k * b[l]
        #print(a)
        #print(b)
        i = i + 1
    l = l + 1
    g = g + 1
d = 0
i = p - 1
x = [0]*p
while i >= 0:
    if i == p-1:
        d = 0
    else:
        d = 0
        j =  i
        while j <= p-1:
            s = a[i][j] * x[j]
            d = s + d
            j = j + 1
    x[i] = (b[i] - d)/a[i][i]
    i = i - 1
#x[0] = b[0]/a[0][0]
print('Корни системы')
i=0
while i<p:
    print(x[i])
    i=i+1

