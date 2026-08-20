# print the elements of the following list
# lists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for element in lists:
#     print(element)


# search for a number x in this tuple
# tuples = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# index = 0
# x = int(input("Enter the element to find: "))
# for element in tuples:
#     if(element == x):
#         print(x ,"at index", index)
#     index += 1
    

# for i in range(100):
#     print(i)
    
# for i in range(100, 0, -1):
#     print (i)
    

# n= int(input("Enter the number for multiplication table: "))
# for i in range(1, 11):
#     print(n * i)

# n = int(input("Enter the number: "))
# sum = 0
# i = 1
# while(i <= n):
#     sum = sum + i
#     i += 1
# print(sum)

n = int(input("Enter the number: "))
fact = 1
i = 1
while(i <= n):
    fact = fact * i
    i += 1
print(fact)
