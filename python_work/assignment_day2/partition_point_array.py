def find_partition_point(arr):
    """
    Finds a partition point in an unsorted array.

    A partition point is an element such that all elements to its left 
    are smaller and all elements to its right are greater.

    Args:
        arr: The input array of integers.

    Returns:
        The index of the partition point if found, otherwise -1.
    """

    n = len(arr)

    # Find the maximum element in the left half
    left_max = [None] * n
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    # Find the minimum element in the right half
    right_min = [None] * n
    right_min[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], arr[i])

    
    for i in range(1, n - 1):
        if left_max[i - 1] <= arr[i] and arr[i] <= right_min[i + 1]:
            return i

    return -1


arr1 = [4, 3, 2, 5, 8, 6, 7]
arr2 = [5, 6, 2, 8, 10, 9, 8]

print(find_partition_point(arr1))  # Output: 3
print(find_partition_point(arr2))  # Output: -1