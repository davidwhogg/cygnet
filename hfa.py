"""
This file is part of the cygnet project.
Copyright 2017 David W. Hogg and Anna-Christina Eilers.

# hfa.py
Heteroskedastic factor analysis

# comments
Assumes that individual-datum covariance matrices are all diagonal.
Could easily be generalized to take an arbitrary covariance matrix for
every datum.

# bugs
- Not yet written.
- Not tested at all.
"""
import numpy as np

def Estep(data, ivars, mu, W):
    """
    Presumes that each entry in ivars is the diagonal of a diagonal matrix!
    """
    return x_means, x_ivars

def Mstep(data, x_means, x_ivars):
    return mu, W

def initialize(data, ivars, K):
    """
    Presumes that each entry in ivars is the diagonal of a diagonal matrix!
    """
    return mu, W

def objective(data, ivars, mu, W):
    """
    Presumes that each entry in ivars is the diagonal of a diagonal matrix!
    """
    return -0.5 * stuff

def train(data, ivars, K):
    """
    Presumes that each entry in ivars is the diagonal of a diagonal matrix!
    """
    N, D = data.shape
    assert ivars.shape == (N, D)
    mu, W = initialize(data, ivars, K)
    converged = False
    obj = np.Inf
    while not converged:
        x_means, x_ivars = Estep(data, ivars, mu, W)
        mu, W = Mstep(data, x_means, x_ivars)
        new_obj = objective(data, ivars, mu, W)
        if new_obj > obj:
            raise ValueError("objective got worse")
        if new_obj > (obj - tiny):
            converged = True
        obj = new_obj
    return mu, W
