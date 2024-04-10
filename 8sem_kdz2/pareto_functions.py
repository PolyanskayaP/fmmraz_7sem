import numpy as np

def pareto_mu_max(f1, f2, t1, t2):
    if (f1 == t1) and (f2 == t2):
        return 1
    elif (t1 < f1) and (t2 < f2) or (t1 == f1) and (t2 < f2) or (t1 < f1) and (t2 == f2):
        return -1
    else:
        return 0

def pareto_mu_min(f1, f2, t1, t2):
    if (f1 == t1) and (f2 == t2):
        return 1
    elif (t1 > f1) and (t2 > f2) or (t1 == f1) and (t2 > f2) or (t1 > f1) and (t2 == f2):
        return -1
    else:
        return 0

def find_pareto(df1, df2, WE_FIND): # df1 df2 это дф-столбцы
    f1_ar = df1.tolist()
    f2_ar = df2.tolist()
    kolvo = df1.shape[0]
    tabl = []
    for f1, f2 in zip(f1_ar, f2_ar):
        inc = 0
        el = [0 for i in range(kolvo)]
        tabl.append(el)
        for t1, t2 in zip(f1_ar, f2_ar):
            pmm = 0
            if WE_FIND == "MAX":
                pmm = pareto_mu_max(f1, f2, t1, t2)
            elif WE_FIND == "MIN":
                pmm = pareto_mu_min(f1, f2, t1, t2)
            if (len(tabl)==1):
                tabl[len(tabl)-1][inc] = pmm
            elif (tabl[-2][inc] != -1):
                tabl[len(tabl)-1][inc] = pmm
            elif (tabl[-2][inc] == -1):
                tabl[len(tabl)-1][inc] = -1
            inc = inc + 1
    Tabl = np.array(tabl)
    pare_idx = []
    not_pare_idx = []
    for i, q in enumerate(Tabl[-1], start=0):
        if (q==-1):
            not_pare_idx.append(i)
        else:
            pare_idx.append(i)
    return(pare_idx, not_pare_idx)