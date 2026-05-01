# No is armstring or not

# num=153
# val=0
#
# l = str(num)
#
# print(l)
# power=len(l)
#
# for i in range(0,len(l)):
#     val=val+(int(l[i])**power)
#
#
# if val== num:
#     print("number is armstrong", val)
# else:
#     print("no armstrong")
#
# output =["Armstrong" if sum(int(d)**power for d in l)==num else "no"]
# print(output)
#
# l1=(1,2,3)
# print (max(l1))
# print(len(str("499")))
# print(len(str("409").replace("0","")))
# count of zero in a range
# cnt=0
# cnt1=0
# for i in range(1,1001):
#     cnt = cnt + int(len(str(i)) - len(str(i).replace("0","")))
#     cnt1=cnt1+str(i).count("0")
#
# print(cnt , cnt1)

# sort a dictionary by key , value

# dict={"Ankush":"husband", "Nancy":"wife","Ahaan":"Son","Kiran":"mother","Narinder":"Father"}
#
# sorted_data={}
#
# sorted_data= { k: dict[k]  for k in  sorted(key for key in dict.keys())}
# print(sorted_data)

# sort of a list without sort function
# print(sorted([1,4,2,6]))

# l=[1,2,5,3,6,2]
# l2=[]
#
# temp=0
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         if l[i]<l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
# print(l)

# factorial of entered number
n=input("Enter the number")
val=int(n)
for i in range(int(n)-1,0,-1):
    val=val*i
print(val)



