from mat import Mat
from vec import Vec
from matutil import *
from hw3 import *

rowlabels = {0, 1}
collabels = {0, 1}
matdict = {(0,0):3, (0,1):4,
           (1,0):2, (1,1):1}
mat = Mat((rowlabels, collabels), matdict)
#print(str(lin_comb_mat_vec_mult(mat,vec)))
#print(mat)
#print(dot_prod_mat_mat_mult(mat, mat))

#3x + 4y = 0
#2x + y = 1

#8x + 4y = 4
#5x = 4
#x= 4/5

#y = -3/5
print(solving_systems_m)
AB = solving_systems_m*mat
BA = mat*solving_systems_m
print(AB)
print(BA)
