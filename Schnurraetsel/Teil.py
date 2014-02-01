class Teil:
    def __init__(self, oben, rechts, unten, links, oben2, rechts2, unten2, links2, teilNr):
        self.vorne = [oben, rechts, unten, links]
        self.hinten = [oben2, rechts2, unten2, links2]
        self.vorneSpeicher = [oben, rechts, unten, links]
        self.hintenSpeicher = [oben2, rechts2, unten2, links2]
        self.__spin = 0
        self.__position = 0
        self.teilNr = teilNr

    def vergleich(self, wo):

        if wo == 'oben':
            rueck = self.getTeil()[0].split("-")
            return rueck[1] + "-" + rueck[0]
        if wo == 'rechts':
            rueck = self.getTeil()[1].split("-")
            return rueck[1] + "-" + rueck[0]
        if wo == 'unten':
            rueck = self.getTeil()[2].split("-")
            return rueck[1] + "-" + rueck[0]
        if wo == 'links':
            rueck = self.getTeil()[3].split("-")
            return rueck[1] + "-" + rueck[0]

    def setSpin(self, spin):
        self.__spin = 0
        self.vorne = self.vorneSpeicher[:]
        self.hinten[:] = self.hintenSpeicher[:]

        for i in range(spin % 8):
            self.drehen()

    def getSpin(self):
        return self.__spin

    def drehen(self):
        if self.__spin <= 3:
            self.vorne.insert(0, self.vorne[3])
            self.vorne.pop()
            self.__spin += 1
        else:
            self.hinten.insert(0, self.hinten[3])
            self.hinten.pop()
            if self.__spin >= 8:
                self.__spin = 0
            else:
                self.__spin += 1

    def getSeite(self, wo):
        if wo == 'oben':
            return self.getTeil()[0]
        if wo == 'rechts':
            return self.getTeil()[1]
        if wo == 'unten':
            return self.getTeil()[2]
        if wo == 'links':
            return self.getTeil()[3]


    def getTeil(self):
        if self.__spin < 4:
            return self.vorne
        else:
            return self.hinten

    def setAktPosition(self, pos):
        self.__position = pos

    def getPosition(self):
        return self.__position