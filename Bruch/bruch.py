#-*- coding: utf-8 -*-
from __future__ import division


class Bruch(object):

    def __init__(self, zaehler = 0, nenner = 1):

        [self.__zaehler, self.__nenner] = self.__kuerzen(zaehler, nenner)

    def __add__(self, other):
        if isinstance(other, Bruch):

            zaehler = self.__zaehler * other.__nenner + self.__nenner * other.__zaehler
            nenner = self.__nenner * other.__nenner

            bruch = self.__kuerzen(zaehler, nenner)

            return Bruch(bruch[0], bruch[1])

        elif isinstance(other, (int, long)):
            zaehler = self.__zaehler + other * self.__nenner
            nenner = self.__nenner
            bruch = self.__kuerzen(zaehler, nenner)

            return Bruch(bruch[0], bruch[1])

    def __sub__(self, other):
        if isinstance(other, Bruch):
            return self.__add__(Bruch(-other.__zaehler, other.__nenner))
        elif isinstance(other, (int, long)):
            return self.__add__(-other)

    def __mul__(self, other):
        assert isinstance(other, Bruch)

        zaehler = self.__zaehler * other.__zaehler
        nenner = self.__nenner * other.__nenner
        bruch = self.__kuerzen(zaehler, nenner)

        return Bruch(bruch[0], bruch[1])

    def __truediv__(self, other):
        if isinstance(other, Bruch):
            return self.__mul__(Bruch(other.__nenner, other.__zaehler))
        elif isinstance(other, (int, long)):
            return self.__mul__(Bruch(1, other))

    def getDezimal(self):
        return self.__zaehler / self.__nenner

    def __kuerzen(self, zaehler, nenner):

        #Vorzeichen bereinigen -> in Zaehler schieben
        vorzeichen = 1
        if (zaehler < 0 and nenner > 0) or zaehler > 0 and nenner < 0:
            vorzeichen = -1

        zaehler = abs(zaehler)
        nenner = abs(nenner)

        #kleineren Wert fuer ggt finden
        klein = int(min([zaehler, nenner]))

        #groessten gemeinsamen Teiler finden
        ggt = 1
        for i in range(1, klein + 1):
            if zaehler % i == 0 and nenner % i == 0:
                ggt = i

        return [vorzeichen*zaehler/ggt, nenner/ggt]

    def getZahler(self):
        return self.__zaehler

    def getNenner(self):
        return self.__nenner

    def Ausgabe(self):
        print u"Zähler: \t" + str(int(self.__zaehler))
        print "Nenner: \t" + str(int(self.getNenner()))

        return

    def check(self):
        print self.__kuerzen(self.__zaehler, self.__nenner)
        return