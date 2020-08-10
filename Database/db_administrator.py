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


def add():
    new_id = int(input('Proszę wpisać nowe ID\n'))
    new_name = input('Proszę podać nazwę\n')
    new_address = input('Proszę podać adres\n')
    new_longitude = float(input('Proszę podać długość geograficzną (zaokrąglenie do 8 miejsc po kropce)\n'))
    new_latitude = float(input('Proszę podać szerokość geograficzną (zaokrąglenie do 8 miejsc po kropce)\n'))
    try:
        dtb.create(id=new_id, name=new_name, address=new_address, longitude=new_longitude, latitude=new_latitude)
        print('Lokalizacja dodana!\n')
    except:
        print('Lokalizacja o tym ID już istnieje')
    input('Wciśnij Enter\n')


def delete():
    id_to_delete = int(input('Proszę podać ID rekordu do usunięcia\n'))
    if input('Potwierdź usunięcie wpisując Y\n').upper() == 'Y':
        try:
            dtb.get(id=id_to_delete).delete_instance()
            print('Usunięto lokalizację o ID {}\n'.format(id_to_delete))
        except:
            print('Nie znaleziono ID\n')
    else:
        print('Lokalizacja NIE została usunięta')
        input('Wciśnij Enter\n')


def search():
    search_id = int(input('Proszę podać ID\n'))
    try:
        search_name = dtb.get(id=search_id).name
        search_address = dtb.get(id=search_id).address
        search_longitude = dtb.get(id=search_id).longitude
        search_latitude = dtb.get(id=search_id).latitude
        print('Id: {}\n'
              'Nazwa: {}\n'
              'Adres: {}\n'
              'Współrzędne: {}N, {}E\n'.format(search_id,search_name, search_address, search_latitude, search_longitude))
    except:
        print('Nie znaleziono ID!')
    input('Wciśnij Enter\n')


db.connect()
dtb = Location()


if __name__ == '__main__':
    while True:
        option = input('Aby dodać lokalizację wpisz A\n'   
                       'Aby wyszukać lokalizację wpisz S\n'
                       'Aby usunąć lokalizację wpisz D\n'
                       'Aby zakończyć wpisz Q\n').upper()
        if option == 'A':
            add()
        elif option == 'S':
            search()
        elif option == 'D':
            delete()
        elif option == 'Q':
            break
        else:
            print('Nie rozpoznano komendy.\n')
