from datastruct.unionfind.quickUnion import QuickUnionBalancedPathCompression as UnionFind
from datastruct.graph.GraphGenerator import graphGeneratorNOTCycle, graphGeneratorCycle
import random
import time


def decorator(funct):
    """
    Decorator per le funzioni hasCycleUF() e hasCycleDFS():
    salva su due file (result_hasCycleUF.txt e result_hasCycleUF.txt)
    il tempo di esecuzione t e il numero di archi n del grafo nel formato
    n: <archi>  t: <tempo>

    ATTENZIONE: se i file dei risultati sono già esistenti i nuovi risultati in coda
    """

    def wraping_function(*args, **kwargs):
        start = time.time()
        value = funct(*args, **kwargs)
        enlapsed = time.time() - start
        in_file = open(f'result_{funct.__name__}.txt', 'a')
        in_file.write(f'n: {value[1]} \tt: {enlapsed}\n')
        in_file.close()
        return value[0]
    return wraping_function


@decorator
def hasCycleUF(graph):
    """
    Verifica se il grafo dato ha un ciclo o meno
    Implementato con la struttura dati Union-Find
    """

    edgs = len(graph.getEdges())

    # initialize the Union-Find
    uf = UnionFind()
    for i in range(len(graph.nodes)):
        uf.makeSet(graph.nodes[i])

    # scan edges
    for edge in graph.getEdges():
        r1 = uf.findRoot(uf.nodes[edge.tail])
        r2 = uf.findRoot(uf.nodes[edge.head])
        # connect, if not connected
        if r1 != r2:
            uf.union(r1, r2)  # merge sets within the Union-Find
        else:
            return [True, edgs]
    return [False, edgs]


@decorator
def hasCycleDFS(graph):
    """
    Verifica se il grafo dato ha un ciclo o meno
    Esegue una visita DFS, se torna su un nodo marcato come esplorato
    allora esiste un ciclo
    """

    edgs = len(graph.getEdges())

    # sceglie un nodo casuale su cui effettuare la DFS
    set = graph.getNodes()
    x = random.randrange(0, len(set))
    # esegue una variante della visita DFS
    return [graph.dfsCycle(x), edgs]


if __name__ == '__main__':

    x = graphGeneratorNOTCycle(10)
    y = hasCycleUF(x)
    z = hasCycleDFS(x)
    print('has a cycle UF?', y)
    print('has a cycle DFS?', z)
    print('\n')
    x = graphGeneratorNOTCycle(10)
    y = hasCycleUF(x)
    z = hasCycleDFS(x)
    print('has a cycle UF?', y)
    print('has a cycle DFS?', z)
