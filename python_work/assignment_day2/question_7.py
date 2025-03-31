def sum_even_odd_positions(numbers):
  """
  Calculates the sum of values at even and odd positions in a list.

  Args:
      numbers: A list of numbers.

  Returns:
      A tuple containing the sum of values at even positions 
      and the sum of values at odd positions.
  """
  even_pos_sum = 0
  odd_pos_sum = 0

  for i in range(len(numbers)):
    if i % 2 == 0:  # Even position
      even_pos_sum += numbers[i]
    else:  # Odd position
      odd_pos_sum += numbers[i]

  return even_pos_sum, odd_pos_sum


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_pos_sum, odd_pos_sum = sum_even_odd_positions(my_list)

print("Sum of values at even positions:", even_pos_sum)
print("Sum of values at odd positions:", odd_pos_sum)