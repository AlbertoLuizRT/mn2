# Used to calculate error
def calculate_norm_without_diagonal(A):
    sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if j == i:
                continue
            else:
                sum += A[i][j]
    return sum
