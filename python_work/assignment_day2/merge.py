def merge_alternatively(str1, str2):
    """
    Merges two strings alternatively.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        The merged string.
    """

    merged_str = ""
    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        merged_str += str1[i] + str2[i]

    
    merged_str += str1[min_len:] + str2[min_len:]

    return merged_str


str1 = "Bhima"
str2 = "ABCDEOLM"
merged_str = merge_alternatively(str1, str2)
print("Merged string:", merged_str)  # Output: BAhiBmCaDeEOLM