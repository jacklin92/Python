import csv
#告訴程式要讀哪個檔案
file_name = 'sample.csv'
#讀取檔案
with open(file_name, 'r') as csvfile:
    # 創建CSV reader
    csv_reader = csv.reader(csvfile)
    #逐行讀取
    for row in csv_reader:
        print(row)
