import numpy as np
from InvPot import inverted_potency


def shifted_potency(A, tolerance, X, mi):
    A_ = A - mi*np.identity(len(A))
    lambda_shifted, Xn = inverted_potency(A_, tolerance, X)
    return lambda_shifted + mi, Xn
