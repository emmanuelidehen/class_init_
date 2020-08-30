#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 08:24:56 2020

@author: emmanuelidehen
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
        
        #using the the person class to create an object, then execute the printmane object
x = Person("Emmanuel"," Idehen")
x.printname()
        
class Car(Person):
    def __init__(self, model, year):
        self.carmodel = model
        self.caryear = year
       
    def carprintname(self):
        print(self.carmodel, self.caryear)
        
y = Car("Toyota", " 2006")
y.carprintname()


        


        