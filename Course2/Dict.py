Dict1 = {"1": "me", "2": "you", "3": "he", "4": "she"}
# len():計算Dict的長度
print(len(Dict1))
# update():新增字典的key及對應的value
Dict1.update({"5": "it"})
# keys():告訴你Dict裡有哪些可用的key
print(Dict1.keys())
# values():告訴你Dict裡有哪些value
print(Dict1.values())
# items():告訴你Dict裡有哪些keys及對應的values
print(Dict1.items())
for key, value in Dict1.items():
    print(key, value)
# get():根據指定的鍵返回相應的值，如果鍵不存在，則返回指定的默認值(默認為None)
print(Dict1.get("1"))
print(Dict1.get("6"))
# pop():根據指定的key刪除相應的value
Dict1.pop("5")
print(Dict1.items())
# copy():複製一個字典的所有keys及對應的values
Dict2 = Dict1.copy()
print(Dict2)
# clear():清空字典中的所有keys及對應的values
Dict2.clear()
print(Dict2)
# setdefault():如果字典中存在指定的key，則返回其value。如果不存在，則插入指定的key及value
Dict1.setdefault("5", "its")
print(Dict1)
# popitem():按進入字典順序刪除一對key及value
Dict1.popitem()
print(Dict1)
# fromkeys():創建一個新Dict，其中包含指定的key，並將每個key的value設置為一個默認值(默認為None)
keys = ["a", "b", "c"]
default_value = 0
Dict3 = dict.fromkeys(keys, default_value)
print(Dict3)
