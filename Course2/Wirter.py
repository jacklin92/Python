import csv
#資料寫入
data = [
    ['Name', 'Age'],
    ['John', 28],
    ['Alice', 22],
    ['Bob', 35]
]
#定義檔名
file_name = 'sample.csv'
#file_path = '/path/to/your/directory/sample.csv' #指定寫入位置
#將資料放進剛剛開的csv檔案
with open(file_name, 'w', newline='') as csvfile:
    #創建Writer
    csv_writer = csv.writer(csvfile)
    # 逐行寫入資料
    csv_writer.writerows(data)
print(f'資料已寫入{file_name}。')


'''
newdata=[['Jack',20]]
with open(file_name, 'a', newline='') as csvfile:
    # 創建Writer
    csv_writer = csv.writer(csvfile)
    # 逐行寫入資料
    csv_writer.writerows(newdata)
print(f'資料已寫入{file_name}。')
'''

