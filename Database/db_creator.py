from peewee import *


db = SqliteDatabase('locations.db')


class Location(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    address = CharField()
    latitude = FloatField()
    longitude = FloatField()

    class Meta:
        database = db


def add_locations(loc):
    for location in loc:
        Location.create(id=int(location[0]),
                        name=location[1],
                        address=location[2],
                        latitude=float(location[3]),
                        longitude=float(location[4]))


db.connect()
dtb = Location()

example = dtb.get(id=1).latitude
