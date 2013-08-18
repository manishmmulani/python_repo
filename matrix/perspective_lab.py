from image_mat_util import *

from matutil import rowdict2mat,mat2coldict,coldict2mat
from mat import Mat
from vec import Vec

from solver import solve

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'}, {key:(1.0*value)/v['y3'] for key,value in v.f.items()})

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1, ('y3','x2'):w1*x2, ('y3','x3'):w1, ('y1','x1'):-x1, ('y1','x2'):-x2, ('y1','x3'):-1})
    v = Vec(domain, {('y3','x1'):w2*x1, ('y3','x2'):w2*x2, ('y3','x3'):w2, ('y2','x1'):-x1, ('y2','x2'):-x2, ('y2','x3'):-1})
    return [u, v]

w = Vec({(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}, {('y1','x1'):1})
b = Vec(set(range(9)), {8:1})
def getL():
    xarray = [(358, 36), (329, 597), (592, 157), (580, 483)]
    warray = [(0,0), (0,1), (1,0), (1,1)]
    pairlist = [make_equations(x1,x2,w1,w2) for (x1,x2),(w1,w2) in zip(xarray, warray)]
    mymap = {}
    for i in range(len(pairlist)):
        mymap[2*i]=pairlist[i][0]
        mymap[2*i+1]=pairlist[i][1]
    mymap[8]=w
    return rowdict2mat(mymap)

L = getL()
#print(L)

h=solve(L,b)
#print(h)

## Task 3
H = Mat(({'y1','y2','y3'},{'x1','x2','x3'}), h.f)
#print(H)

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    return coldict2mat({key:move2board(vec) for key, vec in mat2coldict(Y).items()})
