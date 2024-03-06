import numpy as np 
from random import randint
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('TKAgg')

#A = np.array([[1, 4], [3, 5]])
A = np.array([[5,3],[3,8]]) 
#A = np.array([[5, 4, 2, 2], [1, 1, 5, 7]]) 
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
    print(k+1, i+1, B_cycle, alpha_k, j+1, A_cycle, beta_k, u_k)
    i = index_max_A_cycle
print("\nu =", u_k)
p_zv = p_count / col_iter 
q_zv = q_count / col_iter
print("p* =", p_zv, "\nq* =", q_zv)

x = np.arange(col_iter) + 1

fig, ax = plt.subplots()
ax.set(title='График')

ax.plot(x, u_list, color = 'blue', linewidth = 3)

ax.set_xlabel('Итерации')
ax.set_ylabel('Текущее приближение цены игры')

ratio = .3
x_left, x_right = ax.get_xlim ()
y_low, y_high = ax.get_ylim ()
ax.set_aspect ( abs ((x_right-x_left)/(y_low-y_high))*ratio)

#import matplotlib.ticker as mticker
#plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.xticks(x)

plt.show()