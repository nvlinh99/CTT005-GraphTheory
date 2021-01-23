import numpy as np
from collections import deque

def BFS(matrix, flowMatrix, s, t):
	#TODO
	path=[]
	visited={s: []}
	queue = []
	queue.append([s])
	if s == t:
		return visited[s]
	while queue:
		path = queue.pop(0)
		n = len(path)
		node = path[n-1]
		for v in range(len(matrix)):
			if (matrix[node][v] - flowMatrix[node][v] > 0) and v not in visited:
				visited[v] = visited[node] + [(node, v)]
				if v == t:
					return visited[v]
				new_path = list(path)
				new_path.append(v)
				queue.append(new_path)
	return None

def FordFulkerson(matrix, s, t):
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
		flow_matrix: maximum flow network
		max_flow: maximum flow possible
		"""
		# TODO:
		n = len(matrix)
		flow_matrix = [[0] * n for i in range(n)]
		pathFlow = BFS(matrix, flow_matrix, s, t)
		while pathFlow != None:
			flow = min(matrix[u][v] - flow_matrix[u][v] for u, v in pathFlow)
			for u, v in pathFlow:
				flow_matrix[u][v] += flow
				flow_matrix[v][u] -= flow
			pathFlow = BFS(matrix, flow_matrix, s, t)
		
		max_flow = sum(flow_matrix[s][i] for i in range(n))
		flow_matrix = np.array(flow_matrix)

		print("Matrix flow: \n", flow_matrix)
		print("Maximum flow = ", max_flow)
		return flow_matrix, max_flow