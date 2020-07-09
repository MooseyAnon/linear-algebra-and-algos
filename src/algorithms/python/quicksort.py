"""Various implementations of the quicksort algorithm."""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


def in_place_quicksort(array, first, last):
    """A recursive in-place quicksort.

    First and last moved as the algorithm divids up the array. They are
    essentially used as 'walled gardens' so we can restrict the area of
    the array the algorithm is sorting on each recursion.

    :param list array: an array
    :param int first: the first item of a particular subsection of the array
    :param int last: the last item of a particular subsection of the array

    :returns: a sorted array
    :rtype: list
    """
    if first < last:
        piv = quicksort_inner(array, first, last)

        # recurse
        in_place_quicksort(array, first, piv - 1)
        in_place_quicksort(array, piv + 1, last)

    return array


def swap_indexes(array, item_1, item_2):
    """Swap the values of two indexes in an array.

    :param list array: an array
    :param int item_1: the index of the first item to swap
    :param int item_2: the index of the second item to swap
    """
    array[item_1], array[item_2] = array[item_2], array[item_1]


def quicksort_inner(array, first, last):
    """Sort some subsection of an array.

    Sorts the section of the array in between first and last. Everytime
    indexes are swapped (due to the value at that index being larger/smaller
    than the pivot value) we keep a pointer to that index. This allows us to
    know the index of the last item that was smalled than the pivot.

    :param list array: an array
    :param int first: the first index of the subsection
    :param int last: the last index of the subsection

    :returns: the index of the last item that was swapped
    :rtype: int
    """
    pivot = (first + last) // 2
    counter = 0
    last_swap = 0

    # swap pivot with last index
    swap_indexes(array, pivot, last)

    while counter <= last:

        if array[counter] < array[last]:
            swap_indexes(array, counter, last_swap)
            last_swap += 1
        counter += 1

    # swap pivot with last swap
    swap_indexes(array, last_swap, last)

    return last_swap


y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(
    in_place_quicksort(y, 0, len(y) - 1)
)
