# coding: utf-8

import random
import Sorting


def trivialSelect(l, k):
    """ Trova il mediano per k molto piccoli """
    length = len(l)
    if k <= 0 or k > length:
        return None
    for i in range(0, k):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]
    return l[k - 1][1]


def sampleMedianSelect(l, left, right, m):
    """ Funzione che trova il mediamo di un sottoarray e lo mette per primo elemento"""
    temp = []
    for i in range(0, m):   # crea una sottolista di dimensione m di tuple (valore, indice) da una lista
        v = random.randint(left, right)
        elem = (l[v], v)
        temp.append(elem)
    if len(temp) <= 3:  # se k è piccolo conviene usare il trivialSelect()
        mid = trivialSelect(temp, int(m/2)+1)
        l[left], l[mid] = l[mid], l[left]   # scambia il primo elemento con il mediano della sottolista
        return
    Sorting.mergeSort(temp)
    k = int(m / 2) + 1
    mid = temp[k][1]
    l[left], l[mid] = l[mid], l[left]   # scambia il primo elemento con il mediano della sottolista
    return


if __name__ == '__main__':
    List = [(7, 9), (5, 2), (3, 4)]
    # mid = trivialSelect(l, 2)
    # print(mid)

