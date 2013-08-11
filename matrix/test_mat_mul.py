from GF2 import one
from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import *
from hw3 import *
from ecc_lab import G,encoding_1001, R, H, find_error,non_codeword,P,s,C,CTILDE
from bitutil import *

print(G)
print(list2vec(encoding_1001))
print(R*list2vec(encoding_1001))
print(R*G)
print(H*G)
print("0,1,2 -> 0:1" + str(find_error(Vec({0,1,2}, {2:one}))))

#print(P)
print("len(P) : " + str(len(P.D[0])) + "*" + str(len(P.D[1])))
print("No. of bits before : " + str(len(str2bits(s))))
E_P = P + noise(P, 0.02)
print(bits2str(mat2bits(E_P)))
print("No. of bits after : " + str(len(mat2bits(C))))
print(bits2str(mat2bits(R*CTILDE)))
#c_ = non_codeword
#print("c_" + str(c_))
#e = find_error(H*c_)
#print("error vector e : " + str(e))
#c = c_ + e
#print("code word : " + str(c))
#print("original : " + str(R*c))

#print(H*c)

#rowlabels = {0, 1}
#collabels = {0, 1}
#matdict = {(0,0):3, (0,1):4,
#           (1,0):2, (1,1):1}
#mat = Mat((rowlabels, collabels), matdict)
#print(str(lin_comb_mat_vec_mult(mat,vec)))
#print(mat)
#print(dot_prod_mat_mat_mult(mat, mat))

#3x + 4y = 0
#2x + y = 1

#8x + 4y = 4
#5x = 4
#x= 4/5
#3,5,6,7 bits
#0 0 1 0 0 0 0   0 1 1 1 1 0 0
#0 0 0 0 1 0 0
#0 0 0 0 0 1 0
#0 0 0 0 0 0 1


#y = -3/5
#print(solving_systems_m)
#AB = solving_systems_m*mat
#BA = mat*solving_systems_m
#print(AB)
#print(BA)
