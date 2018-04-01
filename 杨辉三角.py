print("￥￥￥输出杨辉三角￥￥￥")
num = int(input("请输入级数:"))
for i in range(0,num):
    print(" ",end=" ")
print(1)
list = [1]
for j in range(0,num-1):
    for i in range(0,num-j-1):
        print(" ",end=" ")
    print(1,end="   ")
    tmp = [1]
    for k in range(0,len(list)-1):
        print(list[k]+list[k+1],end="   ")
        tmp.append(list[k]+list[k+1])
    print(1)
    tmp.append(1)
    list=tmp

