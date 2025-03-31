def count_subarrays_with_one_one(arr):
    """
    Counts the number of ways to divide a binary array into sub-arrays 
    such that each sub-array contains exactly one 1.

    """

    if not arr or arr.count(1) == 0:
        return 0

    prev_one = -1  # Index of the previous 1
    ways = 1  # Initial ways to divide

    for i in range(len(arr)):
        if arr[i] == 1:
            if prev_one != -1:
                ways *= (i - prev_one)  # Multiply ways by the number of possible splits
            prev_one = i

    return ways


arr1 = [1, 0, 1, 0, 1]
arr2 = [0, 0, 0]

print(count_subarrays_with_one_one(arr1))  # Output: 4
print(count_subarrays_with_one_one(arr2))  # Output: 0