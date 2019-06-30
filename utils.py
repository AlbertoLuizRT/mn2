# Used to calculate error
def calculate_norm_without_diagonal(A):
    sum = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            sum += A[i, j] * A[i, j]
    return sum
