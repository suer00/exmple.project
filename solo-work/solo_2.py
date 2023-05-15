
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
