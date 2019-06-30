import numpy as np
from utils import calculate_norm_without_diagonal


def jacobi_transformation(A, tolerance):
    error = np.inf
    count = 0
    A_ = A
    p = np.identity(len(A))
    while tolerance < error and count < 10000:
        for j in range(len(A)-1):
            for i in range(j+1, len(A)):
                pij = calculate_pij_jacobi(A_, i, j)
                A_ = np.dot(np.transpose(pij).dot(A_), pij)
                p = np.dot(p, pij)
        error = calculate_norm_without_diagonal(A)
        count += 1
    print('jacobi_matrix:\n', p)
    print('A matrix:\n', A_)
    print('\n')
    return p, A_


def calculate_pij_jacobi(A, i, j):
    pij = np.identity(len(A))
    if A[j, j] - A[i, i] == 0:
        theta = np.pi/4
    else:
        theta = 0.5 * np.arctan((2*A[i, j])/(A[j, j] - A[i, i]))
    pij[i, i] = np.cos(theta)
    pij[j, j] = np.cos(theta)
    pij[i, j] = np.sin(theta)
    pij[j, i] = -np.sin(theta)
    return pij

