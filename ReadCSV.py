import csv

index = []
with open('Data.csv', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        listToIndex = (row[0].split(";"))
        index.append(listToIndex)
if __name__ == '__main__':
    for line in index:    # get all data to one double-level list (index[][])
        print(line)
locationsCount = len(index)-1    # index - 2 because 1 is header
