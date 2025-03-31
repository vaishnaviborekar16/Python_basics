"""Q6. Write a program to Count number of ways to divide a given number in 4 parts. 
Input:
5
Output: 1
Input:
6
Output: 2
Input:
8
Output: 5"""

def countWays(n):

    counter = 0 


    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    if (i + j + k + l == n):
                        counter += 1
    return counter


n =int(input("enter n:"))
print (countWays(n))



