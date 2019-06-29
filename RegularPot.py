import numpy as np


def potency(A, tolerance, X):
    lambda_new = 0
    x_old = X/np.linalg.norm(X)
    while True:
        lambda_old = lambda_new
        y_new = A.dot(x_old)
        x_new = y_new/np.linalg.norm(y_new)
        lambda_new = np.transpose(x_old).dot(y_new)
        x_old = x_new
        if lambda_new - lambda_old/lambda_new < tolerance:
            break
    return lambda_new, x_new
