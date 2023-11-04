from scipy.optimize import linprog
import numpy as np
import pandas as pd
from pprint import pprint
import sys
#прямая задача

c = [1, 1]   #коэффициенты целевой функции (ЕСЛИ ПРИДЕЛАТЬ К НИМ МИНУС, ТО НАХОДИТ МАКСИМУМ, НО ТОГДА НАЙДЕННОЕ ЗНАЧЕНИЕ F НАДО БУДЕТ ПОТОМ УМНОЖИТЬ НА -1)
A = [[-5,-1],[-4,-1],[-2,-5],[-2,-7]]  #коэффициенты у переменных в ограничениях (ВСЕ ОГРАНИЧЕНИЯ ДОЛЖНЫ БЫТЬ СО ЗНАКОМ МЕНЬШЕ ИЛИ РАВНО <=)
b = [-1,-1,-1,-1]  #свободные
og_x1 = None #(0, 92) #ограничения по x1 x2, которые в конце, одиночные #если нет, пишем None
og_x2 = None #(0, 69)

res = linprog(c, A_ub=A, b_ub=b, bounds=(og_x1,og_x2)) #, method='simplex', options={"disp": True})  #МИНИМУМ ИЩЕМ
#print(res)
#print("X: ",res.x, res.ineqlin.residual)
#print("Y: ","0 0",res.ineqlin.marginals * -1)

x1 = res.x[0]
x2 = res.x[1]
x3 = res.ineqlin.residual[0]
x4 = res.ineqlin.residual[1]
x5 = res.ineqlin.residual[2]
x6 = res.ineqlin.residual[3] 

#y5 = 0
#y6 = 0
y5 = res.lower.marginals[0] #* -1
y6 = res.lower.marginals[0] #* -1
y1 = res.ineqlin.marginals[0] * -1
y2 = res.ineqlin.marginals[1] * -1
y3 = res.ineqlin.marginals[2] * -1
y4 = res.ineqlin.marginals[3] * -1

arr = np.array([
       [x1, x2, x3, x4, x5, x6],
       ["x1", "x2", "x3", "x4", "x5", "x6"],
       ["y5", "y6", "y1", "y2", "y3", "y4"],
       [y5, y6, y1, y2, y3, y4]])

df = pd.DataFrame(data=arr)

d_x = {"x1": x1, "x2": x2, "x3": x3, "x4": x4, "x5": x5, "x6": x6}
d_y = {"y1": y1, "y2": y2, "y3": y3, "y4": y4, "y5": y5, "y6": y6}

print('\n')
print(df.to_string(index=False))
#print(df.to_csv(header=None,index=False))
print('\n')
pprint(d_x)
print('\n')
pprint(d_y)
print('\n')

u = 1 / (x1 + x2)
u = 1 / (y1 + y2 + y3 + y4)
p1 = x1 * u
p2 = x2 * u
q1 = y1 * u
q2 = y2 * u
q3 = y3 * u
q4 = y4 * u 

print("Решение игры:")
print("p1* = ", p1,"; ", "p2* = ", p2)
print("q1* = ", q1,"; ", "q2* = ", q2,"; ", "q3* = ", q3,"; ", "q4* = ", q4)
print("u =", round(u))
