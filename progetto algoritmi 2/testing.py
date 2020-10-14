import datastruct.graph.GraphGenerator as Generator
import detectCycle
import random


seed = random.seed(1)


def testNotCycle(x):
    graph = Generator.graphGeneratorNOTCycle(x)
    y = detectCycle.hasCycleUF(graph)
    z = detectCycle.hasCycleDFS(graph)
    # print('has a cycle UF?', y)
    # print('has a cycle DFS?', z)


def testCycle(x):
    graph = Generator.graphGeneratorNOTCycle(x)
    y = detectCycle.hasCycleUF(graph)
    z = detectCycle.hasCycleDFS(graph)
    # print('has a cycle UF?', y)
    # print('has a cycle DFS?', z)


def testCompleto():
    set = [10, 100, 1000, 10000, 100000]
    print('Testing NOTCycle graphs...')
    for i in set:
        for j in range(0, 10):
            testNotCycle(i)
    print('Testing Cycle graphs...')
    for i in set:
        for j in range(0, 10):
            testCycle(i)
    print('Done')
    return


if __name__ == '__main__':
    testCompleto()
