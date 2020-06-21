

def binary_search(array, first, last, item, steps=0):
    """A recursive binary search.

    :param list array: a sorted list to search
    :param int first: the index of the first item. During the first
        iteration this will be set to 0 but may change during the search
    :param int last: the index of the last element. During the first
        iteration this will be set to n-1 but may change during the search
    :param int item: the item to look for. This binary search assumes the
        list is an integer/float list.
    :param int steps: the number of recursive steps the search took.
        Purely for statistical uses.

    :returns: the index of the item or -1, and the number of steps it took to
        do the search.
    :rtype: tuple(int, int)
    """

    steps += 1
    middle = (last + first) // 2

    if last >= first:

        if array[middle] == item:
            return middle, steps

        if item > array[middle]:
            return binary_search(array, middle + 1, last, item, steps=steps)
        else:
            return binary_search(array, first, middle - 1, item, steps=steps)

    else:
        return -1, steps


# ------------------- tests ----------------

x = range(1049)

assert binary_search(x, 0, len(x) - 1, 256)[0] != -1
assert binary_search(x, 0, len(x) - 1, 1)[0] != -1
assert binary_search(x, 0, len(x) - 1, 1048)[0] != -1
assert binary_search(x, 0, len(x) - 1, 0)[0] != -1
assert binary_search(x, 0, len(x) - 1, 100)[0] != -1
assert binary_search(x, 0, len(x) - 1, 750)[0] != -1
assert binary_search(x, 0, len(x) - 1, 512)[0] != -1
assert binary_search(x, 0, len(x) - 1, 1000)[0] != -1
assert binary_search(x, 0, len(x) - 1, 1050)[0] == -1
assert binary_search(x, 0, len(x) - 1, 2000)[0] == -1
assert binary_search(x, 0, len(x) - 1, -8)[0] == -1

# ---------------------


def find_col_peak(two_d_array, col):
    """Find a column peak in a given 2D list.

    :param two_d_array: a 2D list
    :type: list[list[int]]
    :param int col: the column number to seach

    :returns: a tuple of colum max index and column max value
    :rtype: tuple(int, int)
    """
    col_max_value = two_d_array[0][col]
    col_max = 0
    for row in range(1, len(two_d_array)):
        new_number = two_d_array[row][col]
        if new_number > col_max_value:
            col_max_value = new_number
            col_max = row

    return col_max, col_max_value


def peak_finder(two_d_array, first_column, last_column):
    """A recursive 2D peak finder.

    :param two_d_array: a 2D list
    :type: list[list[int]]
    :param int first_column: the first column of the matrix, intially set to 0
    :param int last_column: the last column of the matrix, initally set to n-1

    :return: a vector of x, y coordinates of the peak (column, row)
    :rtype: tuple(int, int)
    """

    middle_column = last_column // 2
    row, item = find_col_peak(two_d_array, middle_column)

    # if we are in the first or last row then that column max will ve a local
    # maximum
    if middle_column == first_column or middle_column == last_column:
        return middle_column, row

    if last_column > first_column:

        # if we find peak
        if (two_d_array[row][middle_column - 1]
            <= item >= two_d_array[row][middle_column + 1]):
            return middle_column, row

        if two_d_array[row][middle_column - 1] > item:
            return peak_finder(two_d_array, first_column, middle_column - 1)

        else:
            return peak_finder(two_d_array, middle_column + 1, last_column)

    return middle_column, row


arr = [
    [10, 8, 10, 10, 16],
    [14, 13, 12, 11, 24],
    [15, 9, 11, 21, 6],
    [16, 21, 19, 20, 12],
    [100, 6, 13, 19, 9]
]

print(peak_finder(arr, 0, len(arr) - 1))
