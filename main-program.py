import program2, MakeCSV, LoadDemand as Ld


if input('Aby stworzyć nowy plik CSV wpisz N.\nAby wczytać dane z gotowego pliku Demand.csv wciśnij ENTER ') == 'N':
    MakeCSV.start()
else:
    Ld.load()

program2.start()
