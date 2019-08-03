from fractions import Fraction #штука для работы с обычными функциями
from sympy import *#Это нужно для производной
from matplotlib import mlab
import numpy
import math
print('Введите функцию')
func = str(input() )         #вводим функцию напр. х^2, tan(x), atan(x)
print('eps =')
eps = float(input())
print('min = ')
min_l = float(input())
print('max =')
max_l = float(input())
def methofrect(fun, min_l, max_l, eps):
     def integral(fun, min_l, max_l, n):
          integ = 0.0
          step = (max_l - min_l) / n
          for x in numpy.arange( min_l, max_l-step, step):
               integ = integ + step * fun(x + step / 2)
          return integ

     d, n = 1, 1
     while math.fabs(d) > eps:
          d = (integral(fun, min_l, max_l, n * 2) - integral(fun, min_l, max_l, n))/3
          n *= 2
     print('integral:')
     print(math.fabs(integral(fun, min_l, max_l, n)))

methofrect(lambda x: eval(func), min_l, max_l, eps)

