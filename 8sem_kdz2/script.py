from random import random
import numpy as np
import matplotlib.pyplot as plt
import pareto_functions as pareto
import nash_functions
import iter_brown 
import iter_model_nash 
import functions

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
    return np.array(list_f_1_2), p, q

f1f2, p_mass, q_mass = gener_f1_f2(n) #!!!!!!
#print(p_mass, q_mass)

pareidx, not_pareidx = pareto.find_pareto(f1f2[:,0], f1f2[:,1], "MAX")
#print(pareidx)

fA_N, fB_N = nash_functions.nash(A, B)
#print(fA_N, fB_N)

p_zvA, q_zvA, v_A = iter_brown.brown(A)
p_zvB, q_zvB, v_B = iter_brown.brown(B)
print(p_zvA, p_zvB)

v_kon_x, v_kon_y, ne_kon_x, ne_kon_y = functions.find_konus_idxs_max(f1f2[pareidx,0], f1f2[pareidx,1], v_A, v_B)
max_x, max_y, max_N = functions.find_fun_Nash(v_kon_x, v_kon_y, v_A, v_B)
print(max_x, max_y, max_N)
#v_kon_x5, v_kon_y5, ne_kon_x5, ne_kon_y5 = functions.find_konus_idxs_max(f1f2[pareidx,0], f1f2[pareidx,1], v_A, v_B)
#max_x5, max_y5, max_N5 = functions.find_fun_Nash(f1f2[0], f1f2[1], v_A, v_B)
#print(max_x5, max_y5, max_N5)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(f1f2[not_pareidx,0], f1f2[not_pareidx,1], color = 'blue', marker = '*', label='Не Парето')  #точки
ax.scatter(A, B, color = 'red', marker = '*', label='A и B')  #точки
#ax.scatter(f1f2[pareidx,0], f1f2[pareidx,1], color = 'green', marker = '*', label='Парето')  #точки
ax.scatter(v_kon_x, v_kon_y, color = 'green', marker = '*', label='Парето, конус')
ax.scatter(ne_kon_x, ne_kon_y, color = 'pink', marker = '*', label='Парето, не конус')
ax.scatter(max_x, max_y, color = 'cyan', marker = '*', label='MAX функ.Нэша')
##ax.scatter(fA_N, fB_N, color = 'orange', marker = '*', label='т. равн. по Нэшу')
ax.scatter(v_A, v_B, color = 'orange', marker = '*', label='S')
ax.legend()
plt.show() #

######list_N_f = functions.gener_f1_f2_N (n, v_A, v_B, p_zvA, p_zvB)
'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(range(n), list_N_f, color = 'blue', marker = '*', label='')  #точки
ax.scatter(max_x, max_y, color = 'cyan', marker = '*', label='MAX функ.Нэша')
ax.legend()
plt.show() #
'''
iter_model_nash.it_mod(A, B, 0.1, 0.1, 1000) #A, B, p_volna, q_volna, n # 0.6 0.714

#v_A, v_B
N_f1_f2_gar = (v_A - v_A) * (v_B - v_B)
print(N_f1_f2_gar)