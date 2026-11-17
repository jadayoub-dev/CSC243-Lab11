# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:08:38 2026

@author: Jad.ayoub
"""

class ScubaTank:
    def __init__(self, label, bar):
        self.label = label
        self.__bar = bar
    def get_bar(self):
        return self.__bar
    def get_label(self):
        return self.label
    def set_bar(self, bar):
        if 0 <= bar <= 300:
            self.__bar = bar 
        else:
            print('Invalid pressure.')
            return self.__bar
    def fill(self, amount):
        if amount > 0:
            self.__bar += amount 
        else:
            print('Invalid amount.') 
    def release(self, amount):
        if amount <= 0:
            print('Invalid amount.')
        elif amount > self.__bar:
            print('Not enough air.')
        else:
            new =  self.__bar = self.__bar - amount
            return new
    def __str__(self):
        return 'Tank ' + self.label + ': ' + str(self.__bar) + ' bar'
def transfer_air(source, target, amount):
    if amount <= 0:
        print('Invalid amount')
    elif source.get_bar() < amount:
        print('Not enough air')
    else:
        source.set_bar(source.get_bar() - amount)
        target.set_bar(target.get_bar() + amount)
def main():
    src = ScubaTank("A", 150)
    dst = ScubaTank("B", 20)
    transfer_air(src, dst, 50)
    print(src)
    print(dst)
    transfer_air(src, dst, 120)
    print(src.get_bar())
    print(dst.get_bar())
main()
