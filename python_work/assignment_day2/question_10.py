def find_subarray_with_sum(arr, n, sum):
   
    curr_sum = arr[0]
    start = 0

    for i in range(1, n):
       
        while curr_sum > sum and start < i:
            curr_sum -= arr[start]
            start += 1

        
        if curr_sum == sum:
            return start, i - 1

        
        if i < n:
            curr_sum += arr[i]

    
    return -1, -1


arr = [1, 4, 0, 0 , 3, 10, 5]
n = len(arr)
sum = 7

start, end = find_subarray_with_sum(arr, n, sum)

if start != -1:
    print("Subarray found between index", start, "to", end)
else:
    print("No subarray found")