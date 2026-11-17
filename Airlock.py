# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:12:21 2026

@author: Jad.ayoub
"""

class Airlock:
    def __init__(self, code):
        self.code = code
        self.__sealed = False
    def is_sealed(self):
        return self.__sealed
    def __lock_bolts(self):
        print('Bolts locked')
    def __unlock_bolts(self):
        print('Bolts unlocked')
    def seal(self):
        if self.__sealed == True:
            print('Already sealed.')
        else:
            self.__lock_bolts()
            self.__sealed = True
            print('Airlock sealed.')
    def unseal(self):
        if self.__sealed == False:
            print('Already open.')
        else:
            self.__unlock_bolts()
            self.__sealed = False
            print('Airlock sealed.')
    def __str__(self):
        if self.__sealed == False:
            return 'Airlock ' + self.code + ':  ' + 'open'
        else:
            return 'Airlock ' + self.code + ':  ' + 'sealed'
def main():
    a = Airlock("H1")
    print(a)
    a.seal()
    print(a.is_sealed())
    a.seal()
    a.unseal()
    print(a)
    a.unseal()
main()
