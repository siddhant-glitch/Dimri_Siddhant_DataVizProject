import csv
import matplotlib.pyplot as plt

can = []
ger = []



categories = []


with open('canvsger.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			#parse thtafirst row of text data out of the file
			categories.append(row)
			line_count += 1
		else:
			if row[4] == "CAN":
				print("canada won")
				can.append(row[4])

			elif row[4] == "GER":
				print("germany won")
				ger.append(row[4])

			line_count += 1;

print("Medals for CAN: ", len(can))
print("Medals for GER: ", len(ger))

#plota pie chart

labels = ("CAN", "GER")

sizes = [len(can), len(ger)]
colors = ['cyan', 'blue']
explode = (0.1, 0.1)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("CAN vs. GER")
plt.xlabel("Medals since 1924")
plt.show()