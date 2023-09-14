import math
import numpy as np;
from numpy import linalg as la

# global attributes
k_factor = 0.18


def compress(A):
    U, S, Vh = np.linalg.svd(A, full_matrices=False)
    Sigma = np.diag(S)

    # number of values / columns / rows to delete
    k = math.floor((la.matrix_rank(A)) * (1 - k_factor))

    # Modify Sigma matrix
    print("Modify Sigma matrix by deleting", k, "values\n---------------------------")
    for x in range(1, k + 1):
        Sigma[-x][-x] = 0

    # Modify U matrix
    print("Modify U matrix by deleting", k, "columns\n---------------------------")
    U = U.T
    for column in range(1, k):
        for row in range(U.shape[1]):
            U[-column][row] = 0
    U = U.T

    # Modify Vh matrix
    print("Modify V matrix by deleting", k, "Rows\n---------------------------")
    for column in range(1, k):
        for row in range(Vh.shape[1]):
            Vh[-column][row] = 0

    eval_string = "Efficiency: " + str((1 - (
            (U.shape[0] * (U.shape[1] - k) + la.matrix_rank(A) - k + (Vh.shape[0] - k) * Vh.shape[1]) * 3 / (
            A.shape[0] * A.shape[1]))) * 100) + "%"

    return U, Sigma, Vh, eval_string
