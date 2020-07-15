import csv
from peewee import *
from DistanceCalc import distance_calc
db = SqliteDatabase('Database/locations.db')


class Location(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    address = CharField()
    latitude = FloatField()
    longitude = FloatField()

    class Meta:
        database = db


db.connect()
dtb = Location()


def import_from_database(maker_checker):
    if maker_checker:
        rows = maker_checker
    else:
        with open('Demand.csv', 'r', newline='') as demandCsv:
            reader = csv.reader(demandCsv, delimiter=';')
            rows = list(reader)
    demandDict = {}
    for i in range(1, len(rows)):
        locationId = rows[i][0]
        demandDict[i] = [int(locationId)]
        latitudeQuerry = dtb.get(id=locationId).latitude
        demandDict[i].append(latitudeQuerry)
        longitudeQuerry = dtb.get(id=locationId).longitude
        demandDict[i].append(longitudeQuerry)
        demandDict[i].append(int(rows[i][1]))
    demandDict[0] = ['1']
    latitudeQuerry = dtb.get(id=1).latitude
    demandDict[0].append(latitudeQuerry)
    longitudeQuerry = dtb.get(id=1).longitude
    demandDict[0].append(longitudeQuerry)
    demandDict[0].append(0)
    return demandDict


def load(maker_checker=False):
    locationsDict = import_from_database(maker_checker)

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
                                                      (locationsDict[j][1], locationsDict[j][2])))
                else:
                    distancesRow.append(0)
            distancesRow.append(locationsDict[i][3])
            distancesRow.append(locationsDict[i][0])
            distance.writerow(distancesRow)
