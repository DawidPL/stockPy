from typing import Dict, Union
import plotly.plotly as py
import plotly.graph_objs as go

sectors: Dict[int, str] ={1:'złoto', 2:'srebro', 3:'uran', 4:'lit', 5:'metale ziem rzadkich', 6:'mangan', 7:'kobalt'}
print('Podaj inwestowany kapital (w gotowce, bez spacji) w poszczegolne sektory')
for i in sectors.keys():
    price_value = input(sectors[i])
    sector[i] = price_value

trace = go.Pie(labels=sectors.keys(), values=sectors.items())

py.iplot([trace], filename='basic_pie_chart')

print('Stworz wlasny wykres')
user_sectors: Dict[Union[int, str], int] = {}
stop: bool == True
while stop:
    user_sector = input('Podaj sektor ktory chcesz dodac do wykresu i nacisnij enter aby dodac kolejny. Jezeli dodales juz wszystkie wpisz 0 i zatwierdz aby przejsc dalej')
    user_sectors[user_sector] = 0
    if user_sector == 0:
        stop == False
for i in user_sectors.keys():
    x = 0
    user_sector_value: int = int(input('Teraz dodaj wartosci do sektora ' + i))
    user_sectors[x] = user_sector_value
    x +=

user_trace = go.Pie(labels=user_sectors.keys(), values=user_sectors.items())
py.iplot([user_trace], filename='basic_pie_chart')

change: bool == True
while change:
    edit_sector: str = input('Podaj nazwe sektora ktory chcesz edytowac')
    if edit_sector in sectors or edit_sector in user_sectors:
        edit_sector_options: str = input('Co chcesz zrobic? A - usunac , B - zmienic wartosc . Wpisz wybrana litere i nacisnij enter')
        edit_sector_options.title()
        if edit_sector_options == 'A':
            del user_sectors[edit_sector]
            print('Zmiana zakonczona')
            change == False
        elif edit_sector_options == 'B':
            new_user_sector_value: int = int(input('Podaj nowa wartosc dla sektora '+ edit_sector))
            user_sectors[edit_sector] = new_user_sector_value
            print('Zmiana zakonczona')
            change == False
    else:
        print('Nie ma takiego sektora')
