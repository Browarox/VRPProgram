import csv
import psycopg2 as pg2
from DistanceCalc import distance_calc


conn = pg2.connect(database='VRPLocations', user='postgres', password='jaxr12')
cur = conn.cursor()

def import_from_database():
    with open('Demand.csv', 'r', newline='') as demandCsv:
        reader = csv.reader(demandCsv, delimiter=';')
        rows = list(reader)
        demandDict = {}
        for i in range(1, len(rows)):
            locationId = rows[i][0]
            demandDict[i] = [int(locationId)]
            latitudeQuerry = 'select latitude from locations where id = ' + locationId
            cur.execute(latitudeQuerry)
            demandDict[i].append(float(cur.fetchone()[0]))
            longitudeQuerry = 'select longitude from locations where id = ' + locationId
            cur.execute(longitudeQuerry)
            demandDict[i].append(float(cur.fetchone()[0]))
            demandDict[i].append(int(rows[i][1]))
        demandDict[0] = ['1']
        latitudeQuerry = 'select latitude from locations where id = 1'
        cur.execute(latitudeQuerry)
        demandDict[0].append(float(cur.fetchone()[0]))
        longitudeQuerry = 'select longitude from locations where id = 1'
        cur.execute(longitudeQuerry)
        demandDict[0].append(float(cur.fetchone()[0]))
        demandDict[0].append(0)
        return demandDict

def load():

    locationsDict = import_from_database()

    with open('Data.csv', 'w', newline='') as dataCsv:
        fieldnames = ['']
        for i in range(len(locationsDict)):
            fieldnames.append(i)
        fieldnames.append('zapotrzebowanie')
        fieldnames.append('id')
        distance = csv.writer(dataCsv, delimiter=';')
        distance.writerow(fieldnames)
        for i in range(len(locationsDict)):
            distancesRow = [i]
            for j in range(len(locationsDict)):
                if i != j:
                    distancesRow.append(distance_calc((locationsDict[i][1], locationsDict[i][2]),
                                                      ((locationsDict[j][1], locationsDict[j][2]))))
                else:
                    distancesRow.append(0)
            distancesRow.append(locationsDict[i][3])
            distancesRow.append(locationsDict[i][0])
            distance.writerow(distancesRow)
