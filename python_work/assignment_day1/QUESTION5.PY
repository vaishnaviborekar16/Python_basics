""" Reverse a given num [DONE]
i/p
num 12345
o/p
num 54321 """

x=int(input("x: "))
print(x)
def reverse_number(x):
  
  reversed= 0
  while x > 0:
    digit = x % 10  
    reversed = reversed * 10 + digit
    x //= 10  

  return reversed
reversed = reverse_number(x)
print("Original number:", x)
print("Reversed number:", reversed)
