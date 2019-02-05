#!/usr/bin/python


def sort(_input):
    # sort the input array using merge sort
    merge_sort(_input)


def merge_sort(_input):
    # Spilt the array from the middle only if we have at least 2 elements in the input array.
    if len(_input) > 1:
        middle_point = len(_input)//2
        # Divide the array in two parts, the left side and the right side.
        left_side = _input[:middle_point]
        right_side = _input[middle_point:]
        # Partition on the left side of the array first till it has only 1 element, and then partition right part.
        merge_sort(left_side)
        merge_sort(right_side)
        # Merge starts when we have single element in the left and right side array, and then combines all the arrays
        # same way till we reach the top of the recursive call.
        merge(_input, left_side, right_side)


def merge(_input,left_side,right_side):
    i = 0
    j = 0
    k = 0
    print("Before merge input array ->> " + str(_input))
    print("Before merge left array ->> " + str(left_side))
    print("Before merge  right array ->> " + str(right_side))
    while i < len(left_side) and j < len(right_side):
        # Find the lowest of the right and left array and update it to the input array.
        if left_side[i] >= right_side[j]:
            _input[k] = right_side[j]
            j += 1
        else:
            _input[k] = left_side[i]
            i += 1
        k += 1

    # Add all the remaining elements of one of the array to input array.
    while i < len(left_side):
        _input[k] = left_side[i]
        i += 1
        k += 1

    while j < len(right_side):
        _input[k] = right_side[j]
        j += 1
        k += 1

    print("After merge input array ->> " + str(_input))


if __name__ == '__main__':
    _input = [10, 2, 12, 1, 5, 9, 20]
    sort(_input)
