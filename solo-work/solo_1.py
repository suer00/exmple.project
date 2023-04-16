# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie")

print("Hello {}".format(student))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi: {}".format(liczba_studentow))


# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in studenci:
    print("Hello {}".format(i))

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

print("Wynik wynosi: {}".format(wynik))

# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")


print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci= sorted(studenci)

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)


# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studemco=studenci.sort(key=lambda n: n.split()[1])

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
litera = 'N'

nazwiska = [sub.split()[1] for sub in studenci if len(sub.split()) > 1]
studenci_z_nazwiskie_N = [idx for idx in nazwiska if idx.lower().startswith(litera.lower())]


liczba_n = len(studenci_z_nazwiskie_N)
print("Liczba studentow na N wynosi: "+ str(liczba_n))


# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True



def czy_funkcja_liniowa(wykres):
    x1 = wykres[0][0]
    y1 = wykres[0][1]
    x2 = wykres[1][0]
    y2 = wykres[1][1]


    a = (y2-y1)/(x2-x1)
    b = y1 - a * x1

    x3 = wykres[2][0]
    y3 = wykres[2][1]

    test = a * x3 + b
    if test == y3:
        return True
    else:
        return False


wykres_1_funkcja_liniowa = czy_funkcja_liniowa(wykres_1)

wykres_2_funkcja_liniowa = czy_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")

