from Indicators import Indicators
from typing import List

indicator_list: List[str] = []
indicator_name_list: List[str] = ["drugi","trzeci,","czwarty","piaty","szosty","siodmy","osmy"]
chart_range_eng: str = ''
chart_range_list: List[str] = ['date', '1d', '1m', '3m', '6m', '1y', '2y', '5y']
chart_range_list_pl: List[str] = ['dzienny', '1d', '1m', '3m', '6m', 'rok', '2lata', '5lat']
indicator_list_base: List[str] = [rsi, macd, adx, ma]
my_type: str

def ma_properties(value: float, type: str) -> None:
    if my_type == 'prosta':
        pass
    elif my_type == 'ważona':
        pass
    elif my_type == 'wykladnicza':
        pass
print("Witaj w programie analitycznym.")
ticket: str = input('Podaj ticket spolki ktora chcesz sprawdzic')
print(chart_range_list_pl)

check_range: bool == True

while check_range:
    chart_range: str = input('Jaki przedział czasowy Cię interesuje z wyzej wymienionych?')
    if chart_range in chart_range_list_pl:
        x = chart_range_eng.index(chart_range)
        chart_range_eng = chart_range_list[x]
        check_range == False
    else:
        print('Nie ma takiego przedziału, sprobuj ponownie.')

print("Witaj w programie, oto lista dostepnych wskaznikow:")
for i in indicator_list_base:
    print(i)
input_indicators_number: int = int(input("Ile wskaźnikow chcesz sprawdzic?"))
for i in range(0, input_indicators_number):
    if input_indicators_number == 1:
        input_indicator: str = str(input("Podaj wskaźnik ktory chcesz sprawdzic i zatwierdz enterem:"))
        input_indicator = input_indicator.capitalize()
        indicator_list.append(input_indicator)
        if input_indicator == "ma":
            ma_value: int = int(input("Podaj liczbe okresow ktore chcesz sprawdzic"))
            ma_type: str = input("Podaj typ sredniej (prosta, ważona, wykladnicza)")
            ma_properties(ma_value, ma_type)
    elif input_indicators_number <= 0:
        print("Podałeś złą wartosc. Koniec programu")
        break
    elif input_indicators_number > 1:
        for i in indicator_name_list[:input_indicators_number]:
            input_indicator: str = input("Podaj "+ str(i) "+ wskaźnik ktory chcesz sprawdzic i zatwierdz enterem:")
            input_indicator = input_indicator.capitalize()
            if input_indicator == "ma":
                ma_value = int(input("Podaj liczbe okresow ktore chcesz sprawdzic"))
                ma_type = input("Podaj typ sredniej (prosta, ważona, wykladnicza)")
                ma_properties(ma_value, ma_type)
            indicator_list.append(input_indicator)
