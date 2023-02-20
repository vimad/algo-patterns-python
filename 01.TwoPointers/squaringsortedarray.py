# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

def make_squares(arr):
    start, end = 0, len(arr) - 1
    result = [0 for x in range(len(arr))]
    highest_index = len(arr) - 1

    while start < end:
        left_square = arr[end] * arr[end]
        right_square = arr[start] * arr[start]
        if left_square > right_square:
            result[highest_index] = left_square
            end -= 1
        else:
            result[highest_index] = right_square
            start += 1
        highest_index -= 1

    return result


if __name__ == '__main__':
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
