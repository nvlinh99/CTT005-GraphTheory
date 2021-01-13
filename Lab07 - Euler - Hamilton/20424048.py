# Matrix = [
# 		[0, 1, 1, 0, 0, 0],
# 		[1, 0, 1, 1, 1, 0],
# 		[1, 1, 0, 1, 1, 0],
# 		[0, 1, 1, 0, 1, 1],
# 		[0, 1, 1, 1, 0, 1],
# 		[0, 0, 0, 1, 1, 0],
# 	]

Matrix = [
	[0, 1, 0, 1, 0],
	[1, 0, 1, 1, 1],
	[0, 1, 0, 0, 1],
	[1, 1, 0, 0, 0],
	[0, 1, 1, 0, 0],
]

startVertex = 0

# EULER 
def Euler(matrix, start):
	stack = [start]
	path = []
	while stack:
		top = stack[-1]
		isEdge = False
		for i in range(len(matrix)):
			if matrix[top][i] == 1:
				matrix[top][i] = -1
				matrix[i][top] = -1
				stack.append(i)
				path.append((i, top))
				isEdge = True
				break
		if isEdge:
			continue
		stack.pop()
		path.reverse()

	for i in range(len(matrix)):
		for j in range(len(matrix)):
			matrix[i][j] *= -1
	
	return path

# HAMILTON
Path = []
Visited = [False] * len(Matrix)

def Hamilton(matrix, start):
	Path.append(start)
	if len(Path)  == len(matrix):
		if matrix[Path[0]][Path[-1]] == 1:
			return Path
		else:
			Path.pop()
			return False
	Visited[start] = True
	for nextVertex in range(len(matrix)):
		if matrix[start][nextVertex] == 1 and not Visited[nextVertex]:
			if Hamilton(matrix, nextVertex):
				return Path
	Visited[start] = False
	Path.pop()
	return False

def main():
	eulerPath = Euler(Matrix, startVertex)
	vertexStart = []
	vertexEnd = []
	if not eulerPath:
		print(-1)
	else:
		# Chuyển từ cặp cạnh sang list đỉnh đầu và cuối của cạnh để kiểm tra chu trình
		for i in eulerPath:
			vertexStart.append(i[0])
			vertexEnd.append(i[1])

		# Kiểm tra có dây chuyền và đỉnh đầu = đỉnh cuối.
		if vertexStart[0] == vertexEnd[-1]:
			print(1)
			print(eulerPath)
		else:
			print(0)
			print(eulerPath)
	
	hamiltonPath = Hamilton(Matrix, startVertex)
	if not hamiltonPath:
		print(-1)
		print(-1) 
	else:
		print(0)
		print(hamiltonPath)	
	
if __name__ == "__main__":
	main()