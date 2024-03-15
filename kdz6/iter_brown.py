import numpy as np 
from random import randint
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('TKAgg')

#A = np.array([[5, 15], [20, 5]]) #B 
#A = np.array([[5,3],[3,8]]) #A

#A = np.array([[5, 4, 2, 2], [1, 1, 5, 7]]) 

def brown(A):
    col_iter = 1000

    u_list = []

    i = randint(0, A.shape[0]-1)

    B_cycle = np.zeros(A.shape[1])
    A_cycle = np.zeros(A.shape[0])
    u_k = 0
    p_count = np.zeros(A.shape[0])
    q_count = np.zeros(A.shape[1])
    for k in range(col_iter):
        p_count[i] = p_count[i] + 1
        B_cycle = B_cycle + A[i]
        index_min_B_cycle = np.argmin(B_cycle)
        alpha_k = B_cycle[index_min_B_cycle] / (k+1)
        j = index_min_B_cycle
        q_count[j] = q_count[j] + 1
        A_cycle = A_cycle + A[:, j]
        index_max_A_cycle = np.argmax(A_cycle)
        beta_k = A_cycle[index_max_A_cycle] / (k+1)
        u_k = (alpha_k + beta_k) / 2 
        u_list.append(u_k)
       # print(k+1, i+1, B_cycle, alpha_k, j+1, A_cycle, beta_k, u_k)
        i = index_max_A_cycle
    #print("\nu =", u_k)
    p_zv = p_count / col_iter 
    q_zv = q_count / col_iter
    return(p_zv, q_zv, u_k)
#print("p* =", p_zv, "\nq* =", q_zv)