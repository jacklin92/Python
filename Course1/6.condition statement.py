"""
判斷式if
    if "條件":
        如果符合條件就執行
    elif"條件":
        如果上面 if/elif 的條件不符合但本elif的條件符合就執行
    else:
        上述條件都不符合就執行
"""
x = int(input("輸入一個0~100之間的數字:"))
if x > 80:
    print("A")
elif x > 60:
    print("B")
elif x > 40:
    print("C")
else:
    print("D")
