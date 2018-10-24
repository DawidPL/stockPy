from class import Global
from math import range

indicator_list = []
indicator_name_list = ["drugi","trzeci,","czwarty","piaty","szosty","siodmy","osmy"]
chart_range_eng = ''
chart_range_list = ['date', '1d', '1m', '3m', '6m', '1y', '2y', '5y']
chart_range_list_pl = ['dzienny', '1d', '1m', '3m', '6m', 'rok', '2lata', '5lat']
indicator_list_base = [rsi, macd, adx, ma]

def ma_properties(value, type):
    if my_type == 'prosta':
        pass
    elif my_type == 'ważona':
        pass
    elif my_type == 'wykladnicza':
        pass
print("Witaj w programie analitycznym.")
ticket = input('Podaj ticket spolki ktora chcesz sprawdzic')
print(chart_range_list_pl)

check_range == false

while check_range != true:
    chart_range = input('Jaki przedział czasowy Cię interesuje z wyzej wymienionych?')
    if chart_range in chart_range_list_pl:
        x = chart_range_eng.index(chart_range)
        chart_range_eng = chart_range_list[x]
        check_range == true
    elif:
        print('Nie ma takiego przedziału, sprobuj ponownie.')

print("Witaj w programie, oto lista dostepnych wskaznikow:")
for i in indicator_list_base:
    print(i)
input_indcators_number = int(input("Ile wskaźnikow chcesz sprawdzic?"))
for i in range(0, input_indcators_number):
    if input_indcators_number == 1:
        input_indicator = str(input("Podaj wskaźnik ktory chcesz sprawdzic i zatwierdz enterem:"))
        input_indicator = input_indicator.capitalize()
        indicator_list.append(input_indicator)
        if input_indicator == "ma":
            ma_properties()
    elif input_indcators_number <= 0:
        print("Podałeś złą wartosc. Koniec programu")
        break
    elif input_indcators_number > 1:
        for i in indicator_name_list[:input_indcators_number]:
            input_indicator = input("Podaj "+ str(i) "+ wskaźnik ktory chcesz sprawdzic i zatwierdz enterem:")
            input_indicator = input_indicator.capitalize()
            if input_indicator == "ma":
                ma_value = int(input("Podaj liczbe okresow ktore chcesz sprawdzic"))
                ma_type = input("Podaj typ sredniej (prosta, ważona, wykladnicza)")
                ma_properties(ma_value, ma_type)
            indicator_list.append(input_indicator)