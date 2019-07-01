from RegularPot import potency
from InvPot import inverted_potency
from ShiftedPot import shifted_potency
from HouseHolder import householder
from Jacobi import jacobi_transformation
from QR import QR_transformation
import numpy as np


def main():
    # with open("input_file.txt", "r") as input_data:
        # for i, line in enumerate(input_data):
        #     if i == 0:
        #         dimension = int(line)
        #     if i == dimension + 2:
        #         tolerance = float(line)
    A = np.matrix('42 3 6 2 9;'
                  '3 20 4 9 9;'
                  '6 4 61 8 11;'
                  '2 9 8 37 13;'
                  '9 9 11 13 54')
    initial_guess = np.transpose(np.matrix('0.8 0.20 3 2 1'))
    tolerance = 0.01

    print("Métodos de Potência e Transformações de Similaridade\n\n")
    print("Alberto Luiz Rigotto, Daneivan Rainey Cordeiro, Fernanda Soares\n")
    print("Métodos Numéricos 2, Prof. Creto Vidal\n\n\n")
    print("Selecione o Método desejado, lembrando de editar o arquivo input_file.txt com os valores desejados\n")
    option = input("1 - Potência Regular\n2 - Potência Inversa\n3 - Potência com deslocamento\n4 - Householder\n"
                   "5 - Jacobi\n6 - QR\n")
    option = int(option)
    if option == 1:
        eigenvalue, eigenvector = potency(A, tolerance, initial_guess)
    if option == 2:
        eigenvalue, eigenvector = inverted_potency(A, tolerance, initial_guess)
    if option == 3:
        shift = input("Entre com o deslocamento que deverá ser utilizado\n")
        eigenvalue, eigenvector = shifted_potency(A, tolerance, initial_guess, shift)
    if option == 4:
        householder_matrix, result_matrix = householder(A, tolerance)
    if option == 5:
        jacobi_matrix, eigenvalues = jacobi_transformation(A, tolerance)
        print_values_from_methods(eigenvalues, jacobi_matrix)
    if option == 6:
        QR_matrix, eigenvalues = QR_transformation(A, tolerance)
        print_values_from_methods(eigenvalues, QR_matrix)


# def get_values_from_matrix(A, column):
#     b = A.dot(column)
#
#     print(column)
#     proportion = b[0, 0]/column[0]
#
#     for i in range(1, len(column)):
#         new_proportion = b[0, i]/column[i]
#
#         if proportion - new_proportion > 0.1:
#             return None
#     return proportion


def print_values_from_methods(eigenvalues, eigenvectors):
    for i in range(len(eigenvectors) - 1):
        eigenvalue = eigenvalues[i, i]
        print('Eigenvector:\n', eigenvectors[:, i])
        print('Eigenvalue:', eigenvalue)
        print('\n')
    return


if __name__ == "__main__":
    main()
