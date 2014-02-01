#-*- coding: utf-8 -*-
from __future__ import division
import bruch

__author__ = 'JPaehr'

zahl1 = bruch.Bruch(-3, 4)
zahl2 = bruch.Bruch(5, 6)

print "Zahl1: "
zahl1.Ausgabe()
print ""

print "Zahl2: "
zahl2.Ausgabe()
print ""

print "Addition"
(zahl1+zahl2).Ausgabe()
print ""

print "Subtraktion"
(zahl1-zahl2).Ausgabe()
print ""

print "Multiplikation"
(zahl1*zahl2).Ausgabe()
print ""

print "Division"
(zahl1/zahl2).Ausgabe()
print ""
