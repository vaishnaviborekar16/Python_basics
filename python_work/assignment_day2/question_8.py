def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_pairs(n):
  
    pairs = []
    for i in range(2, n // 2 + 1):  
        if is_prime(i) and is_prime(n - i):
            pairs.append((i, n - i))
    return pairs


number = int(input("Enter the number: "))
prime_pairs = find_prime_pairs(number)

if prime_pairs:
    print(f"Prime number pairs for {number}:")
    for pair in prime_pairs:
        print(f"{number} = {pair[0]} + {pair[1]}")
    print(f"NoofWays = {len(prime_pairs)}")
else:
    print(f"{number} cannot be expressed as the sum of two prime numbers.")