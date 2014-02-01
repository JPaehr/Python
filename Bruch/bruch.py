from __future__ import division


class Bruch(object):

    def __init__(self, zaehler = 0, nenner = 1):
        self.__zaehler = zaehler
        self.__nenner = nenner

    def __add__(self, other):
        if type(other) == Bruch:
            zaehler = self.__zaehler*other.__nenner + self.__nenner*other.__zaehler
            nenner = self.__nenner * other.__nenner

            bruch = self.__kuerzen(zaehler, nenner)

            return Bruch(bruch[0], bruch[1])
        elif type(other) == int:
            zaehler = self.__zaehler + other * self.__nenner
            nenner = self.__nenner
            bruch = self.__kuerzen(zaehler, nenner)

            return Bruch(bruch[0], bruch[1])

    def __mul__(self, other):
        assert isinstance(other, Bruch)
        zaehler = self.__zaehler * other.__zaehler
        nenner = self.__nenner * other.__nenner
        bruch = self.__kuerzen(zaehler, nenner)

        return Bruch(bruch[0], bruch[1])

    def __truediv__(self, other):
        if isinstance(other, Bruch):
            return self.__mul__(Bruch(other.__nenner, other.__zaehler))

    def getDezimal(self):
        return self.__zaehler / self.__nenner

    def __kuerzen(self, zaehler, nenner):
        vorzeichen = 1
        if (zaehler < 0 and nenner > 0) or zaehler > 0 and nenner < 0:
            vorzeichen = -1

        zaehler = abs(zaehler)
        nenner = abs(nenner)
        print zaehler
        print nenner
        klein = min([zaehler, nenner])
        ggk = 1
        for i in range(1, klein + 1):
            if zaehler % i == 0 and nenner % i == 0:
                ggk = i

        return [vorzeichen*zaehler/ggk, nenner/ggk]

    def getZahler(self):
        return self.__zaehler

    def getNenner(self):
        return self.__nenner

    def check(self):
        print self.__kuerzen(self.__zaehler, self.__nenner)

zahl1 = Bruch(-6, 2)
zahl1.check()
print zahl1.getZahler()

zahl2 = Bruch(1, 2)

zahl3 = zahl1 / zahl2
print zahl3.getDezimal()