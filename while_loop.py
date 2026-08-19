# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# j = 100    
# while j >=1:
#     print(j)
#     j -= 1

# n = 3
# s = 1
# while s <= 10:
#     print(s*n)
#     s += 1

# p = 1
# while p <= 10:
#     print(p**2)
#     p += 1    

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the numbe ryou want to find: "))
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index:",i)
    i += 1