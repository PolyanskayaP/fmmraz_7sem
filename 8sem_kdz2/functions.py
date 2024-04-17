import numpy as np
from random import random

def find_konus_idxs_max(x_list, y_list, sq_x, sq_y):
    v_kon_x = []
    v_kon_y = []
    ne_kon_x = []
    ne_kon_y = []
    for x, y in zip(x_list, y_list):
        if (x >= sq_x and y >= sq_y ):
            v_kon_x.append(x)
            v_kon_y.append(y)
        else:
            ne_kon_x.append(x)
            ne_kon_y.append(y)
    return v_kon_x, v_kon_y, ne_kon_x, ne_kon_y

def find_fun_Nash(x_list, y_list, v_A, v_B):
    N_f1_f2 = (x_list[0] - v_A) * (y_list[0] - v_B)
    max_N = N_f1_f2 
    max_x = x_list[0]
    max_y = y_list[0]
    for x, y in zip(x_list, y_list):
        N_f1_f2 = (x - v_A) * (y - v_B)
        if (N_f1_f2 > max_N):
            max_N = N_f1_f2
            max_x = x 
            max_y = y 
    print("max_N_fun = ", max_N)
    return max_x, max_y, max_N

def Nash_1(v_A, v_B, pg, qg):
    #pass
    f1zv = v_A
    f2zv = v_B
    A = np.array([[5,3],[3,8]])  #7 вариант
    B = np.array([[5,15],[20,5]]) 
    f1 = gener_f1(p,q)
    f2 = gener_f2(p,q) 
    N_f1_f2 = (f1 - f1zv) * (f2 - f2zv)

def gener_f1(pp, qq):
    A = np.array([[5,3],[3,8]])  #7 вариант
    B = np.array([[5,15],[20,5]]) 
    f1 = np.dot ( np.dot(pp , A) , qq)
    return f1

def gener_f2(pp, qq):
    A = np.array([[5,3],[3,8]])  #7 вариант
    B = np.array([[5,15],[20,5]]) 
    f2 = np.dot ( np.dot(pp , B) , qq)
    return f2
    
#################
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

def gener_f1_f2_N (n, f1zv, f2zv, p_zvA, p_zvB):
    A = np.array([[5,3],[3,8]])  #7 вариант
    B = np.array([[5,15],[20,5]]) 
    p, q = gener_p_q(n)
    p = np.array(p)
    q = np.array(q)
    list_f_1_2 = []
    list_N_f = []
    for i in range(n - int(n/2)):
        pp = np.array([[p[i], 1-p[i]]]) #в 1 случае меняем p
        qq = np.array([[0.6],[0.4]]) #во 2 случае q
        #qq = np.array([ [p_zvB[0]], [p_zvB[1]] ]) 
        f1 = np.dot ( np.dot(pp , A) , qq)
        f2 = np.dot ( np.dot(pp , B) , qq)
        N_f1_f2 = (f1 - f1zv) * (f2 - f2zv)
      #  print(f1, f2, f1zv, f2zv)
        list_f_1_2.append([f1[0][0], f2[0][0]])
        list_N_f.append(N_f1_f2)
        #print("f1:", f1[0][0], " f2:", f2[0][0])
    for i in range(n - int(n/2)):
        pp = np.array([[0.713, 0.287]]) #в 1 случае меняем p
        #pp = np.array([[p_zvA]])
        qq = np.array([[q[i]],[1-q[i]]]) #во 2 случае q
        f1 = np.dot ( np.dot(pp , A) , qq)
        f2 = np.dot ( np.dot(pp , B) , qq)
        N_f1_f2 = (f1 - f1zv) * (f2 - f2zv)
        #print(f1, f2, f1zv, f2zv)
        list_f_1_2.append([f1[0][0], f2[0][0]])
        list_N_f.append(N_f1_f2)
        #print("f1:", f1[0][0], " f2:", f2[0][0])
    return list_N_f #np.array(list_f_1_2)
        
            