import csv
from peewee import *
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


def import_from_db(locations):
    locationsDict = {}
    declaredlocs = []
    for i in range(1, locations + 1):
        check = True
        while check:
            locationId = input('Podaj ID lokalizacji ' + str(i))
            if int(locationId) <= 1 or int(locationId) > 10:
                print('Proszę podać id z zakresu od 2 do 10 (id=1 to jest magazyn)')
            elif locationId in declaredlocs:
                print('Lokacja o id=',locationId, 'już została zadeklarowana. Proszę podać inne id')
            else:
                declaredlocs.append(locationId)
                check = False
        locationsDict[i] = list(locationId)
        check = True
        while check:
            loc_demand = (int(input('Podaj zapotrzebowanie w lokacji ' + str(i))))
            if loc_demand > 1500:
                print('Przekroczono max. ładowność pojazdu. Proszę podać mniejszą wartość')
            else:
                check = False
        locationsDict[i].append(loc_demand)
    return locationsDict


def make_demand():
    locations = int(input('Podaj liczbę lokacji'))
    locationsDict = import_from_db(locations)
    with open('Demand.csv', 'w', newline='') as demand_file:
        fieldnames = ['id', 'zapotrzebowanie']
        demand = csv.writer(demand_file, delimiter=';')
        demand.writerow(fieldnames)
        demand_list = [fieldnames]
        for key_id, value_demand in locationsDict.items():
            demand_row = [value_demand[0], value_demand[1]]
            demand_list.append(demand_row)
            demand.writerow(demand_row)
    return demand_list
