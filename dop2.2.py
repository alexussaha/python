from sympy import *
from fractions import Fraction
from math import sqrt, exp
print('Введите функцию')
func = input()
x = Symbol('x')#вводим функцию напр. х^2, tan(x), atan(x)
f = diff(func,x, 2)          #ищем производную
print(f) #убрать это "#" если захочешь посмотреть производную
print('Введите нижнюю границу интегрирования')
a = int(input())
print('Введите верхнюю границу интегрирования')
b = int(input())
print('введите точность')
eps = float(input()) 
eps = Fraction(eps) # переводим точность в обычную дробь
M = float(f.evalf(subs={'x':b}))  #подставляем в производную b
M1 = float(f.evalf(subs={'x':a})) #подставляем в производную a
M = abs(Fraction(M))              # переводим точность в обычную дробь
M1 = abs(Fraction(M1))            # переводим точность в обычную дробь
if M1 > M :        #находим max|M|
     M = M1
h = Fraction(sqrt(abs(Fraction(eps*24/M))))
s = 0 # сумма
func = func.replace('^', '**') # меняем '^' на '**' т.к. питон возводит в степеь знаком '**'
print(func) #блаблабла
print(h)  #вы про это уже поняли
x1 = 0
x2 = h
while x2 <= b :             #функция суммы см. лекцию 1 умк 3
     x = (x1 + x2)/2
     l = Fraction(eval(func))
     f1 = l#это мы из записи функцию, которую ввели переводим в выражение и подставляем предыдущую строку
     print('f1 = ', f1)
     x = x2
     f2 = Fraction(eval(func))
     print('f2 = ', f2)
     s = s + Fraction(h*f1)
     x1 = x1+h
     x2 = x2+h
print(float(s))  
