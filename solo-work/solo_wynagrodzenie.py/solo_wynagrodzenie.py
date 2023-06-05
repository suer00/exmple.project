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

    def pensja_brutto(self):
        return self.wynagrodzenie_brutto


    def oblicz_netto(self):

        #składki na ZUS =pensja brutto zł x wskaźnik 13,71%
        #składka zdrowotna=(pensja brutto – składki na ZUS) x 9%
        # #zaliczka na PIT = Dochód*stawka PIT
        #Wynagrodzenie użytkownika (pensja brutto – składki na ZUS – składka zdrowotna – zaliczka na PIT)
# załozenie stawka PIT -12%
        wynagrodzenie_brutto = float(self.wynagrodzenie_brutto)
        skladka_zus = wynagrodzenie_brutto * 0.1371
        skladka_zdrowotna = (wynagrodzenie_brutto-skladka_zus)*0.09
        zaliczka_na_PIT = wynagrodzenie_brutto *0.12
        wynagordzenie_netto = wynagrodzenie_brutto-skladka_zus-skladka_zdrowotna-zaliczka_na_PIT
        return wynagordzenie_netto




    def oblicz_koszt(self):
#https://kadry.infor.pl/5725403,koszty-pracodawcy-zwiazane-z-zatrudnieniem-pracownika.html
        # składka_emerytalna = 9, 76 % x brutto
        # składka_rentowa = 6, 50 % x brutto
        # składka_na_ubezpieczenie_wypadkowe = 1, 67 % x brutto
        # składka_na_Fundusz_Pracy - 2, 45 % x brutto
        # składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych = 0, 10 % x brutto
        wynagrodzenie_brutto=float(self.wynagrodzenie_brutto)
        składka_emerytalna  = 0.0976 * wynagrodzenie_brutto
        składka_rentowa = 0.065 * wynagrodzenie_brutto
        składka_na_Fundusz_Pracy = 0.0245 * wynagrodzenie_brutto
        składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych = 0.001 *  wynagrodzenie_brutto
        koszt=wynagrodzenie_brutto + składka_emerytalna + składka_rentowa + składka_na_Fundusz_Pracy +składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych
        return koszt

#nie powinien bz w klasie pracownik
    def oblicz_koszt_calkowity(self, pracownicy):
        koszt_calkowity = 0
        wynagrodzenie_brutto = float(self.wynagrodzenie_brutto)
        for pracownik in pracownicy:
            składka_emerytalna = 0.0976 * wynagrodzenie_brutto
            składka_rentowa = 0.065 * wynagrodzenie_brutto
            składka_na_Fundusz_Pracy = 0.0245 * wynagrodzenie_brutto
            składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych = 0.001 * wynagrodzenie_brutto
            koszt = wynagrodzenie_brutto + składka_emerytalna + składka_rentowa + składka_na_Fundusz_Pracy + składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych
            koszt_calkowity += koszt
        return koszt_calkowity

    def koszt_calkowity_wszystkich_pracownikow(self, pracownicy):
        koszt_calkowity = 0
        wynagrodzenie_brutto= float(self.wynagrodzenie_brutto)
        for pracownik in pracownicy:
            składka_emerytalna = 0.0976 * wynagrodzenie_brutto
            składka_rentowa = 0.065 * wynagrodzenie_brutto
            składka_na_Fundusz_Pracy = 0.0245 * wynagrodzenie_brutto
            składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych = 0.001 * wynagrodzenie_brutto
            koszt = wynagrodzenie_brutto + składka_emerytalna + składka_rentowa + składka_na_Fundusz_Pracy + składka_na_Fundusz_Gwarantowanych_Świadczeń_Pracowniczych
            koszt_calkowity+=koszt
        return koszt_calkowity





#stworzenie csv z przcownikami


with open("salary.csv", 'r') as f:
    pracownicy = DictReader(f)

    pracownicy = list(pracownicy)





for pracownik in pracownicy:
    ludek = Pracownik(pracownik.get('imie'), pracownik.get('nazwisko'), pracownik.get('wynagrodzenie_brutto'))
    print("Pracownik: ", ludek)
    print(" -pensja brutto: ", ludek.pensja_brutto())
    print(" -pensja netto: ",ludek.oblicz_netto())
    print(" -koszty pracodawcy: ",ludek.oblicz_koszt())
    #print(" -koszt całkowity: ", ludek.oblicz_koszt_calkowity())
print('----------------------------------------------------------------------------------')
print("Suma kosztów wyników: ", ludek.koszt_calkowity_wszystkich_pracownikow(pracownicy))

        #wsyztskie koszty skłądki jakie ponosi pracodawca
