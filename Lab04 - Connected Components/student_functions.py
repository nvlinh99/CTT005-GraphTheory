import numpy as np
from collections import defaultdict

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
		return visited, path

def BFS(matrix, start, end):
		"""
		BFS algorithm:
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

def Prim(matrix):
		"""
		Prim algorithm:
		Parameters:
		---------------------------
		matrix: np array 
			The graph's adjacency matrix
		Returns
		---------------------
		edges: list
			List of founded edges in spanning tree (sort by search order)
			example: [[1,2],[3,4],[4,5]]
		"""
		# TODO:
		edges = []
		n_v = matrix.shape[0]
		np.random.seed(0)
		start_v = np.random.randint(0, n_v-1)

		return edges

def Kruskal(matrix):
		"""
		DFS algorithm
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
		edges: list
			List of founded edges in spanning tree (sort by search order)
			example: [(1,2),(3,4),(4,5)]
		"""
		# TODO:
		edges = []
		return edges

def adjMatrixToAdjList1(matrix):
	adjList = defaultdict(list)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] > 0:
				adjList[i].append((i, j))
	return adjList

def conComUtil(neighbors):
	seen = set()
	def component(node):
		nodes = set([node])
		while nodes:
			node = nodes.pop()
			seen.add(node)
			nodes |= neighbors[node] - seen  # In-place OR
			yield node
	
	for node in neighbors:
		if node not in seen:
			yield component(node)

class UnionFind:
	def __init__(self, n):
		self.id = [i for i in range(n)]

	def findRoot(self, p):
		while p != self.id[p]:
			p = self.id[p]
		return p

	def isConnected(self, p, q):
		return self.findRoot(p) == self.findRoot(q)

	def union(self, p, q):
		pRoot = self.findRoot(p)
		qRoot = self.findRoot(q)
		if pRoot == qRoot:
			return
		self.id[pRoot] = qRoot

def ConnectedComponents(matrix):
		"""
		Connected Components
		Parameters:
		---------------------------
		matrix: np array 
		The graph's adjacency matrix

		Returns
		---------------------
		edges: list
			example: [
				[4,6],[5,6],[6,7]], // component 1
				[[1,3],[1,2],[2,0]],  // component 2
				[[9,10],[9,11],[8,10]  // component 3
			]
		"""
		# TODO:
		old_graph = adjMatrixToAdjList1(matrix)
		list_edges = {v for k, vs in old_graph.items() for v in vs}
		graph = defaultdict(set)

		for v1, v2 in list_edges:
			graph[v1].add(v2)
			graph[v2].add(v1)

		components = []
		for component in conComUtil(graph):
			c = set(component)
			components.append([edge for edges in old_graph.values()
												for edge in edges
												if c.intersection(edge)])

		uf = UnionFind(len(matrix))
		edges = []
		for component in components:
			temp = []
			for edge in component:
				pNode, qNode = edge
				if uf.isConnected(pNode, qNode):
					continue
				uf.union(pNode, qNode)
				temp.append(edge)
			edges += [temp]
		return edges