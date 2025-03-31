def nth_god_number(n):
    """
    Finds the nth God number.

    Args:
        n: The index of the God number to find.

    Returns:
        The nth God number.
    """

    god_numbers = [1]  
    i = 1
    while len(god_numbers) < n:
        if i % 2 == 0:
            god_numbers.append(i * 2)
        if i % 3 == 0:
            god_numbers.append(i * 3)
        if i % 5 == 0:
            god_numbers.append(i * 5)
        i += 1

    
    god_numbers = sorted(list(set(god_numbers)))

    return god_numbers[n - 1]


n = int(input("enter the n: "))


print(nth_god_number(n))