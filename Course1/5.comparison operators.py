"""
比較運算子的用法，比如常見的大於、小於或等於...等，都是比較運算子的一種喔~
等於:==、不等於:!=、

"""
z1,z2,z3,z4,z5=10,20,30,25,10
"""
補充:判斷式if
    if "條件":
        如果符合條件就執行
    elif"條件":
        如果上面 if/elif 的條件不符合但本elif的條件符合就執行
    else:
        上述條件都不符合就執行
"""
if z1 >= z2:
    print("if True")
elif z1 == z3:
    print("elif1 true")
elif z1 == z4:
    print("elif2 true")
elif z1 <= z5:
    print("elif3 true")