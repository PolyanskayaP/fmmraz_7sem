import nash_functions
import script
import iter_brown

A = script.A
B = script.B

p, q = nash_functions.prosto_p_q(A, B) #p and q from неравенства Нэша

p_zvA, q_zvA, v_A_f1_Nash = iter_brown.brown(A)
p_zvB, q_zvB, v_B_f2_Nash = iter_brown.brown(B)