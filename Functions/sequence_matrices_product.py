memo = []

def bestForm(m, memo, i, j):
	if (j - i) <= 1:
		return 0

	if(memo[i][j-1] != 0):
		return memo[i][j-1]

	minCost = float('inf')
	tempValue = 0
	k_0 = i+1
	for k in range(i+1, j):

		cost_ikj = m[i][0] * m[k][0] * m[j-1][1]

		tempValue = bestForm(m, memo, i, k) + bestForm(m, memo, k, j) + cost_ikj
		if tempValue <= minCost:
			minCost = tempValue
			k_0 = k

	memo[i][j-1] = minCost
	memo[j-1][i] = k_0
	return minCost

def mult(matrixA, matrixB):
	nrow = len(matrixA)
	var = len(matrixA[0])
	ncol = len(matrixB[0])

	matrixC = [ [0] * ncol for i in range(nrow) ]

	for i in range(nrow):
		for j in range(ncol):
			for k in range(var):
				matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

	return matrixC

def multiplyMatrices(matrices, memo, i, j):
	if( j - i <= 1 ):
		return matrices[i]

	if( j - i <= 2):
		return mult(matrices[i], matrices[i+1])

	k = memo[j-1][i]
	return mult(multiplyMatrices(matrices, memo, i, k), multiplyMatrices(matrices, memo, k, j))

def printMatrix(matrix):
	for i in range(len(matrix)):
		print(" ".join(map(str, (matrix[i]))))




n = int(input())
m = []
matrices = []
for i in range(n):
	m.append(list(map(int,input().split(' '))))

	matrices.append([])
	for j in range(m[-1][0]):
		matrices[i].append(list(map(int,input().split(' '))))

memo = [ [0] * n for i in range(n) ]


print('#####################################################')
print('SEQUENCE MATRICES PRODUCT\n')
print('Input matrices: \n')
for matrix in matrices:
    printMatrix(matrix)
    print()
print("The cost is:", bestForm(m, memo, 0,len(m))) # Calculate the cost of the best form of multiplication
print()
print("The final result is:")
printMatrix(multiplyMatrices(matrices, memo, 0, len(m))) # Calculate the actual multiplication
print('#####################################################')
