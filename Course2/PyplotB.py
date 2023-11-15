import matplotlib.pyplot as plt
import csv

file_name = "sample.csv"
categories = []
values = []

with open(file_name, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    # 第一行為標題
    header = next(csv_reader)
    for row in csv_reader:
        category, value = row
        categories.append(category)
        values.append(int(value))

# 畫直條圖
plt.bar(categories, values, color="skyblue")
# 添加標題籍資料標籤
plt.title("Age Bar Chart")
plt.xlabel("Name")
plt.ylabel("Age")

# 顯示幕前圖表
plt.show()
