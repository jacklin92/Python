# List
List1 = [1, 2, 3]
List2 = [4, 5, 6]
List3 = List1 + List2
print(List3)
# len():計算List的長度
print(len(List1))
# append(x):新增
List3.append(7)
print(List3)
# pop(i):指定位置後，刪除該位置存在的元素
List3.pop(6)
print(List3)
# remove(x):刪除列表中第一個為x的值
List3.append(1)
print(List3)
List3.remove(1)
print(List3)
# insert(i,x):在指定位置插入元素，並將原本元素向後移
List3.insert(0, 1)
print(List3)
# clear():清除list中所有元素，變成空列表
List4 = [1, 2, 3, 4, 5]
List4.clear()
print(List4)
# index(x):返回列表中第一個值為x的元素的索引。如果沒有為x的元素就會返回一個錯誤
print(List1.index(1))
# print(List1.index(0))
# count(x):計算x在列表中出現的次數
List5 = [1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6]
print(List5.count(6))
# sort():將列表元素由小排到大
List6 = [1, 3, 5, 6, 2, 4]
List6.sort()
print(List6)
# reverse():將列表原本的順序倒過來
List6.reverse()
print(List6)
# extend(List):其實就是List跟List合併(List+List)
print(List1 + List2)
# copy():複製一個List的所有元素
List7 = List1.copy()
print(List7)
