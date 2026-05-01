# # print pattern
#
# star ="*"
# l=[]
# l1=[]
# l2=[]
#
# for i in range(1,5):
#
#     for j in range(1,i+1):
#         l.append("*")
#     for j in range(5-i,0,-1):
#         l1.append(" ")
#     for k in range(1,i):
#         l2.append("*")
#
#     print("".join(l1)+"".join(l2)+"".join(l))
#     l1=[]
#     l2=[]
#     # print("".join(l))
#     l=[]
#
#
#
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         l.append("*")
#     for j in range(5 - i, 0, -1):
#         l1.append(" ")
#     for k in range(1, i):
#         l2.append("*")
#
#     print("".join(l1) + "".join(l2) + "".join(l))
#     l1 = []
#     l2 = []
#     # print("".join(l))
#     l = []
#



# n = 7  # height of the diamond (number of rows in the top half)
#
#
# # Top half
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
#
# # Bottom half
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# Palindrom word
#
# str="Check pop is palindrome or not dad"
#
# l = str.split()
# print ({word : "Palindrome"  for word in l if word==word[::-1]})

