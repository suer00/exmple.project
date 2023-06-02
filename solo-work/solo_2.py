
class Trojkat:
    def __init__(self, a, b, c,h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a= h_a
        #self.obwod =a + b + c

    def obwod(self):
        return self.a + self.b + self.c
    def pole(self):
        return (self.a + self.b)/self.h_a
trojkat_rownoboczny = Trojkat(10,10,10,8)
print(trojkat_rownoboczny.a)
print(trojkat_rownoboczny.obwod())

trojkat_Pauliny = Trojkat(23, 27, 36, 9)
print()


class Trapez:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def pole(self):
        return ((self.a+self.b)/2)*self.h
    def obwod(self):
        return self.a+self.b+(self.c*2)

trapez = Trapez(5, 8, 4, 3)
print(trapez.pole())
print(trapez.obwod())

class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeks = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def __int__(self):
        return 5

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_Srednia(self):
        return sum(self.oceny)/len(self.oceny)


student_paulina=Student('Paulina', 'Reus', '120120')
print(student_paulina)
student_paulina.dodaj_ocene(4)
student_paulina.dodaj_ocene(5)
student_paulina.dodaj_ocene(4.5)
print(student_paulina.zwroc_Srednia())


import math
class Dieta:

    def __init__(self, waga, wzrost, wiek,plec):
        self.waga =waga
        self.wzrost= wzrost
        self.wiek =wiek
        self.plec=plec
        self.posilki=({})
        self.bmi=float
        self.bmr=float
        self.aktywnosc_fizyczna = []
        self.ilosc_wypitej_wody=[]

    def __str__(self):
        return f"Twoja aktualna waga to {self.waga}, przy wzroscie {self.wazrost}"



    def oblicz_BMI(self):
        self.bmi=self.waga/pow(self.wzrost/100,2)
        if self.bmi<=18.5:
            message='Niedowaga'
        elif self.bmi<=24.9:
            message='Waga prawidłowa'
        else :
            message='Nadwaga'

        return self.bmi, message
    def oblicz_BMR(self):
        if self.plec=='k' :
            self.bmr= (9.99 * self.waga) + (6.25 *self.wzrost) - (4.92 *self.wiek) -161
        else:
            self.bmr= (9.99 * self.waga) + (6.25 *self.wzrost) - (4.92 *self.wiek)  + 5
        return "Twoje dzienne zapotrzebowanie kaloryczne to około ", self.bmr, " kcal"

    def dodaj_posilek(self,posilek, kcal):
        self.posilki.update({posilek: kcal})
        return self.posilki
    def licz_kalorie(self):
        return "Na tą chwilę spożyłeś/aś ", sum(self.posilki.values()), "kcal"
    def dodaj_aktywnosc(self, aktywnosc):
        self.aktywnosc_fizyczna.append(aktywnosc)
    def wyswietl_aktywnosci(self):
        return self.aktywnosc_fizyczna
    def dodaj_ilosc_wypietej_wody(self, ilosc):
        self.ilosc_wypitej_wody.append(ilosc)
    def wyswietl_ilosc_wypitej_wody(self):
        return sum(self.ilosc_wypitej_wody), 'ml'


#Przykładowe wywołania
dieta = Dieta(55, 164, 22, 'k')

print(dieta.oblicz_BMI())
print(dieta.oblicz_BMR())

#w metodzie dodaj_posiłe dodajemy nazwe posilku i ilośc kolarii w formie słowanika
dieta.dodaj_posilek('śniadanie', 456)
dieta.dodaj_posilek('II śniadanie', 345)
print(dieta.licz_kalorie())

#w metodzie dodaj_aktywnosc dodajmy aktywności do listy
dieta.dodaj_aktywnosc('bieganie')
dieta.dodaj_aktywnosc('jazda na rowerze')
print(dieta.wyswietl_aktywnosci())

#funkcaj wyswietl_ilosc_wypitej_wody zsumowuje ilośc wyptej wody dodawanej za pomocą funkcji dodaj_ilosc_wypietej_wody
dieta.dodaj_ilosc_wypietej_wody(300)
dieta.dodaj_ilosc_wypietej_wody(250)
print(dieta.wyswietl_ilosc_wypitej_wody())