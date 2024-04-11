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
    N_f1_f2 = (x_list[0] - v_A) * (x_list[0] - v_B)
    max_N = N_f1_f2 
    max_x = x_list[0]
    max_y = y_list[0]
    for x, y in zip(x_list, y_list):
        N_f1_f2 = (x - v_A) * (y - v_B)
        if (N_f1_f2 > max_N):
            max_N = N_f1_f2
            max_x = x 
            max_y = y 
    return max_x, max_y, max_N
            