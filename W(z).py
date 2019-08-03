import math
y = float(input())
eps = float(input())
if y>= 0:
    y1 = 0
    y2 = math.exp(1)
    x1 = 0
    x2 = 1
else:
    y1 = math.exp(-1)
    y2 = 0
    x1 = -1
    x2 = 0
while y1 <= y <= y2:
    if y>= 0:
        x1 = x1 + 1
        x2 = x2 + 1
        y1 = x1 * math.exp(x1)
        y2 = x2 * math.exp(x2)
    else :
        x1 = x1 - 1
        x2 = x2 -1
        y1 = x1 * math.exp(x1)
        y2 = x2 * math.exp(x2)
if x1*math.exp(x1) == y:
    print('Решение: ')
    print(x1)
elif x2*math.exp(x2) == y:
    print('Решение: ')
    print(x2)
else:
    i=1
    while i<1000:
        xs = (x2 - x1)/2
        if xs * math.exp(xs) > y:
                x2 = xs
        elif xs * math.exp(xs) < y:
                x1 = xs
        i = i + 1 
    print('Решение в промежутке от')
    print(x1)
    print('до')
    print(x2)
    
