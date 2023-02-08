# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each
# element appears only once. The relative order of the elements should be kept the same and you should not use any extra space
# so that that the solution have a space complexity of O(1).
#
# Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.
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
