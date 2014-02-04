'''
Created on 21.09.2013

@author: Johannes
'''

from WindowSudoku2 import Ui_Sudokusolver as UI
import Sudoku as Sudoku
from PyQt4 import QtGui, QtCore
import sys

class textEdit(QtGui.QLineEdit):
    def textEdited(self, parent):
        self.textChanged()
        
class Windows(QtGui.QMainWindow, UI):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, parent=None)
        self.setupUi(self)
        
        self.neuesSudoku()
        self.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.neuesSudoku)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.neuMalen)
    def neuesSudoku(self):
        self.meinFeld = Sudoku.Feld()
        self.le1.setText(str())
        self.le2.setText(str())
        self.le3.setText(str())
        self.le4.setText(str())
        self.le5.setText(str())
        self.le6.setText(str())
        self.le7.setText(str())
        self.le8.setText(str())
        self.le9.setText(str())
        self.le10.setText(str())
        self.le11.setText(str())
        self.le12.setText(str())
        self.le13.setText(str())
        self.le14.setText(str())
        self.le15.setText(str())
        self.le16.setText(str())
        self.le17.setText(str())
        self.le18.setText(str())
        self.le19.setText(str())
        self.le20.setText(str())
        self.le21.setText(str())
        self.le22.setText(str())
        self.le23.setText(str())
        self.le24.setText(str())
        self.le25.setText(str())
        self.le26.setText(str())
        self.le27.setText(str())
        self.le28.setText(str())
        self.le29.setText(str())
        self.le30.setText(str())
        self.le31.setText(str())
        self.le32.setText(str())
        self.le33.setText(str())
        self.le34.setText(str())
        self.le35.setText(str())
        self.le36.setText(str())
        self.le37.setText(str())
        self.le38.setText(str())
        self.le39.setText(str())
        self.le40.setText(str())
        self.le41.setText(str())
        self.le42.setText(str())
        self.le43.setText(str())
        self.le44.setText(str())
        self.le45.setText(str())
        self.le46.setText(str())
        self.le47.setText(str())
        self.le48.setText(str())
        self.le49.setText(str())
        self.le50.setText(str())
        self.le51.setText(str())
        self.le52.setText(str())
        self.le53.setText(str())
        self.le54.setText(str())
        self.le55.setText(str())
        self.le56.setText(str())
        self.le57.setText(str())
        self.le58.setText(str())
        self.le59.setText(str())
        self.le60.setText(str())
        self.le61.setText(str())
        self.le62.setText(str())
        self.le63.setText(str())
        self.le64.setText(str())
        self.le65.setText(str())
        self.le66.setText(str())
        self.le67.setText(str())
        self.le68.setText(str())
        self.le69.setText(str())
        self.le70.setText(str())
        self.le71.setText(str())
        self.le72.setText(str())
        self.le73.setText(str())
        self.le74.setText(str())
        self.le75.setText(str())
        self.le76.setText(str())
        self.le77.setText(str())
        self.le78.setText(str())
        self.le79.setText(str())
        self.le80.setText(str())
        self.le81.setText(str())
    def neuMalen(self):
        
        if self.le1.text() != '':
            self.meinFeld.setFixed(0, 0, int(self.le1.text()))
        if self.le2.text() != '':
            self.meinFeld.setFixed(1, 0, int(self.le2.text()))
        if self.le3.text() != '':
            self.meinFeld.setFixed(2, 0, int(self.le3.text()))
        if self.le4.text() != '':
            self.meinFeld.setFixed(3, 0, int(self.le4.text()))
        if self.le5.text() != '':
            self.meinFeld.setFixed(4, 0, int(self.le5.text()))
        if self.le6.text() != '':
            self.meinFeld.setFixed(5, 0, int(self.le6.text()))
        if self.le7.text() != '':
            self.meinFeld.setFixed(6, 0, int(self.le7.text()))
        if self.le8.text() != '':
            self.meinFeld.setFixed(7, 0, int(self.le8.text()))
        if self.le9.text() != '':
            self.meinFeld.setFixed(8, 0, int(self.le9.text()))
        if self.le10.text() != '':
            self.meinFeld.setFixed(0, 1, int(self.le10.text()))
        if self.le11.text() != '':
            self.meinFeld.setFixed(1, 1, int(self.le11.text()))
        if self.le12.text() != '':
            self.meinFeld.setFixed(2, 1, int(self.le12.text()))
        if self.le13.text() != '':
            self.meinFeld.setFixed(3, 1, int(self.le13.text()))
        if self.le14.text() != '':
            self.meinFeld.setFixed(4, 1, int(self.le14.text()))
        if self.le15.text() != '':
            self.meinFeld.setFixed(5, 1, int(self.le15.text()))
        if self.le16.text() != '':
            self.meinFeld.setFixed(6, 1, int(self.le16.text()))
        if self.le17.text() != '':
            self.meinFeld.setFixed(7, 1, int(self.le17.text()))
        if self.le18.text() != '':
            self.meinFeld.setFixed(8, 1, int(self.le18.text()))
        if self.le19.text() != '':
            self.meinFeld.setFixed(0, 2, int(self.le19.text()))
        if self.le20.text() != '':
            self.meinFeld.setFixed(1, 2, int(self.le20.text()))
        if self.le21.text() != '':
            self.meinFeld.setFixed(2, 2, int(self.le21.text()))
        if self.le22.text() != '':
            self.meinFeld.setFixed(3, 2, int(self.le22.text()))
        if self.le23.text() != '':
            self.meinFeld.setFixed(4, 2, int(self.le23.text()))
        if self.le24.text() != '':
            self.meinFeld.setFixed(5, 2, int(self.le24.text()))
        if self.le25.text() != '':
            self.meinFeld.setFixed(6, 2, int(self.le25.text()))
        if self.le26.text() != '':
            self.meinFeld.setFixed(7, 2, int(self.le26.text()))
        if self.le27.text() != '':
            self.meinFeld.setFixed(8, 2, int(self.le27.text()))
        if self.le28.text() != '':
            self.meinFeld.setFixed(0, 3, int(self.le28.text()))
        if self.le29.text() != '':
            self.meinFeld.setFixed(1, 3, int(self.le29.text()))
        if self.le30.text() != '':
            self.meinFeld.setFixed(2, 3, int(self.le30.text()))
        if self.le31.text() != '':
            self.meinFeld.setFixed(3, 3, int(self.le31.text()))
        if self.le32.text() != '':
            self.meinFeld.setFixed(4, 3, int(self.le32.text()))
        if self.le33.text() != '':
            self.meinFeld.setFixed(5, 3, int(self.le33.text()))
        if self.le34.text() != '':
            self.meinFeld.setFixed(6, 3, int(self.le34.text()))
        if self.le35.text() != '':
            self.meinFeld.setFixed(7, 3, int(self.le35.text()))
        if self.le36.text() != '':
            self.meinFeld.setFixed(8, 3, int(self.le36.text()))
        if self.le37.text() != '':
            self.meinFeld.setFixed(0, 4, int(self.le37.text()))
        if self.le38.text() != '':
            self.meinFeld.setFixed(1, 4, int(self.le38.text()))
        if self.le39.text() != '':
            self.meinFeld.setFixed(2, 4, int(self.le39.text()))
        if self.le40.text() != '':
            self.meinFeld.setFixed(3, 4, int(self.le40.text()))
        if self.le41.text() != '':
            self.meinFeld.setFixed(4, 4, int(self.le41.text()))
        if self.le42.text() != '':
            self.meinFeld.setFixed(5, 4, int(self.le42.text()))
        if self.le43.text() != '':
            self.meinFeld.setFixed(6, 4, int(self.le43.text()))
        if self.le44.text() != '':
            self.meinFeld.setFixed(7, 4, int(self.le44.text()))
        if self.le45.text() != '':
            self.meinFeld.setFixed(8, 4, int(self.le45.text()))
        if self.le46.text() != '':
            self.meinFeld.setFixed(0, 5, int(self.le46.text()))
        if self.le47.text() != '':
            self.meinFeld.setFixed(1, 5, int(self.le47.text()))
        if self.le48.text() != '':
            self.meinFeld.setFixed(2, 5, int(self.le48.text()))
        if self.le49.text() != '':
            self.meinFeld.setFixed(3, 5, int(self.le49.text()))
        if self.le50.text() != '':
            self.meinFeld.setFixed(4, 5, int(self.le50.text()))
        if self.le51.text() != '':
            self.meinFeld.setFixed(5, 5, int(self.le51.text()))
        if self.le52.text() != '':
            self.meinFeld.setFixed(6, 5, int(self.le52.text()))
        if self.le53.text() != '':
            self.meinFeld.setFixed(7, 5, int(self.le53.text()))
        if self.le54.text() != '':
            self.meinFeld.setFixed(8, 5, int(self.le54.text()))
        if self.le55.text() != '':
            self.meinFeld.setFixed(0, 6, int(self.le55.text()))
        if self.le56.text() != '':
            self.meinFeld.setFixed(1, 6, int(self.le56.text()))
        if self.le57.text() != '':
            self.meinFeld.setFixed(2, 6, int(self.le57.text()))
        if self.le58.text() != '':
            self.meinFeld.setFixed(3, 6, int(self.le58.text()))
        if self.le59.text() != '':
            self.meinFeld.setFixed(4, 6, int(self.le59.text()))
        if self.le60.text() != '':
            self.meinFeld.setFixed(5, 6, int(self.le60.text()))
        if self.le61.text() != '':
            self.meinFeld.setFixed(6, 6, int(self.le61.text()))
        if self.le62.text() != '':
            self.meinFeld.setFixed(7, 6, int(self.le62.text()))
        if self.le63.text() != '':
            self.meinFeld.setFixed(8, 6, int(self.le63.text()))
        if self.le64.text() != '':
            self.meinFeld.setFixed(0, 7, int(self.le64.text()))
        if self.le65.text() != '':
            self.meinFeld.setFixed(1, 7, int(self.le65.text()))
        if self.le66.text() != '':
            self.meinFeld.setFixed(2, 7, int(self.le66.text()))
        if self.le67.text() != '':
            self.meinFeld.setFixed(3, 7, int(self.le67.text()))
        if self.le68.text() != '':
            self.meinFeld.setFixed(4, 7, int(self.le68.text()))
        if self.le69.text() != '':
            self.meinFeld.setFixed(5, 7, int(self.le69.text()))
        if self.le70.text() != '':
            self.meinFeld.setFixed(6, 7, int(self.le70.text()))
        if self.le71.text() != '':
            self.meinFeld.setFixed(7, 7, int(self.le71.text()))
        if self.le72.text() != '':
            self.meinFeld.setFixed(8, 7, int(self.le72.text()))
        if self.le73.text() != '':
            self.meinFeld.setFixed(0, 8, int(self.le73.text()))
        if self.le74.text() != '':
            self.meinFeld.setFixed(1, 8, int(self.le74.text()))
        if self.le75.text() != '':
            self.meinFeld.setFixed(2, 8, int(self.le75.text()))
        if self.le76.text() != '':
            self.meinFeld.setFixed(3, 8, int(self.le76.text()))
        if self.le77.text() != '':
            self.meinFeld.setFixed(4, 8, int(self.le77.text()))
        if self.le78.text() != '':
            self.meinFeld.setFixed(5, 8, int(self.le78.text()))
        if self.le79.text() != '':
            self.meinFeld.setFixed(6, 8, int(self.le79.text()))
        if self.le80.text() != '':
            self.meinFeld.setFixed(7, 8, int(self.le80.text()))
        if self.le81.text() != '':
            self.meinFeld.setFixed(8, 8, int(self.le81.text()))
        
        self.meinFeld.Recursion(0, 0)
        self.meinFeld.ausgabe()
        
        
        self.le1.setText(str(self.meinFeld.feld[0][0]))
        self.le2.setText(str(self.meinFeld.feld[0][1]))
        self.le3.setText(str(self.meinFeld.feld[0][2]))
        self.le4.setText(str(self.meinFeld.feld[0][3]))
        self.le5.setText(str(self.meinFeld.feld[0][4]))
        self.le6.setText(str(self.meinFeld.feld[0][5]))
        self.le7.setText(str(self.meinFeld.feld[0][6]))
        self.le8.setText(str(self.meinFeld.feld[0][7]))
        self.le9.setText(str(self.meinFeld.feld[0][8]))
        self.le10.setText(str(self.meinFeld.feld[1][0]))
        self.le11.setText(str(self.meinFeld.feld[1][1]))
        self.le12.setText(str(self.meinFeld.feld[1][2]))
        self.le13.setText(str(self.meinFeld.feld[1][3]))
        self.le14.setText(str(self.meinFeld.feld[1][4]))
        self.le15.setText(str(self.meinFeld.feld[1][5]))
        self.le16.setText(str(self.meinFeld.feld[1][6]))
        self.le17.setText(str(self.meinFeld.feld[1][7]))
        self.le18.setText(str(self.meinFeld.feld[1][8]))
        self.le19.setText(str(self.meinFeld.feld[2][0]))
        self.le20.setText(str(self.meinFeld.feld[2][1]))
        self.le21.setText(str(self.meinFeld.feld[2][2]))
        self.le22.setText(str(self.meinFeld.feld[2][3]))
        self.le23.setText(str(self.meinFeld.feld[2][4]))
        self.le24.setText(str(self.meinFeld.feld[2][5]))
        self.le25.setText(str(self.meinFeld.feld[2][6]))
        self.le26.setText(str(self.meinFeld.feld[2][7]))
        self.le27.setText(str(self.meinFeld.feld[2][8]))
        self.le28.setText(str(self.meinFeld.feld[3][0]))
        self.le29.setText(str(self.meinFeld.feld[3][1]))
        self.le30.setText(str(self.meinFeld.feld[3][2]))
        self.le31.setText(str(self.meinFeld.feld[3][3]))
        self.le32.setText(str(self.meinFeld.feld[3][4]))
        self.le33.setText(str(self.meinFeld.feld[3][5]))
        self.le34.setText(str(self.meinFeld.feld[3][6]))
        self.le35.setText(str(self.meinFeld.feld[3][7]))
        self.le36.setText(str(self.meinFeld.feld[3][8]))
        self.le37.setText(str(self.meinFeld.feld[4][0]))
        self.le38.setText(str(self.meinFeld.feld[4][1]))
        self.le39.setText(str(self.meinFeld.feld[4][2]))
        self.le40.setText(str(self.meinFeld.feld[4][3]))
        self.le41.setText(str(self.meinFeld.feld[4][4]))
        self.le42.setText(str(self.meinFeld.feld[4][5]))
        self.le43.setText(str(self.meinFeld.feld[4][6]))
        self.le44.setText(str(self.meinFeld.feld[4][7]))
        self.le45.setText(str(self.meinFeld.feld[4][8]))
        self.le46.setText(str(self.meinFeld.feld[5][0]))
        self.le47.setText(str(self.meinFeld.feld[5][1]))
        self.le48.setText(str(self.meinFeld.feld[5][2]))
        self.le49.setText(str(self.meinFeld.feld[5][3]))
        self.le50.setText(str(self.meinFeld.feld[5][4]))
        self.le51.setText(str(self.meinFeld.feld[5][5]))
        self.le52.setText(str(self.meinFeld.feld[5][6]))
        self.le53.setText(str(self.meinFeld.feld[5][7]))
        self.le54.setText(str(self.meinFeld.feld[5][8]))
        self.le55.setText(str(self.meinFeld.feld[6][0]))
        self.le56.setText(str(self.meinFeld.feld[6][1]))
        self.le57.setText(str(self.meinFeld.feld[6][2]))
        self.le58.setText(str(self.meinFeld.feld[6][3]))
        self.le59.setText(str(self.meinFeld.feld[6][4]))
        self.le60.setText(str(self.meinFeld.feld[6][5]))
        self.le61.setText(str(self.meinFeld.feld[6][6]))
        self.le62.setText(str(self.meinFeld.feld[6][7]))
        self.le63.setText(str(self.meinFeld.feld[6][8]))
        self.le64.setText(str(self.meinFeld.feld[7][0]))
        self.le65.setText(str(self.meinFeld.feld[7][1]))
        self.le66.setText(str(self.meinFeld.feld[7][2]))
        self.le67.setText(str(self.meinFeld.feld[7][3]))
        self.le68.setText(str(self.meinFeld.feld[7][4]))
        self.le69.setText(str(self.meinFeld.feld[7][5]))
        self.le70.setText(str(self.meinFeld.feld[7][6]))
        self.le71.setText(str(self.meinFeld.feld[7][7]))
        self.le72.setText(str(self.meinFeld.feld[7][8]))
        self.le73.setText(str(self.meinFeld.feld[8][0]))
        self.le74.setText(str(self.meinFeld.feld[8][1]))
        self.le75.setText(str(self.meinFeld.feld[8][2]))
        self.le76.setText(str(self.meinFeld.feld[8][3]))
        self.le77.setText(str(self.meinFeld.feld[8][4]))
        self.le78.setText(str(self.meinFeld.feld[8][5]))
        self.le79.setText(str(self.meinFeld.feld[8][6]))
        self.le80.setText(str(self.meinFeld.feld[8][7]))
        self.le81.setText(str(self.meinFeld.feld[8][8]))
        


app = QtGui.QApplication(sys.argv) 
dialog = Windows() 
dialog.show() 
sys.exit(app.exec_())