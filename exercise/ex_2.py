# kwadrat

a = 10

obwod = a * 4
pole = pow(a, 2)
print("Obwód kwardratu wynosi", obwod, "a pole", pole)
print("Obwód kwardratu wynosi {} a pole {}".format(obwod, pole))

#Prostokąt

b = 10
c = 20

obwod_p = 2*b + 2* c
pole_p = b * c

print("Obwód prostokąta wynosi {} a pole {}".format(obwod_p, pole_p))

#Koło
import math
r = 10


obwod_k = 2*math.pi*r
pole_k = math.pi*pow(r,2)

print("Obwód koła wynosi {} a pole {}".format(obwod_k, pole_k))
 


#Trapez

podstawa_1 = 7
podstawa_2 = 8
ramie_1=4
ramie_2=9
wysokosc=9

obwod_t =podstawa_1+podstawa_2+ramie_1+ramie_2
pole_t = ((podstawa_1+podstawa_2)/2)*wysokosc

print("Obwód trapezu wynosi {} a pole {}".format(obwod_t, pole_t))



