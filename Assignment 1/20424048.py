'''
	@Họ tên: Nguyễn Vũ Linh
	@MSSV: 20424048
	@Lớp: 20HCB1
	@Môn: TH Lý thuyết đồ thị
'''
'''
	Sample matrix Input:
	Create file input.txt and paste a matrix

	* Undirected Graph
	0 1 0 1
	1 0 2 3
	0 2 0 0
	1 3 0 0

	* Directed Graph
	0 0 1 2
	2 0 -3 0
	0 0 0 4
	0 0 0 0

'''
from collections import defaultdict #Define dictionary

# Func read file without space at the end of line. Use enter to break line.
def readFile():
	with open("input.txt", "rt") as f:
		l = [[int(num) for num in line.split(' ')] for line in f if line.strip() != "" ]
	return l

# Func check matrix get type nxn or not
def isSquare (matrix): 
	return all (len (row) == len (matrix) for row in matrix)

# Func check matrix is scalar matrix (Undirected graph) or not
def isScalarMatrix(matrix):
	if(isSquare(matrix)):
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix)):
				if(matrix[i][j] != matrix[j][i]):
					return False
		return True
	else:
		print("Matrix is invalid!")

def printCheckMatrix(matrix):
	if(isScalarMatrix(matrix)):
		print("0")
	else:
		print("1")

# Func covert matrix to adjacency list
def adjacencyList(matrix):
	adjList = defaultdict(list)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] >= 1:
				adjList[i].append(j)
	return adjList

def printAdjacencyList(matrix):
	AdjList = adjacencyList(matrix)
	for i in AdjList: 
		for j in AdjList[i]: 
			print("{}".format(j), end =" ") 

# Func find degree of vertex scalar matrix
def degreeOfVertexScalar(matrix):
	AdjList = adjacencyList((matrix))
	degree = 0
	dicDegSca = dict()
	for i in range(0, len(matrix)):
		for j in AdjList:
			if i == j:
				degree += 2 * matrix[j][i]
				if i>0:
					degree -= dicDegSca[i-1]
				dicDegSca[i] = degree
			else:
				degree += matrix[j][i]
				dicDegSca[i] = degree
	return dicDegSca

# Func find degree of vertex directed graph
def degreeOfVertexDirected(matrix):
	AdjList = adjacencyList(matrix)
	lenMat = len(matrix)
	degIn = [0] * lenMat
	degOut = [0] * lenMat
	dicDegDir = dict()
	for i in range(0, len(AdjList)):
		List = AdjList[i]
		degOut[i] = len(List)  
		for j in range(0, len(List)):
			degIn[List[j]] += 1
	 
	for k in range(0, lenMat):
		dicDegDir[k] = degIn[k] + degOut[k]		
	return dicDegDir

def printDegreeOfVertex(matrix):
	print()
	if(isScalarMatrix(matrix)):
		degrees = degreeOfVertexScalar(matrix)
		for degree in degrees.values():
			print(degree, end =" ")
	else:
		degrees = degreeOfVertexDirected(matrix)
		for degree in degrees.values():
			print(degree, end =" ")

# Func count type of degree
def typeOfDegree(matrix):
	countEven = 0
	countOdd = 0
	countPendant = 0
	countIsolated = 0
	if(isScalarMatrix(matrix)):
		degrees = degreeOfVertexScalar(matrix)
	else:
		degrees = degreeOfVertexDirected(matrix)

	for degree in degrees.values():
		if degree % 2 == 0:
			countEven += 1
		else:
			countOdd += 1
		if degree == 1:
			countPendant += 1
		if degree == 0:
			countIsolated += 1
	
	print()
	print("{}\n{}\n{}\n{}".format(countEven, countOdd, countPendant, countIsolated))

def menu():
	matrixInput = readFile()
	printCheckMatrix(matrixInput)
	printAdjacencyList(matrixInput)
	printDegreeOfVertex(matrixInput)
	typeOfDegree(matrixInput)
	
if __name__ == "__main__":
	menu()