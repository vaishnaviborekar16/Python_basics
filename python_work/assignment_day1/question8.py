""" print the below print:
i/p=5
o/p:
12345
23451
34512
45123
51234
"""
def pattern(n):

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end="")
        for j in range(1, i):
            print(j, end="")
        print()
n = int(input("enter n : "))
pattern(n)