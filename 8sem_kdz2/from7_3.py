import random
import numpy as np

#A = np.array([[5, 4, 2, 2], [1, 1, 5, 7]]) 
A = np.array([[5,3],[3,8]])  #7 вариант не работает

n_konveyer = 10
sum_win_1 = 0

def rand_q2_q3():
    sluch_q2 = random.random()
    sluch_q3 = 1 - sluch_q2
    return sluch_q2, sluch_q3

def rand_q_all(): 
    q1_ = np.random.random()
    q2_ = np.random.random()
    summa = q1_ + q2_
    q1 = q1_ / summa 
    q2 = q2_ / summa
    return q1, q2

def A1(A):
    return A[0, :]

def A2(A):
    return A[1, :]

p1_zv = 0.7  #найти аналитически 
p2_zv = 0.3 
f = input("ВВОД: 1 - оптимальные q*; 2 - случайные q2,q3. q1,q4=0 ; 3 - все q*случайные ") #q*стационарные
if (f=="1"):
    #q1_zv = 0
    q2_zv = 0.5  #найти аналитически
    q3_zv = 0.5
    #q4_zv = 0
elif (f=="2"):
   # q1_zv = 0
    q2_zv, q3_zv = rand_q2_q3()
    #q4_zv = 0
elif (f=="3"):
    q1_zv, q2_zv = rand_q_all()
else: #не нужно
    #q1_zv = 0
    q2_zv = 0.5  #найти аналитически
    q3_zv = 0.5
    #q4_zv = 0
    

for i in range(n_konveyer):
    # p
    sluch_p = random.random()
    
    strat_A = []
    
    if sluch_p < p1_zv:
        strat_A = A1(A)
        print("Стратегия A1", A1(A))
    elif sluch_p >= p1_zv:  
        strat_A = A2(A)
        print("Стратегия A2", A2(A))
    
    sluch_q = random.random()  
    
    # q 
    ind_B = 1
   
    stratB = strat_A[ind_B]
    print("Стратегия B", ind_B+1, sep='')
    print(stratB, '\n')
    
    sum_win_1 += stratB

if f=="1":
    print("при оптимальных q*")
elif f=="2":
    print("при случайных q2,q3; q1,q4=0")
elif f=="3":
    print("при всех случайных q*")
print("итоговое матожидание (цена игры, выигрыш 1го игрока)", sum_win_1 / n_konveyer)   
print(q2_zv,q3_zv)#,q4_zv)     
    