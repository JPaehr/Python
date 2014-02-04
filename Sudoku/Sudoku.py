'''
Created on 20.09.2013

@author: Johannes
'''
import sys

class Topf(object):
    def __init__(self):
        
        self.part = []
        for i in range(1, 4):
            self.part.append([range(1, 10) for a in range(1, 4)])
        self.rows = []
        for i in range(9):
            self.rows.append(range(1, 10))    
        self.columns = []
        for i in range(9):
            self.columns.append(range(1, 10))        
    def getCols(self):
        return self.columns
    def getRows(self):
        return self.rows
    def getPart(self):
        return self.part
    
    def delInCol(self, x, value):
        self.columns[x].remove(value)
    def delInRow(self, y, value):
        self.rows[y].remove(value)
    def delInPart(self, x, y, value):
        # x und y sind in koordinatenform nicht partform anzugeben
        TopfListPart = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        self.part[TopfListPart[x]][TopfListPart[y]].remove(value)
    def ReturnInRow(self, y, value):
        self.rows[y].append(value)
    def ReturnInCol(self, x, value):
        self.columns[x].append(value)
    def ReturnInPart(self, x, y, value):
        TopfListPart = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        self.part[TopfListPart[x]][TopfListPart[y]].append(value)
    def getTopf(self, x, y):
        TopfListPart = [0, 0, 0, 1, 1, 1, 2, 2, 2]
       
        liste = self.__ListenVergleich(self.rows[y], self.columns[x], self.part[TopfListPart[x]][TopfListPart[y]])
        
        return liste
    def useValue(self, x, y, value):
        self.delInCol(x, value)
        self.delInRow(y, value)
        self.delInPart(x, y, value)
        
    def returnValue(self, x, y, value):
        self.ReturnInCol(x, value)
        self.ReturnInPart(x, y, value)
        self.ReturnInRow(y, value)
        
    def __ListenVergleich(self, liste1, liste2, liste3=0):
        listAusgabe = []
        if liste3 == 0:
                
            for i in liste1:
                if liste2.count(i) == 1:
                    listAusgabe.append(i)
                    
            return listAusgabe
        else:
            return self.__ListenVergleich(self.__ListenVergleich(liste1, liste2), liste3)
        
class Feld(object):
    def __init__(self):
        self.feld = [[0 for a in range(9)] for i in range(9)]
        self.topf = Topf()
        self.fixed = [[False for a in range(9)] for i in range(9)]
    def setFixed(self, x, y, value):
        self.feld[y][x] = value
        self.fixed[y][x] = True
        self.topf.useValue(x, y, value)
    def getFeld(self):
        return self.feld 
    def ReadyCheck(self):
        
        for y in range(9):
            for x in range(9):
                if self.feld[y][x] == 0:
                    return False
                
        return True
    def ausgabe(self):
        for i in range(9):
            print self.feld[i]
    def XYNeu(self, x, y):
        if x == 8 and y == 8:
            return [0, 0, False]
        if x < 8:
            return [x + 1, y, True]
        else:
            if y < 8:
                return [0, y + 1, True]
            
    def Recursion(self, x, y):
        if self.ReadyCheck():
            return True
        if self.fixed[y][x]:
            xNeu = self.XYNeu(x, y)[0]
            yNeu = self.XYNeu(x, y)[1]
            self.Recursion(xNeu, yNeu)
            
            return True
        
        else:    
            for i in self.topf.getTopf(x, y):
                
                if self.ReadyCheck():
                    return True
                
                self.feld[y][x] = i
                self.topf.useValue(x, y, i)
                xNeu = self.XYNeu(x, y)[0]
                yNeu = self.XYNeu(x, y)[1]
                self.Recursion(xNeu, yNeu)
                self.topf.returnValue(x, y, i)
                
            return True
"""

meinFeld = Feld()

meinFeld.setFixed(3, 0, 5)

meinFeld.setFixed(0, 1, 7)
meinFeld.setFixed(2, 1, 5)
meinFeld.setFixed(6, 1, 4)
meinFeld.setFixed(8, 1, 3)

meinFeld.setFixed(0, 3, 8)
meinFeld.setFixed(2, 3, 4)
meinFeld.setFixed(3, 3, 3)
meinFeld.setFixed(6, 3, 7)
meinFeld.setFixed(8, 3, 2)

meinFeld.setFixed(1, 2, 3)
meinFeld.setFixed(5, 2, 8)
meinFeld.setFixed(6, 2, 5)
meinFeld.setFixed(7, 2, 9)

meinFeld.setFixed(2, 4, 3)
meinFeld.setFixed(4, 4, 1)
meinFeld.setFixed(6, 4, 9)

meinFeld.setFixed(0, 5, 5)
meinFeld.setFixed(2, 5, 9)
meinFeld.setFixed(5, 5, 7)
meinFeld.setFixed(6, 5, 3)
meinFeld.setFixed(8, 5, 4)


meinFeld.setFixed(1, 6, 5)
meinFeld.setFixed(2, 6, 1)
meinFeld.setFixed(3, 6, 2)
meinFeld.setFixed(7, 6, 7)

meinFeld.setFixed(0, 7, 3)
meinFeld.setFixed(2, 7, 7)
meinFeld.setFixed(6, 7, 2)
meinFeld.setFixed(8, 7, 5)

meinFeld.setFixed(5, 8, 4)
#meinFeld.ausgabe()
meinFeld.Recursion(0, 0)
meinFeld.ausgabe()
"""