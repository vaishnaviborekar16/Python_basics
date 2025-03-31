def reverse_array(arr):
  """
  Reverses the given array in-place.

  Args:
    arr: The array to be reversed.

  Returns:
    None (the array is modified in-place).
  """

  # Two-pointer approach
  left = 0
  right = len(arr) - 1
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Example usage
my_array = [1, 2, 3, 4, 5]
reverse_array(my_array)
print("Reversed array:", my_array)  # Output: [5, 4, 3, 2, 1]