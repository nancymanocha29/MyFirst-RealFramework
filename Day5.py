#Reverse a string with split and without split()
# STR = """gjvgdu
# DUYEWGDU uygugdi
# uyegcugeyfu
# EDUGD
# EDAVEDJWA"""
#
# # list = STR.split()
# #
# # print(list)
#
# print(STR.find("x"))
# print(STR.index("x"))

# str1= "my name is Nancy"
# str2=""
# l=len(str1)-1
# for i in range(0,len(str1)):
#     str2=str2+str1[l-i]
# print(str2)

str1= "my name is Nancy"
str2 = str1[-1]+str1[-2]+str1[-3]
print(str2)
# below ode is with split()
# li = str1.split()
# ou =[]
# for item in li:
#     l= len(item)-1
#     str2=""
#     for i in range(0,len(item)):
#         str2= str2 + item[l-i]
#     ou.append(str2)
#
# str3 = " ".join(ou)
# print(str3)

#below code is without split()
# print(len(str1))
str3=""
str2=""
for i in range(0,len(str1)):
    if str1[i] !=" ":
        str2=str2+str1[i]
    if str1[i]==" " or i==len(str1)-1:
        str3=str3+" "+str2[::-1]
        # l=len(str2)
        # # print(l , str2)
        # str3=str3+" "
        # for j in range(1,l+1):
        #     # if l-j==0:
        #     #     str3 = str3 + str2[0]
        #     # else:
        #     str3=str3+str2[-j]
        # # print(str3.strip())
        str2=""
print(str3.strip())



