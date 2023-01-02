ARRAY = [2, 3, 4, 5, 6, 7, 8, 9]


def multy_map(array: list) -> list: # list of lists
    return [[multiplier * num for multiplier in array] for num in array]

# O(n*n) algorithm complexity

def main():
    print(multy_map(ARRAY))

if __name__ == '__main__':
    main()
