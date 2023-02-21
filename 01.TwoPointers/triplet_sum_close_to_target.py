# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number
# as possible, return the sum of the triplet. If there are more than one such triplet,
# return the sum of the triplet with the smallest sum.
import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    result = math.inf

    for i in range(len(arr)):
        left, right = i + 1, len(arr) - 1
        while left < right:
            diff = target_sum - (arr[i] + arr[left] + arr[right])
            if diff == 0:
                return target_sum

            if abs(diff) < abs(result) or (abs(diff) == abs(result) and diff > result):
                result = diff

            if diff > 0:
                left += 1
            else:
                right -= 1


    return target_sum - result


if __name__ == '__main__':
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))
