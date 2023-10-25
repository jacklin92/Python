x = 0
for i in range(0, 3):
    for j in range(0, 3):
        x += 1
print(x)


n = int(input("輸入數字計算數字內的質數:"))
i = 2
while i < n:
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
print("%d以內的質數都算出來了" % (n))
