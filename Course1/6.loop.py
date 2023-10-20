"""
好的，那麼既然對運算子有一點初步的認識了，那我們接下來就來說說運算子的好朋友:迴圈

在python裡面，迴圈最常見的有:
1.while迴圈
    while 判斷條件：
    執行語句……
2.for迴圈
    for i in range(0,5):
        i+=i
    print(i)
3.巢狀迴圈(while+for)
    for i in range(1, 6):
        for j in range(1, 6):
            result = i * j
            print(f'{i} x {j} = {result}')
以下會帶大家做做看各種迴圈的應用例子
"""
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
