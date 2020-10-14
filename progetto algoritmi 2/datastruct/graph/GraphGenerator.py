from datastruct.graph.Graph_AdjacencyList import GraphAdjacencyList as Graph
import random


random.seed(1)


def graphGeneratorNOTCycle(nodes):
    """
    Crea un grafo non orientato connesso senza cicli
    """

    graph = Graph()
    dump_node = []
    connected_node = []

    # aggiungo i nodi
    for i in range(0, nodes):
        graph.addNode(i)
        dump_node.append(i)

    # crea gli archi
    while len(dump_node) != 0:
        if len(connected_node) == 0:
            elem = random.choice(dump_node)     # scelgo un elemento casuale da dump_node
            connected_node.append(elem)
            dump_node.remove(elem)
        else:
            u = random.choice(connected_node)   # scelgo un elemento casuale da connected_node
            v = random.choice(dump_node)        # scelgo un elemento casuale da dump_node
            connected_node.append(v)
            dump_node.remove(v)
            graph.insertEdge(u, v)              # creo l'arco (u, v)
    return graph


def graphGeneratorCycle(nodes):
    """
    Crea un grafo non orientato connesso con almeno un ciclo
    """

    graph = graphGeneratorNOTCycle(nodes)

    # crea archi tra elementi successivi, l'ulimo elemento è collegato al primo
    for i in range(0, nodes):
        succ = (i+1) % nodes
        if not graph.isAdj(i, succ):
            graph.insertEdge(i, succ)
    return graph


if __name__ == '__main__':
    x = graphGeneratorNOTCycle(8)
    x.print()
    print('\n')
    y = graphGeneratorCycle(8)
    y.print()
