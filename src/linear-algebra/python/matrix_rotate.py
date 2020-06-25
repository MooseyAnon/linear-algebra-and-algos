"""Rotate a matrix 90° in place.

A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

R = [
    [21, 16, 11, 6, 1],
    [22, 17, 12, 7, 2],
    [23, 18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [25, 20, 15, 10, 5],
]

idea, corners move first:
    - (0, 0) -> (0, 4),
    - (0, 4) -> (4, 4),
    - (4, 4) => (4, 0),
    - (4, 0) -> (0, 0),

then one item in (and up):
    - (0, 1) -> (1, 4),
    - (1, 4) -> (4, 3),
    - (4, 3) -> (3, 0),
    - (3, 0) -> (0, 1),

then same again for all items k in floor(matrix columns / 2):
    - (0, 2) -> (2, 4),
    - (2, 4) -> (4, 2),
    - (4, 2) -> (2, 0),
    - (2, 0) -> (0, 2)
"""

def rotate(matrix):
    """Rotate a matrix by 90°.

    This is a simple method that treats the matrix like a rubix cube
    and rotates one layer at a time for m/2 layers.

    :param matrix: an mxm matrix
    :type: list[list[int]]
    :return: a rotated matrix
    :rtype: list[list[int]]
    """

    # if the matrix is not mxm fail fast
    if len(matrix) != len(matrix[0]):
        return -1

    i = 0
    # columns and rows are the same
    cols = len(matrix) - 1
    depth = cols // 2

    while i <= depth:
        # come in one place (one up, one left)
        right = i
        left = cols - i
        for k in range(left - i):

            # get the four corners we are going to rotate
            top_right = matrix[right][right + k]
            top_left = matrix[right + k][left]
            bottom_right = matrix[left][left - k]
            bottom_left = matrix[left - k][right]

            # swap items
            matrix[right][right + k] = bottom_left
            matrix[right + k][left] = top_right
            matrix[left][left - k] = top_left
            matrix[left - k][right] = bottom_right
        i += 1
    return matrix

# ---------------- in place rotation tests --------------


A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

B = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

C = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

D = [
    [1, 2],
    [3, 4],
]

E = [[1, 2]]

F = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
]


assert rotate(A) == [
    [21, 16, 11, 6, 1],
    [22, 17, 12, 7, 2],
    [23, 18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [25, 20, 15, 10, 5],
]

assert rotate(B) == [
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4],
]

assert rotate(C) == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]

assert rotate(D) == [
    [3, 1],
    [4, 2],
]

assert rotate(E) == -1
assert rotate(F) == -1
