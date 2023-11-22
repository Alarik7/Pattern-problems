# n = int(input("enter the value"))
# for i in range(n):
#     for j in range(n):
#         print("*",end='')
#     print()
# ****
# ****
# ****
# ****

# n = int(input("enter the value"))
# for i in range(0,n+1):
#     for j in range(i):
#         print("*",end='')
#     print()

# *
# **
# ***
# ****


# n = int(input("enter the value"))
# for i in range(0,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# 1
# 12
# 123
# 1234

# n = int(input("enter the value"))
# for i in range(0,n+1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

# 1
# 22
# 333
# 4444

# n = int(input("enter the value"))
# for i in range(0,n+1):
#     for j in range(n-i+1):
#         print("*",end='')
#     print()

# ****
# ***
# **
# *

# n = int(input("enter the value"))
# for i in range(0,n+1):
#     for j in range(1,n-i+1):
#         print(j,end='')
#     print()
# 12345
# 1234
# 123
# 12
# 1

# n = int(input("enter the value"))
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,2*i+1):
#         print("*", end="")
#     for j in range(0,n-i-1):
#         print(end=" ")
        
#     print()

#     *    
#    ***   
#   *****  
#  ******* 
# *********

# n = int(input("enter the value"))
# for i in range(0,n+1):
#     for j in range(i):
#         print(end=" ")
#     for j in range(0, 2*n-2*i+1):
#         print("*", end="")
#     for j in range(i):
#         print(end=" ")    
#     print()

# ***********
#  ********* 
#   *******  
#    *****   
#     ***    
#      *  

# n = int(input("enter the value"))
# for i in range(n+1):
#     if i % 2 == 0:
#         start = 1
#     else:
#         start = 0
#     for j in range(i):
#         start = 1-start
#         print(start,end="")
#     print()

# 1
# 01
# 101
# 0101
# 10101