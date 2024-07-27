from numpy import ndarray
from program2 import get_matrix


def do_transpose(matrix: ndarray) -> ndarray:
    """
    Transpose a matrix

    Parameters
    ----------
    matrix: ndarray
        The matrix to transpose

    Returns
    -------
    ndarray
        The transposed matrix
    """
    return matrix.T


if __name__ == "__main__":
    matrix = get_matrix("")

    transposed = do_transpose(matrix)
    print("Transposed matrix is:")
    print(transposed)
