def remove_duplicates(arr):
    next_non_duplicate_index = 1

    for i in range(0, len(arr)):
        if arr[next_non_duplicate_index - 1] != arr[i]:
            arr[next_non_duplicate_index] = arr[i]
            next_non_duplicate_index += 1

    return arr


if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
