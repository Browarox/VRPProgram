from VRPv3.ReadCSV import index, locationsCount
from random import shuffle


def create_list(locationsCount):
    locationsList = []
    for i in range(1, locationsCount):
        locationsList.append(i)
    return locationsList


def route(locationsList, maxCapacity):
    leftCapacity = maxCapacity
    fullDistance = 0
    returning = []
    for i in range(0, len(locationsList)-1):
        driveFrom = locationsList[i]
        driveTo = locationsList[i+1]
        zapotrzebowanie = int(index[driveTo+1][locationsCount + 1])
        if leftCapacity >= zapotrzebowanie:
            distance = float(index[driveFrom+1][driveTo+1])
            leftCapacity -= zapotrzebowanie
            fullDistance += distance
        else:
            distance = float(index[1][driveFrom+1]) + float(index[1][driveTo+1])
            leftCapacity = maxCapacity - zapotrzebowanie
            fullDistance += distance
            returning.append(index[0][driveFrom+1])
    return [fullDistance, returning]

def random_locations():
    locationsList = []
    randomList = create_list(locationsCount)
    shuffle(randomList)
    locationsList.append(0)
    locationsList += randomList
    locationsList.append(0)
    return locationsList

def start():
    maxCapacity = 1500
    fullDistance = 0
    iterations = 1000

    returnings = []
    locationsList = []
    for _ in range(locationsCount):
        locationsList.append(_)
    locationsList.append(0)

    optimization = route(locationsList, maxCapacity)
    optimizedDistance = optimization[0]
    optimizedList = locationsList
    optimizedReturnings = optimization[1]


    for j in range(iterations):
        locationsList = random_locations()
        optimization = route(locationsList, maxCapacity)
        newDistance = optimization[0]
        returnings = optimization[1]
        if newDistance < optimizedDistance:
            optimizedDistance = newDistance
            optimizedList = locationsList
            optimizedReturnings = returnings

    print(optimizedList, round(optimizedDistance, 2))
    routeList = []
    returningList = []
    for id in optimizedList:
        routeList.append(index[int(id + 1)][locationsCount+2])
    for id in optimizedReturnings:
        returningList.append(index[int(id) + 1][locationsCount+2])
    print('Optymalna trasa wiedzie przez lokacje o następujących ID:', routeList, 'o długości:', round(optimizedDistance, 2), 'km. Po punktach', returningList, 'należy ponownie załadować samochód')
