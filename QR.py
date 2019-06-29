import numpy as np
from utils import calculate_norm_without_diagonal


def QR_transformation(A, tolerance):
    p = np.identity(len(A))
    error = np.inf
    count = 0
    while error > tolerance and count < 10000:
        Q, R = decompose_QR(A)
        A = R.dot(Q)
        p = p.dot(Q)
        count += 1
        error = calculate_norm_without_diagonal(A)
    return p, A  # p is the accumulated matrix, A is the diagonal matrix


def decompose_QR(A):
    Q = np.identity(len(A))
    for j in range(1, len(A)-1):
        for i in range(j+1, len(A)):
            pij = calculate_pij_QR(A, i, j)
            A = np.transpose(pij).dot(A)
            Q_t = np.transpose(pij).dot(Q)
            Q = np.transpose(Q_t)
    return Q, A  # A == R


def calculate_pij_QR(A, i, j):
    pij = np.identity(len(A))
    if A[j][j] == 0:
        theta = np.pi/2
    else:
        theta = np.arctan(A[i][i]/A[j][j])
    pij[i][i] = np.cos(theta)
    pij[j][j] = np.cos(theta)
    pij[i][j] = np.sin(theta)
    pij[j][i] = -np.sin(theta)
    return pij
