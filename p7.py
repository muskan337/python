#                  FILE I/O
# PYTHON can be used to perform operations in file, basically READ and WRITE
# RAM- RAM in our computers is volatile, i.e it is removed or deleted as soon as we turn off the computer, to make it involatile, we store our work in the form of files, 
# how can we open, read , write,close, delete a file
# TEXT file: data stored in form of characters, .txt, .doc, .log
# BINARY file: not text files, .mp4, .mov, .png, .jpeg
#             OPEN, READ and CLOSE a file
# 1. open before read and write
# f = open("file_name", "mode")
#           |             |
#    sample.txt         r: read mode
#    demo.docx          w: write mode
# f = open("demo.txt", "r")

# data = f.read() # reads an entire file
# print(data)
# print(type(data))

# we can combine two modes like 
# f = open("demo.txt", "rt") but in text files, it is not necessary to write rt , it will by default open text file but in case of binary files we have to write rb like                                                    f = open("demo.txt", "r")
# 'r', 'w', 'x', 'a', 'b', 't', '+'
#also,

# data_new = f.read(5) # to read a few characters
# print(data_new)
# f.close()

# data = f.read()
# print(data)   it will not read line by line , to read line by line we need to close the file and then reopen it to read line by line

# line1 = f.readline() # to read a file line by line
# print(line1)

# line2= f.readline()
# print(line2)

# f.close()
# terminal shows an extra empty line because when a line ends a "\n" character comes which we can't see , file reads that character due to which a next line comes 

#     WRRITE AND APPEND
# f = open ("demo.txt","a") #to append
# # f = open ("demo.txt","w") #to write
# f.write("then I will learn react.js")
# f.close()

# f = open("sample.txt")

# f.close()

# f = open("demo.txt", "r+")
# f.write("abc") #overwrite at the starting of the file
# print(f.read()) #starts reding fromm the end of the pointer
# f.close()

# f = open("demo.txt", "w+")
# f.write("abc") it truncates the file first, then write
# print(f.read())  
# f.close()

# f = open("demo.txt", "a+")
# print(f.read())  
# f.write("abc")
# f.close()

# with open("demo.txt", "r") as f:
#   data = f.read()
#   print(data)


# with open("demo.txt", "w") as f:
#   f.write("new data")

# import os
# os.remove("sample.txt")

# with open("practice.txt", "r") as f:
#     data = f.read()

# print(data.replace("JAVA", "PYTHON"))

# with open("practice.txt", "w") as f:
#     f.write(data.replace("JAVA", "PYTHON"))

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find("learning") != -1):
#         print("found")
#     else:
#         print("not found")


# with open("practice.txt", "r") as f:
#     data = f.read()
    
#     num = data.split(",")
#     count = 0
#     for val in num:
        
#         if(int(val) % 2 == 0):
#             count += 1

# print(count)

with open("practice.txt", "r") as f:
    data = f.read()

num = data.split(",")  # ← comma AND space

count = 0

for val in num:
    val = val.strip()
    if val == "":
        continue
    if int(val) % 2 == 0:
        count += 1

print(count)
