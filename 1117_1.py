
# for index1,i in enumerate(str1):
#         if str1[index1]==str1[lenght-index1-1]:
#             print("yes")
#         else:
#             print("no")
# yes=[]
#
# for i  in range(lenght):
#     if str1[i] == str1[lenght - i - 1]:
#         yes.append("yes")
#     else:
#         yes.append("no")
# if "no" in yes:
#     print("不是回文数")
# else:
#     print("是回文数")
# fun = 1911
# thou=fun//1000
# hundred=fun//100%10
# ten=fun//10%10
# ge=fun%10
# pass
nums=[2,7,11,15]
tag=18
flag=0
for i ,k in enumerate(nums):
    for j , b in enumerate(nums):
        if i==j:
            continue
        else:
            if k +b ==tag:
                print(f"{k}+{b}={tag}")
                print(i)
                print(j)
                flag=1
                break
    if flag:
        break
