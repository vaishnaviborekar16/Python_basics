""" Write the logic to for incrementing Squared Number-Star Pattern.
Input Format : Take N as input of type integer.
Output Format : Print incrementing Squared Number-Star Pattern.
Constraints: [DONE]
2<=N<=10
Sample Input:
5
Sample Output:
1*2*3*4*5
6*7*8*9*10
11*12*13*14*15
16*17*18*19*20
21*22*23*24*25

"""
def pattern(N):
  
  start = 1
  for i in range(N):
    for j in range(N):
      print(start, end="")
      if j < N - 1:
        print("*", end="")
      start += 1
    print()
N = int(input("enter N: "))
pattern(N)
  