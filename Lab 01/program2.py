import numpy as np
from numpy import ndarray


def get_matrix(name: str) -> ndarray:
    """
    Get a matrix from the user

    Parameters
    ----------
    name: str
        The name of the matrix

    Returns
    -------
    matrix: ndarray
        The matrix entered by the user as a numpy array
    """
    print(f"Please enter matrix {name} - ")

    matrix = np.array([])
    while row := input():
        row = np.array(row.split(), dtype=int)
        matrix = np.vstack((matrix, row)) if matrix.size else np.array([row])

    return matrix


def multiply_matrices(matrix1: ndarray, matrix2: ndarray) -> ndarray:
    """
    Multiply two matrices

    Parameters
    ----------
    matrix1: ndarray
    matrix2: ndarray
        The two matrices to multiply

    Returns
    -------
    ndarray
        The product of the two matrices
    """
    try:
        return np.matmul(matrix1, matrix2)
    except ValueError:
        raise ValueError("The matrices cannot be multiplied") from None


if __name__ == "__main__":
    matrix1 = get_matrix("1")
    matrix2 = get_matrix("2")

    result = multiply_matrices(matrix1, matrix2)
    print("Product of the matrices is:")
    print(result)
