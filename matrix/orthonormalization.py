from orthogonalization import orthogonalize,aug_orthogonalize
from math import sqrt
from vec import Vec

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return list(map(lambda v : (1.0/sqrt(v*v))*v if v*v > 1e-20 else v, orthogonalize(L)))

def adjust(v, multipliers):
	return Vec(v.D, {key:multipliers[key]*v[key] for key in v.D})

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    vstarlist, sigmalist = aug_orthogonalize(L)
    normlist = [sqrt(vec*vec) for vec in vstarlist]
    return orthonormalize(vstarlist), [adjust(sigmavec, normlist) for sigmavec in sigmalist]
