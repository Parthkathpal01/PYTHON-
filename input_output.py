# //read mode only//
# f = open("demo.txt", "r")
# read whole text
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# read upto that character including space
# data = f.read(5)

# read line by line
# line1 = f.readline()
# print(line1)
# f.close()

# //if the data is read completely once it should not print it again it only read \n 

# //write mode only(overwrite) the old data will be deleted

# f = open("demo.txt", "w")
# f.write("I am learning python")
# f.close()

# //append//
# f = open("demo.txt", "a")
# f.write(" and DSA in C++")

# f.close()

# f = open("sample.txt", "a")
# f.close()

# import os
# os.remove("sample.txt")