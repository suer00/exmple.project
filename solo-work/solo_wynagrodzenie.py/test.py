import pandas as pd
import csv
from csv import DictReader


class Pracownik:
    #wyliczenia dotyczą pracowników powyżej 26 roku życia zatrudnionych na podstawie umowy o pracę.
    # https://ksiegowosc-budzetowa.infor.pl/kadry-i-place/wynagrodzenia/5533738,Wzor-obliczania-pensji-netto-z-brutto-przyklad-kroki-algorytm-kalkulator-brutto-netto.html

    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

#stworzenie csv z przcownikami


f = open('pracownicy.csv', 'w')
writer = csv.writer(f)
header = ['Imie', 'Nazwisko', 'Wynagrodzenie_brutto']
row1 = ['Grazyna', 'Heban', '4500']
row2 = ['Mateusz', 'Mull', '4040']
writer.writerow(header)
writer.writerow(row1)
writer.writerow(row2)

        # close the file
f.close()

#Wyczytanie csv jako slownika
with open("salary.csv", 'r') as f:
    pracownicy = DictReader(f)

    list_of_dict = list(pracownicy)


for pracownik in list_of_dict:
    pracownik
    ludek=Pracownik(pracownik.get('imie'), pracownik.get('nazwisko'), pracownik.get('wynagrodzenie_brutto'))
    print(type(pracownik))


