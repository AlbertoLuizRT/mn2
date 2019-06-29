import numpy as np
from utils import calculate_norm_without_diagonal


def jacobi_transformation(A, tolerance):
    j = np.identity(len(A))  # Change to HH matrix, if provided
    error = np.inf
    count = 0
    while tolerance < error and count < 10000:
        p = np.identity(len(A))
        for j in range(len(A)-1):
            for i in range(j+1, len(A)):
                pij = calculate_pij_jacobi(A, i, j)
                A = np.dot(np.dot(np.transpose(pij), A), pij)
                p = np.dot(p, pij)
        count += 1
        j = np.dot(j, p)
        error = calculate_norm_without_diagonal(A)
    return j, A


def calculate_pij_jacobi(A, i, j):
    pij = np.identity(len(A))
    if A[j][j] - A[i][i] == 0:
        theta = np.pi/4
    else:
        theta = 0.5 * np.arctan((2*A[i][j])/(A[j][j] - A[i][i]))
    pij[i][i] = np.cos(theta)
    pij[j][j] = np.cos(theta)
    pij[i][j] = np.sin(theta)
    pij[j][i] = -np.sin(theta)
    return pij

