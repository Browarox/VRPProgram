import program2, MakeCSV, LoadDemand as Ld, RouteVisual as RV

if input('Aby stworzyć nowy plik CSV wpisz N.\n'
         'Aby wczytać dane z gotowego pliku Demand.csv wciśnij ENTER ').upper() == 'N':
    demand = MakeCSV.make_demand()
    print('Proszę czekać...')
    Ld.load(maker_checker=demand)
else:
    print('Proszę czekać...')
    Ld.load()
result = program2.start()
routeList = result[0]
optimizedDistance = result[1]
returningList = result[2]
print('Optymalna trasa wiedzie przez lokacje o następujących ID:', routeList, 'o długości:',
      round(optimizedDistance, 2), 'km. Po punktach', returningList, 'należy ponownie załadować samochód')
RV.plot_creator(result)
