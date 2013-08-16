from mat import Mat
from vec import Vec
from geometry_lab import identity, translation, scale, rotation, grayscale, reflect_about
from matutil import coldict2mat, mat2coldict
from image_mat_util import file2mat, mat2display
import math

pos_mat, color_mat = file2mat('cit.png')

coldict = mat2coldict(pos_mat)
#coldict = {colkey : identity * colvec for colkey, colvec in coldict.items()}
#coldict = {colkey : translation(200,200) * colvec for colkey, colvec in coldict.items()}
#coldict = {colkey : scale(2,4) * colvec for colkey, colvec in coldict.items()}
#coldict = {colkey : rotation(math.pi/30) * colvec for colkey, colvec in coldict.items()}
#coldict = {colkey : reflect_about((0,0),(1,1)) * colvec for colkey, colvec in coldict.items()}
#coldict = {colkey : reflect_about((0,400),(1,400)) * colvec for colkey, colvec in coldict.items()}
#coldict = {colkey : reflect_about((0,400),(400,0)) * colvec for colkey, colvec in coldict.items()}
pos_mat1 = coldict2mat(coldict)

colormat_coldict = {colkey : grayscale()*colvec for colkey, colvec in mat2coldict(color_mat).items()}
color_mat1 = coldict2mat(colormat_coldict)
#color_mat1=color_mat
mat2display(pos_mat1, color_mat1)
input("press enter to exit")


#1,0 cos30, sin30
#0,1 -sin30, cos30
#0,0 0,0

#t=theta
#r,t
#rcos(30+t), rsin(30+t)
#r{cos30 * cost - sin30 * sint}, r{sin30 * cost + cos30 * sint}
#cos30 * x - sin30 * y, x * sin30 + y * cos30

