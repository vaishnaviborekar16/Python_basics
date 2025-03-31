# Create a sample list
list = [1, 2, 3, 4, 5]

# List slicing
print("list:", list)

# Extract elements from index 1 to 3 (exclusive)
sliced_list = list[1:4]
print("Sliced list :", sliced_list)

# Extract elements from the beginning to index 2 (exclusive)
sliced_list = list[:3]
print("Sliced list (beginning to index 2):", sliced_list)

# Extract elements from index 3 to the end
sliced_list = list[3:]
print("Sliced list (index 3 to end):", sliced_list)

# Append a new element to the list
list.append(6)
print("List after appending 6:", list)

# Append multiple elements using 
list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", list)