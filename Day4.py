pairs = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b')]
# 1. {"a": [1, 3], "b": [2, 4]}

output = {letter:[li[0] for li in pairs if li[1]==letter] for letter in (li[1] for li in pairs)}
# print(output)

# 2. expected result-
# {
#   "open": {"values":[100,105], "avg":102.5},
#   "closed": {"values":[105,201], "avg":153.0},
#   "pending": {"values":[200], "avg":200.0}
# }

transactions = [
    [1, 100, 'open'],
    [2, 105, 'closed'],
    [3, 200, 'pending'],
    [4, 201, 'closed'],
    [4, 105, 'open']
]
# Filter only statuses whose average is greater than 150.
# result={
#     status:{
#     "values":[li[1] for li in transactions if li[2]==status] ,
#     "avg": sum(li[1] for li in transactions if li[2]==status)/sum(1 for li in transactions if li[2] == status)
#
#     }
#     for status in {li[2] for li in transactions}
#     if sum(li[1] for li in transactions if li[2]==status)/sum(1 for li in transactions if li[2] == status) >150}
# # {"values":[li[1] for li in transactions if li[2]==status], "sum":sum(li[1] for li in transactions if li[2]==status) }
# print(result)

# Mark each status as "high" or "low" depending on whether its sum exceeds 250.
# Expected:{"open":"low", "closed":"high", "pending":"low"}
result={
    status: "high" if sum(li[1] for li in transactions if li[2]==status) > 200 else "low"

    for status in {li[2] for li in transactions}}
    # if sum(li[1] for li in transactions if li[2]==status)/sum(1 for li in transactions if li[2] == status) >150}
# {"values":[li[1] for li in transactions if li[2]==status], "sum":sum(li[1] for li in transactions if li[2]==status) }
print(result)

# Build a dictionary where each status maps to another dictionary containing:
#
# "values" → list of amounts
#
# "count" → number of transactions
#
# "max" → maximum amount
#
# "min" → minimum amount
# result={
#     status:{
#     "values":[li[1] for li in transactions if li[2]==status] ,
#     "count": sum(1 for li in transactions if li[2] == status),
#      "min": min([li[1] for li in transactions if li[2]==status] )
#
#     }
#     for status in {li[2] for li in transactions}
#     if sum(li[1] for li in transactions if li[2]==status)/sum(1 for li in transactions if li[2] == status) >150}
# # {"values":[li[1] for li in transactions if li[2]==status], "sum":sum(li[1] for li in transactions if li[2]==status) }
# print(result)


data = [
    ("A", "X", 10),
    ("A", "Y", 20),
    ("B", "X", 30),
    ("B", "Y", 40),
    ("A", "X", 50)
]
# Expected:
#
# python
# {("A","X"):60, ("A","Y"):20, ("B","X"):30, ("B","Y"):40}

l1=[1,2,3,4,5]
l2=[2,3,5,6,7]
l3=[5,6,9,10]

# common = set(l1).intersection(set(l2)).intersection(set(l3))
# print(common)

# li=l1+l2+l3
# output = {cnt: li.count(cnt) for cnt in set(li)}
#
# print(output)

dict1={"Nancy":100 , "Ankush":200, "Naksh":500}
dict2={"Ankush":100, "Kiran":150, "Narinder":200,"Naksh":400}

# dict =[keys for keys in dict1.items()] + [keys for keys in dict2.items()]
# output = { name:sum(l[1] for l in dict if l[0]==name) for name in [i[0] for i in dict]}
# print(output)
# # output ={}

final_dict={}

for keys in dict1.keys():
    if keys in dict2.keys():
        final_dict[keys]=sum([dict1[keys]]+[dict2[keys]])
    else:
        final_dict[keys]=dict1[keys]

for keys in dict2.keys():
    if keys not in dict1.keys():
        final_dict[keys]= dict2[keys]

print (final_dict)



