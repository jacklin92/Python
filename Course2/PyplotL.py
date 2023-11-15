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
        
plt.plot(categories, values, marker='o', color='green', label='Line Chart')

# Add title and axis labels
plt.title("Age Line Chart")
plt.xlabel("Name")
plt.ylabel("Age")

# Display the chart
plt.legend()
plt.show()