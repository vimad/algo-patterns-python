# Given an unsorted array of numbers and a target ‘key’,
# remove all instances of ‘key’ in-place and return the new length of the array.
def remove_element(arr, key):
    next_without_key = 0

    for i in range(0, len(arr)):
        if arr[i] != key:
            arr[next_without_key] = arr[i]
            next_without_key += 1
    return arr

if __name__ == '__main__':
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))
