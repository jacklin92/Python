# Import:導入模組
import math

print(math.sqrt(25))
# 另類的導入模式
import math as m

print(m.sqrt(4))
# from math import x:注意!這裡的x是指一個or一個以上的功能
# from math import *:導入math的所有功能


def hi(x):
    return f"hi!{x}!"
