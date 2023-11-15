import matplotlib.pyplot as plt
import csv

file_name = "sample.csv"

categories = []
values = []

with open(file_name, "r") as csvfile:
    csv_reader = csv.reader(csvfile)

    # Skip the header row
    header = next(csv_reader)

    for row in csv_reader:
        category, value = row
        categories.append(category)
        values.append(int(value))


plt.scatter(categories, values, color="blue", marker="o", label="Scatter Plot")


plt.title("Age Scatter Plot")
plt.xlabel("Name")
plt.ylabel("Age")

# Display the chart
plt.legend()
plt.show()
