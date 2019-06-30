import numpy as np


def householder(A, tolerance):
    A_ = A
    H = np.identity(len(A))
    while calculate_error(A) > tolerance:
        for i in range(len(A) - 2):
            hc = mount_hh(A_, i)
            A_ = (hc.dot(A_)).dot(hc)
            H = H.dot(hc)

    return A_, H


def mount_hh(A, i):
    v = np.zeros(len(A))
    v[i+1:len(A)] = A[i+1:len(A), i]
    l_v = np.linalg.norm(v)
    v_ = np.zeros(len(A))
    v_[i+1] = l_v
    N = v - v_
    n = N/np.linalg.norm(N)
    return np.identity(len(A)) - 2 * n.dot(np.transpose(n))


def calculate_error(A):
    sum = 0
    for i in range(len(A) - 2):
        for j in range(i+2, len(A) - 2):
            sum += abs(A[i, j])
    return sum
