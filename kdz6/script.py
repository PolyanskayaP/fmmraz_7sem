from random import random
import numpy as np
import matplotlib.pyplot as plt

n = 50
A = np.array([[1,4],[3,5]]) 
B = np.array([[5,2],[4,8]]) 

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

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(f1f2[:,0], f1f2[:,1], color = 'blue', marker = '*')  #точки
ax.scatter(A, B, color = 'red', marker = '*')  #точки

plt.show()
