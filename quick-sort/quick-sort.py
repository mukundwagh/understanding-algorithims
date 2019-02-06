def _sort(_input):
    print("Input list => ", end="")
    print(" ".join([str(x) for x in _input]))
    quick_sort(_input, 0, len(_input) - 1)
    print("Sorted list => ", end="")
    print(" ".join([str(x) for x in _input]))


def quick_sort(_input, start, end):
    if end > start:
        _index_of_element = partition(_input, start, end)
        quick_sort(_input, start, _index_of_element - 1)
        quick_sort(_input, _index_of_element + 1, end)


def partition(_input, start, end):
    last_element_index = end
    pivot = _input[last_element_index]

    while start < end:
        if _input[start] > pivot:
            end = end - 1
            while _input[end] > pivot and end > start:
                end -= 1
            swap_elements(_input, start, end)
        start += 1
    swap_elements(_input, end, last_element_index)
    return end


def swap_elements(_input, index_1, index_2):
    temp = _input[index_1]
    _input[index_1] = _input[index_2]
    _input[index_2] = temp


if __name__ == '__main__':
    _input = [8, 7, 5, 3, 15, 2, 1]
    _sort(_input)
