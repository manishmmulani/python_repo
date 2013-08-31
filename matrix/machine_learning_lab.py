from mat import *
from vec import *
from cancer_data import *

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, {key: 1 if u[key]>=0 else -1 for key in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    #x = A*w
    #numerator = len([key for key in x.f if b[key]*x.f[key] < 0])
    #return numerator*1.0 / len(x.D)
    # n - 2x = signum(A*w)*b
    return (len(b.D) - signum(A*w)*b)/(2.0*len(b.D))

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    return (A*w-b)*(A*w-b)

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return 2*(A*w-b)*A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w-sigma*find_grad(A,b,w)

def gradient_descent(A,b,w,signma,T):
    w_ = w
    for i in range(T):
        if i%30==0:
            print("Loss : " + str(loss(A,b,w_)))
            print("\nFraction wrong : " + str(fraction_wrong(A,b,w_)))
        w_ = gradient_descent_step(A,b,w_,signma)
    return w_

