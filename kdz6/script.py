from random import random
import numpy as np

n = 5
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
    #list_f_1_2 = np.array()
    for i in range(n):
        #f1 = [p[i], q[i]] * A * np.array( [[q[i]],[1-q[i]]] )
        #f2 = [p[i], q[i]] * B * np.array( [[q[i]],[1-q[i]]] )
        f1 = np.dot([p[i], q[i]], A, np.array( [[q[i]],[1-q[i]]] ))
        f2 = np.dot([p[i], q[i]], B, np.array( [[q[i]],[1-q[i]]] ))
        list_f_1_2.append([f1, f2])
        
      #  print(p[i], q[i])
      #  print(A)
      #  print(np.array( [[q[i]],[1-q[i]]] ))
    return list_f_1_2

print(gener_f1_f2(n))
