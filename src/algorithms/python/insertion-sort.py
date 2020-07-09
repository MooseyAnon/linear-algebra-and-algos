"""Insertion sort."""


def insertion_sort(array, last):
    """Insertion sort.

    A stable in-place implementation of the insertion sort algorithm.

    :params list array: an array
    :param int last: the last index of the array (i.e the length)
    :returns: a sorted array
    :rtype: list
    """
    current = 1
    while current <= last:

        # we want to start the comparision with the item before current
        j = current - 1
        while j >= 0:
            if array[current] >= array[j]:
                break
            array[current], array[j] = array[j], array[current]

            # current has moved to the place j was previously so we need to
            # update the pointer to current
            current = j
            j -= 1

        current += 1

    return array


x = [100, 2, 5, 7, 3, 2, 2, 2, 10, 11, 0]

print(
    insertion_sort(x, len(x) - 1)
)
