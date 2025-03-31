def reorder_string(str):
    """
    Reorders a string using the specified algorithm.

    Args:
        str: The input string.

    Returns:
        The reordered string.
    """

    result = ""
    while str:
        # Find and append smallest characters in ascending order
        smallest = min(str)
        result += smallest
        str = str.replace(smallest, "", 1)  # Remove the smallest character
        while str and all(c >= smallest for c in str):
            smallest = min(c for c in str if c > smallest)
            result += smallest
            str = str.replace(smallest, "", 1)

        # Find and append largest characters in descending order
        if str:
            largest = max(str)
            result += largest
            str = str.replace(largest, "", 1)
            while str and all(c <= largest for c in str):
                largest = max(c for c in str if c < largest)
                result += largest
                str = str.replace(largest, "", 1)

    return result


str = input("Enter the string: ")

reordered_str = reorder_string(str)
print("Reordered string:", reordered_str)