nums=[12,10,6,23,123]
target=123
flag=5
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==5:
    print("Not found")
else:
    print("target found at:",flag)
