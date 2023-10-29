# #例1
# x = int(input("輸入數字計算數字平方:"))
# y = 0
# for i in range(0, x):
#     for j in range(0, x):#(0,0)(0,1).....(0,7)，(1,0~7)(x,y)
#         y += 1
# print("{}的平方是:{}!".format(x, y))
#例2
n = int(input("輸入數字計算數字內的質數:"))
i = 2
while i < n+1:
    j = 2
    while j <= (i // j):
        if i % j == 0:
            # print("i:%d"% i)
            # print("j:%d"% j)
            # print(i//j)
            print(i, "不是質數")
            break
        j = j + 1
    if j > i // j:
        # print("i:%d"% i)
        # print("j:%d"% j)
        # print(i//j)
        print(i, "是質數")
    i = i + 1
print("%d以內的質數都算出來了(含%d)" % (n,n))
