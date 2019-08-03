import math
print('напишите значение переменной х')
x=float(input())
print('Если в аргументе имеется экспонента, напишите её степень, если экспоненты нет, напишите 0. Помните, что программа запишет введённые данные, как x*exp(введённая степень)')
y=float(input())
y=math.exp(y)
print('Введите точность')
eps = float(input())
w = 0
def lambertW(x, prec):
    w = 0
    for i in range(100000):
        wExpW = w*math.exp(w)
        w1ExpW = (w+1)*math.exp(w)
        w -= (wExpW-x)/(w1ExpW-(w+2)*(wExpW-x)/(2*w+2))
        if (prec > abs((x-wExpW)/w1ExpW)):
            break
    return w
print(lambertW(x*y, eps))
 
