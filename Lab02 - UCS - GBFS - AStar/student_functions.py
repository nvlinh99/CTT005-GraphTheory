import numpy as np
from collections import defaultdict
from collections import deque 
from heapq import heappop, heappush

def adjMatrixToAdjList(matrix):
    adjList = defaultdict(list) 
    for i in range(len(matrix)):
            for j in range(len(matrix[i])): 
                if matrix[i][j] > 0:
                    adjList[i].append(j) 
    return adjList

def dfsToFindSortPath(matrix, startNode):
    adjList = adjMatrixToAdjList(matrix)
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

def indexVertex(n, vertex):
    """
    :param index:
    :return row, col:
    """
    return vertex % n, vertex // n

def manhattanDistance(n, start, end):
    start_x, start_y = indexVertex(n, start)
    end_x, end_y = indexVertex(n, end)
    return abs(start_x - end_x) + abs(start_y - end_y)

def pathRollBack(matrix, vPath, start, end):
    path = []
    n = len(matrix)
    def pathTravelsal(s, f):
      nonlocal path
      f_x, f_y = indexVertex(n, f)
      if s == f:
        path.append(f)
      else:
        if vPath[f_x][f_y] == -1:
            path.append(-1)
        else:
            pathTravelsal(s, vPath[f_x][f_y])
            path.append(f)

    pathTravelsal(start, end)
    return path

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
    visited = {start: -1}
    n = len(matrix)
    vPath = [[-1 for _ in range(n)] for _ in range(n)]
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    pQueue = [(0, start)]
    sx, sy = indexVertex(n, start)
    dist[sx][sy] = 0
    graph = adjMatrixToAdjList(matrix)
    while pQueue:
      _, top = heappop(pQueue)
      visited[top] = start
      top_x, top_y = indexVertex(n, top)
      if top == end:
          break
      for neighbor in sorted(graph[matrix[top_x][top_y]]):
          n_x, n_y = indexVertex(n, neighbor)
          if dist[n_x][n_y] > dist[top_x][top_y] + 1:
              dist[n_x][n_y] = dist[top_x][top_y] + 1
              vPath[n_x][n_y] = top
              heappush(pQueue, (dist[n_x][n_y], neighbor))

    path = pathRollBack(matrix, vPath, start, end)
    print(visited)
    return visited, path

def BestFS(matrix, start, end):
    path = []
    visited = {start: -1}
    n = len(matrix)
    vPath = [[-1 for _ in range(n)] for _ in range(n)]
    discovered = [[False for _ in range(n)] for _ in range(n)]
    pQueue = [(manhattanDistance(n, start, end), start)]
    start_x, start_y = indexVertex(n, start)
    discovered[start_x][start_y] = True
    graph = adjMatrixToAdjList(matrix)
    while pQueue:
      _, top = heappop(pQueue)
      print(visited)
      visited[top] = start
      top_x, top_y = indexVertex(n, top)
      if top == end:
        break
      for neighbor in sorted(graph[matrix[top_x][top_y]]):
        n_x, n_y = indexVertex(n, neighbor)
        h = manhattanDistance(n, neighbor, end)
        if not discovered[n_x][n_y]:
          discovered[n_x][n_y] = True
          vPath[n_x][n_y] = top
          heappush(pQueue, (h, neighbor))
    print(vPath)
    path = pathRollBack(matrix, vPath, start, end)
    print(visited)
    return visited,path

def AStar(matrix, start, end, pos):
    path = []
    visited = {start: -1}
    n = len(matrix)
    vPath = [[-1 for _ in range(n)] for _ in range(n)]
    discovered = [[False for _ in range(n)] for _ in range(n)]
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    pQueue = [(manhattanDistance(n, start, end) + 0, start)]
    start_x, start_y = indexVertex(n, start)
    dist[start_x][start_y] = 0
    discovered[start_x][start_y] = True
    graph = adjMatrixToAdjList(matrix)
    while pQueue:
      _, top = heappop(pQueue)
      visited[top] = start
      top_x, top_y = indexVertex(n, top)
      if top == end:
        break
      for neighbor in sorted(graph[matrix[top_x][top_y]]):
        n_x, n_y = indexVertex(n, neighbor)
        h = manhattanDistance(n, neighbor, end)
        print(h)
        g = dist[n_x][n_y] = dist[top_x][top_y] + 1
        # print(g)
        if not discovered[n_x][n_y]:
          discovered[n_x][n_y] = True
          vPath[n_x][n_y] = top
          heappush(pQueue, (h + g, neighbor))

    path = pathRollBack(matrix, vPath, start, end)
    print(visited)
    return visited, path