def can_form_strings(A, B, C):
    """
    Checks if strings A and B can be formed using all characters of string C.

    Args:
        A: The first string.
        B: The second string.
        C: The string containing characters to form A and B.

    Returns:
        "YES" if A and B can be formed using all characters of C, and C is empty afterward.
        "NO" otherwise.
    """

    # Create a dictionary to count the occurrences of each character in C
    char_count = {}
    for char in C:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if all characters of A can be formed from C
    for char in A:
        if char not in char_count or char_count[char] == 0:
            return "NO"
        char_count[char] -= 1

    # Check if all characters of B can be formed from the remaining characters in C
    for char in B:
        if char not in char_count or char_count[char] == 0:
            return "NO"
        char_count[char] -= 1

    # Check if all characters in C have been used
    for count in char_count.values():
        if count != 0:
            return "NO"

    return "YES"

# Get input strings
A = input("Enter string A ")
B = input("Enter string B ")
C = input("Enter string C ")

# Check if A and B can be formed from C
result = can_form_strings(A, B, C)

# Print the result
print(result)