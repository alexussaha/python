from fractions import Fraction #импортируем библиотеки
from sympy import *
from matplotlib import mlab
import numpy
import math
print('Введите функцию')
func = str(input() ) #вводим функцию        
print('eps =')
eps = float(input()) #вводим точность
print('min = ')
min_l = float(input()) #yb;ybq ghtltk byntuhbhjdfybz
print('max =')
max_l = float(input()) #верхний предел интегрирования
def methofrect(fun, min_l, max_l, eps):       #функция - метод прямоуг. принимает (функция, мин. предел, макс. предел, точность)
     def integral(fun, min_l, max_l, n):      #функция - интеграл принимает значения (функция, мин. предел, макс. предел, шаг(на сколько частей делим))
          integ = 0.0                        #счётчик суммы
          step = (max_l - min_l) / n         #вычисляем шаг
          for x in numpy.arange( min_l, max_l-step, step):
               integ = integ + step * fun(x + step / 2) # вычисляем интеграл, как сумму
          return integ #возвращаем интеграл

     d, n = 1, 1
     while math.fabs(d) > eps: #Если точность разности интегралов меньше точности продолжаем
          d = (integral(fun, min_l, max_l, n * 2) - integral(fun, min_l, max_l, n))/3     # ТОЧНОСТЬ интеграл с большим шагом минус интеграл с меньшим
          n *= 2  #увеличиваем шаг в 2 раза
     print('integral:')
     print(math.fabs(integral(fun, min_l, max_l, n)))  #выводим значение интеграла с заданной точностью

methofrect(lambda x: eval(func), min_l, max_l, eps) #вызываем функцию метод прямоугольников, превращая то, что мы ввели в функкцию, готовую к исполнению 

#п.с. yb;ybq ghtltk byntuhbhjdfybz - нижний предел интегрирования
