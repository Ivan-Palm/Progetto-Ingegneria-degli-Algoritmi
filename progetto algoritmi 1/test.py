# coding: utf-8

import time
import random
import Sorting
from Struct import Array

""" Ogni test esegue un algoritmo di ordinamento differente:
    viene specificato quante volte va ripetuto il test e ne si fa la media dei tempi di esecuzione
    le liste di prova sono generate randomicamente e hanno dimensione:
    0, 100, 1000, 10000, 100000, 200000
    se si necessita di controllare se le liste sono ordinate si può usare la funzione check() definita in Array
"""


def test1(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.selectionSort(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg selectionSort: ', t)
    return


def test2(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.insertionSortDown(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg insertionSortDown: ', t)
    return


def test3(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.insertionSortUp(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg insertionSortUp: ', t)
    return


def test4(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.bubbleSort(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg bubbleSort: ', t)
    return


def test5(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.mergeSort(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg mergeSort: ', t)
    return


def test6(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.quickSort(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg quickSortRandom: ', t)
    return


def test7(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.quickSort(temp, True)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg quickSortDet: ', t)
    return


def test8(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.quickSortPrandom(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg quickSortPrandom: ', t)
    return


def test9(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.heapSort(temp)
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg heapSort: ', t)
    return


def test10(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            Sorting.radixSort(temp, 10000, 10)
            end = time.time() - start
            Array.check(temp)
            t += end
        t = t/rip
        print('avg radixSort: ', t)
    return


def test11(rip):
    random.seed(1)
    dim = [0, 100, 1000, 10000, 100000, 200000]
    t = 0
    for i in range(0, len(dim)):
        print('dim array: ', dim[i])
        array = Array.randomArray(dim[i], 100)
        for j in range(0, rip):
            temp = array
            start = time.time()
            temp.sort()
            end = time.time() - start
            # Array.check(temp)
            t += end
        t = t/rip
        print('avg P-sort:', t)
    return


if __name__ == '__main__':
    print('test eseguiti per 10 volte')
    # test1(10)
    # test2(10)
    # test3(10)
    # test4(10)
    # print('test eseguiti per 100 volte')
    # test5(100)
    # test6(100)
    # test7(100)
    # test8(100)
    # test9(100)
    # test10(100)
    # test11(100)





