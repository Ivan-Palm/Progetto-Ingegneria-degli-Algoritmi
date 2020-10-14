# coding: utf-8

import random


def randomArray(length=10, value=100000):
    """ Crea un array random """
    l = []
    for i in range(0, length):
        x = random.randint(0, value)
        l.append(x)
    return l


def check(l):
    """ Funzione che controlla se una lista è ordinata """
    for i in range(0, len(l)-1):
        if l[i] > l[i + 1]:
            print('not ordered')
            return
    print('ordered')
    return


if __name__ == '__main__':
    temp = randomArray()

