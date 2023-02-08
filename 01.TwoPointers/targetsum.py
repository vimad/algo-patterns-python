def pair_with_targetsum(arr, target_sum):
    low, high = 0, len(arr) - 1
    while low < high:
        if arr[low] + arr[high] == target_sum:
            return [low, high]
        elif arr[low] + arr[high] > target_sum:
            high -= 1
        else:
            low += 1

    return [-1, -1]

if __name__ == '__main__':
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
