import csv
import psycopg2 as pg2
from DistanceCalc import distance_calc

def import_from_db(locations, cur):
    locationsDict = {}
    for i in range(1, locations + 1):
        locationId = input('Podaj ID lokalizacji ' + str(i))
        locationsDict[i] = list(locationId)
        latitudeQuerry = 'select latitude from locations where id = ' + locationId
        cur.execute(latitudeQuerry)
        locationsDict[i].append(float(cur.fetchone()[0]))  # to [0] jest potrzebne bo bez tego zwraca tuple
        longitudeQuerry = 'select longitude from locations where id = ' + locationId
        cur.execute(longitudeQuerry)
        locationsDict[i].append(float(cur.fetchone()[0]))
        locationsDict[i].append(int(input('Podaj zapotrzebowanie w lokacji ' + str(i))))
    locationsDict[0] = ['1']
    latitudeQuerry = 'select latitude from locations where id = 1'
    cur.execute(latitudeQuerry)
    locationsDict[0].append(float(cur.fetchone()[0]))
    longitudeQuerry = 'select longitude from locations where id = 1'
    cur.execute(longitudeQuerry)
    locationsDict[0].append(float(cur.fetchone()[0]))
    locationsDict[0].append(0)
    return locationsDict

def start():
    locations = int(input('Podaj liczbę lokacji'))

    conn = pg2.connect(database='VRPLocations', user='postgres', password='jaxr12')
    cur = conn.cursor()

    locationsDict = import_from_db(locations, cur)

    with open('Data.csv', 'w',  newline='') as dataCsv:
        fieldnames = ['']
        for i in range(locations+1):
            fieldnames.append(i)
        fieldnames.append('zapotrzebowanie')
        fieldnames.append('id')
        distance = csv.writer(dataCsv, delimiter=';')
        distance.writerow(fieldnames)
        for i in range(locations+1):
            distancesRow = [i]
            for j in range(locations+1):
                if i != j:
                    distancesRow.append(distance_calc((locationsDict[i][1], locationsDict[i][2]), ((locationsDict[j][1], locationsDict[j][2]))))
                else:
                    distancesRow.append(0)
            distancesRow.append(locationsDict[i][3])
            distancesRow.append(locationsDict[i][0])
            distance.writerow(distancesRow)
