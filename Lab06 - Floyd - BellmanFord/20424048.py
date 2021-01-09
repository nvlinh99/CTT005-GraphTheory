def floydAlgorithm(matrix):
    n = len(matrix)
    floydMatrix = matrix[:]
    t = tuple(range(n))
    floydPath = [list(t) for i in range(n)]

    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or j == i:
                    continue
                if floydMatrix[i][k] == 0 or floydMatrix[k][j] == 0:
                    continue
                newDistance = floydMatrix[i][k] + floydMatrix[k][j]
                if newDistance < floydMatrix[i][j] or floydMatrix[i][j] == 0:
                    floydMatrix[i][j] = newDistance
                    floydPath[i][j] = k
    return floydMatrix, floydPath

def findPathFloyd(pathMatrix, start, end):
    path = [start, end]
    current = end
    while pathMatrix[start][current] != current:
        current = pathMatrix[start][current]
        path.insert(1, current)
    return path

def initialDistancesBellman(lenMatrix, distances, start):
		inf = float("inf")
		for i in range(lenMatrix):
				if i != start:
						distances.append(inf)
				else:
						distances.append(0)

		return distances

def bellmanAlgorithm(matrix, start):
		start -= 1
		distances = []
		size = len(matrix[start])
		distances = initialDistancesBellman(size, distances, start)
		for i in range(size - 1):
				for u in range(size):
						for v in range(size):
								if matrix[u][v] != 0:
										new_dist = distances[u] + matrix[u][v]
										if new_dist < distances[v]:
												distances[v] = new_dist
		return distances

def findPathBellMan(distances, start):
	for i in range(len(distances)):
		print("{}->{}| Khoang cach = {}".format(str(start),str(i+1), str(distances[i])))

def main():
	# matrix = [
	# 	[0, 10, 0, 0, 0, 8],
	# 	[0, 0, 0, 2, 0, 0],
	# 	[0, 1, 0, 0, 0, 0],
	# 	[0, 0, -2, 0, 0, 0],
	# 	[0, -4, 0, -1, 0, 0], 
	# 	[0, 0, 0, 0, 1, 0]
	# ]
	matrix = [
		[5, 3, 0, 0, 7, 0, 0, 0, 0], 
		[6, 0, 0, 1, 9, 5, 0, 0, 0], 
		[0, 9, 8, 0, 0, 0, 0, 6, 0], 
		[8, 0, 0, 0, 6, 0, 0, 0, 3], 
		[4, 0, 0, 8, 0, 3, 0, 0, 1], 
		[7, 0, 0, 0, 2, 0, 0, 0, 6], 
		[0, 6, 0, 0, 0, 0, 2, 8, 0], 
		[0, 0, 0, 4, 1, 9, 0, 0, 5], 
		[0, 0, 0, 0, 8, 0, 0, 7, 9]
		]

	Distance, Route = floydAlgorithm(matrix)
	for i in Distance:
		for j in i:
			print(j, end=" ")
		print()

	startFrom = 1
	print("=======================")
	print("Result: Floyd Algorithm")
	for i in range(len(matrix)):
		if(i != startFrom):
			allDisFloyd = Distance[startFrom][i]
			allPathFloyd = findPathFloyd(Route, startFrom, i)
			print('{}->{}| Khoang cach = {}'.format(allPathFloyd[0], allPathFloyd[-1], allDisFloyd))

	print("=======================")
	print("Result: Bellman Algorithm")
	distances = bellmanAlgorithm(matrix, startFrom)
	findPathBellMan(distances, startFrom)

if __name__ == "__main__":
	main()