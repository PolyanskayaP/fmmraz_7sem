from random import random
import numpy as np
import matplotlib.pyplot as plt
import pareto_functions as pareto
import nash_functions
import iter_brown 
import iter_model_nash

#Надо доделать равновесие Нэша (если больше 1 случая): IF-ом 0 1, у нас от 0 до 1 вообще-то!!!! 

n = 1000
#A = np.array([[1,4],[3,5]]) #6 вариант
#B = np.array([[5,2],[4,8]]) 
A = np.array([[5,3],[3,8]])  #7 вариант
B = np.array([[5,15],[20,5]]) 

def gener_p_q (n):
    #pq_list = []
    p_list = []
    q_list = []
    for i in range(n):
        p = random()
        #q = 1 - p 
        q = random()
        p_list.append(p)
        q_list.append(q)
        #pq_list.append([p, q])
    #pq_list = np.array(pq_list)
    return p_list, q_list

def gener_f1_f2 (n):
    p, q = gener_p_q(n)
    p = np.array(p)
    q = np.array(q)
    list_f_1_2 = []
    for i in range(n):
        pp = np.array([[p[i], 1-p[i]]])
        qq = np.array([[q[i]],[1-q[i]]])
        f1 = np.dot ( np.dot(pp , A) , qq)
        f2 = np.dot ( np.dot(pp , B) , qq)
        list_f_1_2.append([f1[0][0], f2[0][0]])
        #print("f1:", f1[0][0], " f2:", f2[0][0])
    return np.array(list_f_1_2)

f1f2 = gener_f1_f2(n)

pareidx, not_pareidx = pareto.find_pareto(f1f2[:,0], f1f2[:,1], "MAX")
#print(pareidx)

fA_N, fB_N = nash_functions.nash(A, B)
#print(fA_N, fB_N)

p_zvA, q_zvA, v_A = iter_brown.brown(A)
p_zvB, q_zvB, v_B = iter_brown.brown(B)
#print(v_A, v_B)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(f1f2[not_pareidx,0], f1f2[not_pareidx,1], color = 'blue', marker = '*', label='Не Парето')  #точки
ax.scatter(A, B, color = 'red', marker = '*', label='A и B')  #точки
ax.scatter(f1f2[pareidx,0], f1f2[pareidx,1], color = 'green', marker = '*', label='Парето')  #точки
#ax.scatter(fA_N, fB_N, color = 'orange', marker = '*', label='т. равн. по Нэшу')
ax.scatter(v_A, v_B, color = 'orange', marker = '*', label='S')
ax.legend()
plt.show() #