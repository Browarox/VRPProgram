import matplotlib.pyplot as plt
from peewee import *
import numpy as np
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


def plot_creator(result):
    locationsXY = []
    for loc in result[0]:
        locationsXY.append((dtb.get(id=loc).latitude, dtb.get(id=loc).longitude, dtb.get(id=loc).id))

    plot_points = []
    for locat in locationsXY:
        if str(locat[2]) in result[2]:
            plot_points.append(locat[0:2])
            plot_points.append(locationsXY[0][0:2])
        else:
            plot_points.append(locat[0:2])
    data = np.array(plot_points)
    plt.plot(data[:, 0], data[:, 1])
    for name in locationsXY:
        plt.text(name[0], name[1], name[2])
    plt.show()
