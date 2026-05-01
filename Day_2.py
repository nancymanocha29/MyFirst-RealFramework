number = 3456765766467

# ##### Input number is odd or even
# if number % 2 == 0:
#     print("number is even")
# else:
#     print("no is odd")

# #######Input no is prime or not
flag=0
for c in range(2,int(number/2)):
    # print(c)
    if number % c == 0:
        print("number is not prime and divided by" , c)
        flag=1
        break

if flag ==0:
    print("no is prime")


