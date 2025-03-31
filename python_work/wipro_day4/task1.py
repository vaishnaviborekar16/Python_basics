#Write a Python program to read a file and print its content line by line.
def read_file_line_by_line(filename):
 
  try:
    with open(filename, 'r') as file:
      for line in file:
        print(line.strip())

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

filename = 'C:\\Users\\asus\\Desktop\\python_domain\\python_work\\wipro_day4\\myfile.txt'  
read_file_line_by_line(filename)

