
# not_prime_number = [1001]
# prime_flag = 0
# for c in range(1,1000):
#     # print(c)
#     for num in range(2,int(c/2)):
#         if c % num == 0:
#             prime_flag=1
#             # print(num)
#             break
#     if prime_flag == 0:
#         prime_number.append(c)
#     prime_flag=0
# print(prime_number)

# not_prime_number = set([num for num in range(1,1000) for c in range(2, int(num/2)) if num%c==0])
# print(not_prime_number)
# li= [num for num in range(1,1000) if num not in (not_prime_number)]
# print("total prime number between 1 to 1000= ", len(li), "and they are",li)

# nested_list=[[x,x*x,x*x*x] for x in range(1,4)]
# print(nested_list)
#
# flaterred_list=[i for x in nested_list for i in x]
# print(flaterred_list)

list_transaction =[[1,100,'open'],[2,105,'closed'],[3,200,'pending'],[4,201,'closed'],[4,105,'open']]


sal=[[lis[2],lis[1]] for lis in list_transaction]
# output=[(word, status.count(word)) for word in set(status)]
chk={}
print(sal)
# status =[key for item in sal for key in item]
# print(set(status))
#
# chk[k] = {v for item in sal for k,v in item.items()}
# print(chk)
# for lis in sal:
#     if lis[0] in chk.keys():
#         print(lis[0])
#         chk[lis[0]].append(lis[1])
#     else:
#         chk[lis[0]]=[lis[1]]



chk = {status: [lis[1] for lis in list_transaction if lis[2] == status]
       for status in {lis[2] for lis in list_transaction}}
print (chk)

output = {k: (sum(v)/len(v)) for k,v in chk.items()}

print(output)

chk ={ status:[lis[1] for lis in list_transaction if lis[2]==status]
       for status in{list[2] for lis in list_transaction}}