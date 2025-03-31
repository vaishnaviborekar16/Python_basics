#Finds the sum of the series 1+4-9+16-25+36.
def sum_of_series(n):
    sum=1
    for i in range(2,n+1):
        if i% 2  == 0:
            sum+= (i*i)  
        else:
            sum-=(i*i)
    print(sum)
sum_of_series(6)