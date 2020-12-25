import numpy as np
import heapq

def DFS(matrix, start, end):
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
	 
	 
		path=[]
		visited={}
		
		return visited, path

def BFS(matrix, start, end):
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
		visited 
				The dictionary contains visited nodes: each key is a visited node, 
				each value is the key's adjacent node which is visited before key.
		path: list
				Founded path
		"""

		# TODO: 
		
		path=[]
		visited={}
	 
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
		path=[]
		visited={}
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
		edges=[] #NOTE: Matrix => Weights in pygame's screen incorrect
		visited = []
		visited.append(0) #Default start at 0
		while len(visited) != len(matrix):
			stack = []
			for currentNode in visited:
				for nextNode in range(len(matrix)):
					weight = matrix[currentNode][nextNode]
					if nextNode not in visited and weight != 0:
						heapq.heappush(stack,(weight, currentNode, nextNode))
			weight, currentNode, nextNode = heapq.heappop(stack)
			edge = [currentNode, nextNode]
			edges.append(edge)
			visited.append(edge[1])
		return edges

class UnionFind: #NOTE: Use for KruskalAlgo
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

def Kruskal(matrix):
		"""
		Kruskal algorithm
		 Parameters:
		---------------------------
		matrix: np array 
				The graph's adjacency matrix	
		Returns
		---------------------
	 edges: list
				List of founded edges in spanning tree (sort by search order)
				example: [(1,2),(3,4),(4,5)]
		""" 
		# TODO: 
		edges = [] #NOTE: Matrix => Weights in pygame's screen incorrect 
		visited = []
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if matrix[i][j] != 0 and (j, i) not in visited:
					visited.append((i, j))
		sortedEdges = sorted(visited, key=lambda edge:matrix[edge[0]][edge[1]])
		uf = UnionFind(len(matrix))
		for edge in sortedEdges:
			pNode, qNode = edge
			if uf.isConnected(pNode, qNode):
				continue
			uf.union(pNode, qNode)
			edges.append(edge)
		return edges