'''
Created on 21.09.2013

@author: Johannes
'''
x = 1
for i in range(9):
    for y in range(9):
        print "if self.le"+str(x)+".text() != '':"            
        print "    self.meinFeld.setFixed("+str(y)+", "+str(i)+", int(self.le"+str(x)+".text()))"
        x+=1