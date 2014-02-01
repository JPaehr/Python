#-*- coding: utf-8 -*-
__author__ = 'JPaehr'
import Teil as teilKl
import sys
teil1 = teilKl.Teil('lila-rot', 'gelb-lila', 'rot-gruen', 'gelb-gruen', 'gruen-rot', 'lila-gruen', 'rot-gelb', 'lila-gelb', 1)
teil2 = teilKl.Teil('gelb-rot', 'lila-gelb', 'rot-gruen', 'lila-gruen', 'gelb-rot', 'gruen-gelb', 'rot-lila', 'gruen-lila', 2)
teil3 = teilKl.Teil('gelb-lila', 'rot-gelb', 'lila-gruen', 'rot-gruen', 'gruen-lila', 'rot-gruen', 'lila-gelb', 'rot-gelb', 3)
teil4 = teilKl.Teil('lila-gruen', 'gelb-lila', 'gruen-rot', 'gelb-rot', 'lila-gruen', 'rot-lila', 'gruen-gelb', 'rot-gelb', 4)
teil5 = teilKl.Teil('rot-gruen', 'lila-rot', 'gruen-gelb', 'lila-gelb', 'gelb-gruen', 'rot-gelb', 'gruen-lila', 'rot-lila', 5)
teil6 = teilKl.Teil('gelb-lila', 'gruen-gelb', 'lila-rot', 'gruen-rot', 'rot-lila', 'gelb-rot', 'lila-gruen', 'gelb-gruen', 6)
teil7 = teilKl.Teil('gelb-gruen', 'lila-gelb', 'gruen-rot', 'lila-rot', 'rot-gruen', 'gelb-rot', 'gruen-lila', 'gelb-lila', 7)
teil8 = teilKl.Teil('gruen-lila', 'gelb-gruen', 'lila-rot', 'gelb-rot', 'rot-lila', 'gruen-rot', 'lila-gelb', 'gruen-gelb', 8)
teil9 = teilKl.Teil('lila-rot', 'gruen-lila', 'rot-gelb', 'gruen-gelb', 'gruen-rot', 'gelb-gruen', 'rot-lila', 'gelb-lila', 9)

teile = [teil1, teil2, teil3, teil4, teil5, teil6, teil7, teil8, teil9]

oben = list()
zaehler = 0

def rollen(teileListe, platz):

    assert isinstance(teileListe, list)

    for i in range(8):
        teileListe[platz-1].setSpin(i)
        if platz == 2:
            if teileListe[0].vergleich('rechts') != teileListe[1].getSeite('links'):
                continue
        if platz == 3:
            if teileListe[2].vergleich('links') != teileListe[1].getSeite('rechts'):
                continue
        if platz == 4:
            if teileListe[0].vergleich('unten') != teileListe[3].getSeite('oben'):
                continue
        if platz == 5:
            if teileListe[3].vergleich('rechts') != teileListe[4].getSeite('links'):
                continue
        if platz == 6:
            if teileListe[2].vergleich('unten') != teileListe[5].getSeite('oben'):
                continue
            if teileListe[4].vergleich('rechts') != teileListe[5].getSeite('links'):
                continue
        if platz == 7:
            if teileListe[6].vergleich('oben') != teileListe[3].getSeite('unten'):
                continue

        if platz == 8:
            if teileListe[6].vergleich('rechts') != teileListe[7].getSeite('links'):
                continue
            if teileListe[7].vergleich('oben') != teileListe[4].getSeite('unten'):
                continue


        if platz == 9:
            #print teileListe[8].getSeite('oben')
            if teileListe[0].vergleich('rechts') == teileListe[1].getSeite('links') and \
                teileListe[0].vergleich('unten') == teileListe[3].getSeite('oben') and \
                teileListe[3].vergleich('rechts') == teileListe[4].getSeite('links') and \
                teileListe[2].vergleich('links') == teileListe[1].getSeite('rechts') and \
                teileListe[2].vergleich('unten') == teileListe[5].getSeite('oben') and \
                teileListe[6].vergleich('oben') == teileListe[3].getSeite('unten') and \
                teileListe[6].vergleich('rechts') == teileListe[7].getSeite('links') and \
                teileListe[7].vergleich('rechts') == teileListe[8].getSeite('links') and \
                teileListe[1].vergleich('unten') == teileListe[4].getSeite('oben') and \
                teileListe[4].vergleich('rechts') == teileListe[5].getSeite('links') and \
                teileListe[5].vergleich('unten') == teileListe[8].getSeite('oben') and \
                teileListe[7].vergleich('oben') == teileListe[4].getSeite('unten'):
                print "Es hat einen Treffer gegeben"
                teilPlatz = 1
                for einzelteile in teileListe:

                    print "Platz " + str(teilPlatz) + " ",
                    print "Teilnummer: " + str(einzelteile.teilNr),
                    print "Spin: " + str(einzelteile.getSpin())
                    teilPlatz += 1
                sys.exit(0)

        if platz < 9:
            rollen(teileListe, platz+1)

    teileListe[platz-1].setSpin(0)


zahl = 1

def position(bis, ausser, zustand):
    global  zahl
    assert isinstance(ausser, list)
    for i in range(1, bis+1):
        if i not in ausser:

            ausser.append(i)
            zustand.append(i)
            if len(zustand) == bis:

                #print zustand
                if zahl != zustand[0]:
                    print u"stelle1 verändert zu " + str(zustand[0])
                    zahl = zustand[0]
                uebergabe = [teile[zustand[0]-1],
                             teile[zustand[1]-1],
                             teile[zustand[2]-1],
                             teile[zustand[3]-1],
                             teile[zustand[4]-1],
                             teile[zustand[5]-1],
                             teile[zustand[6]-1],
                             teile[zustand[7]-1],
                             teile[zustand[8]-1]]

                rollen(uebergabe, 1)




            position(bis, ausser, zustand)
            ausser.remove(i)
            zustand.remove(i)


zaehler = 0
ausser = list()
zustand = list()
position(9, ausser, zustand)


