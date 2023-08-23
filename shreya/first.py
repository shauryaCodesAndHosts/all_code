from typing import List


def water(arr: List[int]) -> int:
    length = len(arr)
    # check if there is enough walls to store water
    if length < 3:
        return 0

    left, right = 0, length - 1
    left_max, right_max = 0, 0
    total_water = 0
    # calculating the amount of water that can be stored (using 2 pointers method)
    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                total_water += left_max - arr[left]
            left += 1
        else:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                total_water += right_max - arr[right]
            right -= 1
    return total_water


if __name__ == "__main__":
    print(water([1, 2,3,4,5]))