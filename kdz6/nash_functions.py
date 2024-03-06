import numpy as np
i1 = 0
i2 = 1 

def nash(A, B): #A = np.array([[5,3],[3,8]])
    C = A[i1][i1] - A[i2][i1] - A[i1][i2] + A[i2][i2]
    alpha = A[i2][i2] - A[i1][i2]
    D = B[i1][i1] - B[i2][i1] - B[i1][i2] + B[i2][i2]
    beta = B[i2][i2] - B[i2][i1]
    
    #print(ner12_p1(C, alpha))
    #print(ner12_p0(C, alpha))
    #print(ner12_p01(C, alpha))
    #print(ner34_q1(D, beta))
    #print(ner34_q0(D, beta))
    #print(ner34_q01(D, beta))
    #p0_N, p1_N, q0_N, q1_N = N_dot(C, alpha, D, beta)
    
    fA_N, fB_N = fAB_N(A, B,  C, alpha, D, beta)

def neravenstva(C, alpha, D, beta):
    pass

def ner12_p1(C, alpha):
    q0 = alpha / C 
    q1 = 1
    p = 1
    return p, [q0, q1]

def ner12_p0(C, alpha):
    q0 = 0
    q1 = alpha / C 
    p = 0
    return p, [q0, q1]

def ner12_p01(C, alpha):
    q = alpha / C 
    p0 = 0
    p1 = 1
    return q, [p0, p1]

def ner34_q1(D, beta):
    p1 = beta / D
    p0 = 1
    q = 1
    return q, [p0, p1]

def ner34_q0(D, beta):
    p1 = 0
    p0 = beta / D
    q = 0
    return q, [p0, p1]

def ner34_q01(D, beta):
    p = beta / D
    q0 = 0
    q1 = 1
    return p, [q0, q1]

def N_dot(C, alpha, D, beta): 
    p0 = beta / D
    p1 = 1 - p0
    q0 = alpha / C 
    q1 = 1 - q0
    return p0, p1, q0, q1

def fAB_N(A, B,  C, alpha, D, beta):
    p0, p1, q0, q1 = N_dot(C, alpha, D, beta)
    fA = np.dot ( np.dot([p0, p1] , A) , np.array([[q0],[q1]]))
    fB = np.dot ( np.dot([p0, p1] , B) , np.array([[q0],[q1]]))
    return list(fA)[0], list(fB)[0]
    
A = np.array([[5,3],[3,8]])  #7 вариант
B = np.array([[5,15],[20,5]]) 
nash(A, B)