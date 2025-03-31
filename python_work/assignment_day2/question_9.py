def find_nth_number_digits(n):
   

   
    def num_k_digit_numbers(k):
        return 4**k

    k = 1
    count = 0
    while count + num_k_digit_numbers(k) < n:
        count += num_k_digit_numbers(k)
        k += 1

   
    return k


T = int(input("Enter the term to be find"))
for _ in range(T):
    N = int(input())
    print(find_nth_number_digits(N))