f1 = open("file1.txt","r+")

# line = f1.readline()
# lines = f1.readlines()
# print(type(lines),lines)
f1.truncate(10)
# f1.seek(10,0)
f1.write("Hello")
print(f1.tell())
f1.close()