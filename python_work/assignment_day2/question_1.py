def insert_substring(main_string, substring, position):
 

  return main_string[:position] + substring + main_string[position:]


main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
position = int(input("Enter the position to insert the substring: "))

result = insert_substring(main_string, substring, position)
print("Resulting string:", result)