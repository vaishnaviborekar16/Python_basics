#occurence finding in 2nd list
input_str1 = input("Enter the first list of integers (comma-separated): ")
input_str2 = input("Enter the second list of integers (comma-separated): ")


list1 = input_str1.split(",")
list2 = input_str2.split(",")
print(list1)
print(list2)

def find_occurrences(list1, list2):
 
  for num in list1:
    count = list2.count(num)
    print(f"{num}-{count}")

find_occurrences(list1, list2)