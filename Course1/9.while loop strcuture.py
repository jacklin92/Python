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


n = 5
while n > 0:
    n -= 1#n=n-1
    if n == 2:
        continue  # break是終止的意思，也就是當迴圈跑到2時，迴圈會結束；如果是continue則跳過2繼續跑迴圈
    print(n)
print("迴圈結束。")
