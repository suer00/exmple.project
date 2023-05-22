# funkcja sum_list l:
# is empty?
# y->0
# if not
# l[0]+suma_list(list[1:])

###

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


lista = [1, 2, 3]
print(suma_lista(lista))


# ///find max
# funkcja find_max l len(l):
# has only one argument?
# y->l[0]
# if not
# y->max(l[len(l)-1], find_max(l, len(l)-1))


###Finf max
def find_max(lista, a):
    if a == 1:
        return lista[0]
    else:
        return max(lista[a - 1], find_max(lista, a - 1))


lista_1 = [1, 2, 3]
a = len(lista)
print(find_max(lista_1, a))


##silnia
# // silnia
# funkcja silnia a:
# is equal to 0?
# y->1
# else:
# y-> a*silnia(a-1)

def silnia(a):
    if a == 0:
        return 1
    else:

        return a * silnia(a - 1)


a = 3
print(silnia(a))


# Fibonacii
# funkcja fibonacii(a)
# if a is equal 0
# a=0
# elif a is equal 1
# a=1
# elif a is equal 2
# a=1
# else
# return fibonacii(a-1)+fibonacii(a+1)

def fibonacii(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacii(a-1)+fibonacii(a-2)

a=12
print(fibonacii(a))
