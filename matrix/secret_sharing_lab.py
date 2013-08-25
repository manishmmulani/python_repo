# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from itertools import combinations


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def getRandomVector():
    return list2vec([randGF2() for i in range(6)])

def choose_secret_vector(s,t):
    while True:
        u=getRandomVector()
        if a0*u == s and b0*u == t:
            return u

def select_independent_vectors():
    def select_random_vector_pairs():
        return [(a0,b0)] + [(getRandomVector(), getRandomVector()) for i in range(4)]

    while True:
        pairs = select_random_vector_pairs()
        if all([is_independent(list(sum(x,()))) for x in combinations(pairs, 3)]):
            return pairs

s=select_independent_vectors()

## Problem 2
# Give each vector as a Vec instance
secret_a0 = s[0][0]
secret_b0 = s[0][1]
secret_a1 = s[1][0]
secret_b1 = s[1][1]
secret_a2 = s[2][0]
secret_b2 = s[2][1]
secret_a3 = s[3][0]
secret_b3 = s[3][1]
secret_a4 = s[4][0]
secret_b4 = s[4][1]

