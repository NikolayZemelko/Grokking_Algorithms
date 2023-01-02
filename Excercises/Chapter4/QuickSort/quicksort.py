array = [5, 1, 23, 55, 6, 7, 62, 123, 23, 34, 4, 6, 7, 34, 7]


def qsort(array: list) -> None:
    length = len(array)

    if length < 2:
        return array

    middle = array[int(length / 2)]
    array.pop(int(length / 2))
    lower_array = [item for item in array if item <= middle]
    bigger_array = [item for item in array if item > middle]

    return qsort(lower_array) + [middle] + qsort(bigger_array)

def main():
    print(qsort(array))

if __name__ == '__main__':
    main()
