import nash_functions
#import script
import iter_brown
import random
import numpy as np
import matplotlib.pyplot as plt

#print("ыыыыы",p, q)
def it_mod(A, B, p_volna, q_volna, n):
    pp, qq = nash_functions.prosto_p_q(A, B) #p and q from неравенства Нэша
    p_zvA, q_zvA, v_A_f1_Nash = iter_brown.brown(A)
    p_zvB, q_zvB, v_B_f2_Nash = iter_brown.brown(B)
    #print("ыыы", v_A_f1_Nash, v_B_f2_Nash)
    list_a = []
    list_b = [] 
    for ind in range(n):
        #1 игрок
        j = 1
        i = 1
        q = random.uniform(0, 1)
        if (q <= qq):
            j = 1
        else:
            j = 2
        p = random.uniform(0, 1)
        if (p <= p_volna):
            i = 1
        else:
            i = 2
        a = A[i-1,j-1]
        b = B[i-1,j-1]
        #a = A[j-1,i-1]
        #b = B[j-1,i-1]
        list_a.append(a)
        list_b.append(b)
        
    ####
    list_a_II = []
    list_b_II = [] 
    for ind in range(n):
        #2 игрок
        j = 1
        i = 1
        q = random.uniform(0, 1)
        if (q <= q_volna):
            j = 1
        else:
            j = 2
        p = random.uniform(0, 1)
        if (p <= pp):
            i = 1
        else:
            i = 2
        a = A[i-1,j-1]
        b = B[i-1,j-1]
        list_a_II.append(a)
        list_b_II.append(b)
    
    fig = plt.figure()
    ax_1 = fig.add_subplot(2, 1, 1) #2   #разбивает Figure на указанное количество строк и столбцов
    #ax_3 = fig.add_subplot(2, 2, 3)   #первое - количество строк; второе - количество столбцов; третье - индекс ячейки
    #ax_2 = fig.add_subplot(2, 2, 2) 
    ax_4 = fig.add_subplot(2, 1, 2) # 2 4 3

    ax_1.set(title = '', xticks=list(range(n)), yticks=list_a) #I игрок
    #ax_3.set(title = '', xticks=list(range(n)), yticks=list_b)
    #ax_2.set(title = 'II игрок', xticks=list(range(n)), yticks=list_a_II)
    ax_4.set(title = '', xticks=list(range(n)), yticks=list_b_II)
    
    ax_1.set_xlabel('№ партии')
    ax_1.set_ylabel('значения из матрицы А')
    #ax_3.set_xlabel('№ партии')
    #ax_3.set_ylabel('значения из матрицы B')
    #ax_2.set_xlabel('№ партии')
    #ax_2.set_ylabel('значения из матрицы А')
    ax_4.set_xlabel('№ партии')
    ax_4.set_ylabel('значения из матрицы B')
    
    ax_1.scatter(list(range(n)), list_a, color = 'blue', marker = '.', label='')  #точки
    #ax_3.scatter(list(range(n)), list_b, color = 'red', marker = '.', label='')  #точки
    #ax_2.scatter(list(range(n)), list_a_II, color = 'blue', marker = '.', label='')  #точки
    ax_4.scatter(list(range(n)), list_b_II, color = 'red', marker = '.', label='')  #точки
    
    sr_ar_f1 = sum(list_a)/n
    print(sr_ar_f1, " <= ", "4.428")#v_A_f1_Nash)
    
    sr_ar_f2 = sum(list_b_II)/n
    print(sr_ar_f2, " <= ", "11")#v_B_f2_Nash)
    
    plt.show()
        
#A = np.array([[5,3],[3,8]])  #7 вариант
#B = np.array([[5,15],[20,5]]) 
#it_mod(A, B, 0.614, 0.70, 1000)