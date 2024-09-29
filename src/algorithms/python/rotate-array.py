"""Rotate a give array."""

def reverse(arr: list[int], start: int, end: int) -> None:
    """Reverse an array in place."""

    while start < end:
        # swap
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1


def rotate_simple(arr: list[int], k: int) -> list[int]:
    """Pop from the back, push on the front.

    This is O(n^2) time as inserting at the front of an array shifts all the
    other value.
    """
    # we can simplify k but mod it against the number items in arr
    # this is because if k == len(arr), then we don't need to do any work
    # if k > len(arr), we shouldn't need to do multiple loops over the whole
    # list, mod will tell us the max number we need to rotate
    # e.g. arr = 5, k = 7, 5 % 7 == 2 so we only need to do updates
    k = k % len(arr)
    print(k)
    for i in range(k):
        arr.insert(0, arr.pop())

    return arr


def rotate_newarr(arr: list[int], k: int) -> list[int]:
    """Create a new array and move items over.

    O(n) time and space complexity
    """
    result: list[int] = [0 for _ in range(len(arr))]

    k = k % len(arr)
    for i in range(len(arr)):
        # we can figure out the new position of the item by adding k to the
        # current index, because we want to do k rotations. We then need to mod
        # the result by the length of the array to make sure it is still in
        # bounds
        new_position = (i + k) % len(arr)
        result[new_position] = arr[i]

    return result


def rotate_inplace(arr: list[int], k: int) -> list[int]:
    """Rotate array in place.

    O(n) time complexity
    O(1) space complexity
    """
    k = k % len(arr)
    # reverse entire list
    reverse(arr, 0, len(arr) - 1)
    # reverse first k items
    reverse(arr, 0, k - 1)
    # reverse rest of list
    reverse(arr, k, len(arr) - 1)
    # print(arr)
    return arr


x = [1, 2, 3, 4, 5]
# print(rotate_simple(x, 7))
# print(rotate_newarr(x, 7))

print(rotate_inplace([1, 2, 3, 4, 5], 7))
print(rotate_inplace([1, 2, 3, 4, 5], 1))
print(rotate_inplace([1, 2, 3, 4, 5], 3))
