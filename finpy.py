from sympy import Symbol, limit
import numpy as np
import pandas as pd

def FV_N(PV, r, N):
    return PV * (1 + r)**N

def FV_N_m(PV, r_s, m, N):
    return FV_N(PV, r_s/m, m*N)

def FV_N_c(PV, r_s, N):
   return PV * np.e**(r_s*N) 
   
def FV_generic(PV, r_s, m, N):
    _m = Symbol('_m')
    return PV * limit((1 + r_s/_m)**(_m*N), _m, m).evalf()

def FV_annuity(A, r, N=1):
    """
    We assume A is an ordinary annuity.
    """
    return  A * ((1 + r)**N - 1) / r
