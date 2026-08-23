# with open("practice.txt", "w") as f:
#         f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

# //WAF that replace all occurrences of "Java" with "Python"  
# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("Java", "Python")
# print (new_data)  

# with open("practice.txt", "w") as f:
#     data = f.write(new_data)

# //Search if the word "learning" exists in the file or not
# def check_for_word(word):
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("NOT Found")

# check_for_word("learning")

# def check_for_line(word, line_no, data):
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
        
        
# print(check_for_line("learning", 1, True))

# def even():
count = 0
with open("practice1.txt", "r") as f:
    data = f.read()
    print(data)  
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
        