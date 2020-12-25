import numpy as np
from collections import defaultdict
from collections import deque


def adjMatrixToAdjList(matrix):
    adjList = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                adjList[i].append(j)
    return adjList


def dfsToFindSortPath(matrix, startNode):
    adjList = adjMatrixToAdjList(matrix)
    print(adjList)
    stack = [(-1, startNode)]
    discovered = set([startNode])
    while stack:
        neighbor, node = stack.pop()
        yield neighbor, node
        newSetNode = set(adjList[node]) - discovered
        discovered.update(newSetNode)
        for newNeighbor in newSetNode:
            stack.extend([(node, newNeighbor)])


def bfsToFindSortPath(matrix, startNode):
    adjList = adjMatrixToAdjList(matrix)
    queue = deque([(-1, startNode)])
    discovered = set([startNode])
    while queue:
        neighbor, node = queue.popleft()
        yield neighbor, node
        newSetNode = set(adjList[node]) - discovered
        discovered.update(newSetNode)
        for newNeighbor in newSetNode:
            queue.extend([(node, newNeighbor)])


def DFS(matrix, start, end):
    """
    DFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node

    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:
    path = []
    visited = {}

    for aNeighbor, currentNode in dfsToFindSortPath(matrix, start):
        visited[currentNode] = aNeighbor
        if currentNode == end:
            revPath = [end]
            while True:
                aNeighbor = visited[currentNode]
                revPath.append(aNeighbor)
                print(visited)
                if aNeighbor == start:
                    break
                currentNode = aNeighbor
            path = list(reversed(revPath))
            return visited, path


def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node

    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO:
    path = []
    visited = {}

    for aNeighbor, currentNode in bfsToFindSortPath(matrix, start):
        visited[currentNode] = aNeighbor
        if currentNode == end:
            revPath = [end]
            while True:
                aNeighbor = visited[currentNode]
                revPath.append(aNeighbor)
                print(visited)
                if aNeighbor == start:
                    break
                currentNode = aNeighbor
            path = list(reversed(revPath))
            return visited, path


def UCS(matrix, start, end, pos):
    """
    Uniform Cost Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:
    path = []
    visited = {}
    return visited, path
