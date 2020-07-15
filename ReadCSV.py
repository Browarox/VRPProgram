import csv


def index():
    index = []
    with open('Data.csv', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            listToIndex = (row[0].split(";"))
            index.append(listToIndex)
    return index
