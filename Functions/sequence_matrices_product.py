# import copy
# def costOf(mOrigin,i,k,j):
# 	m = copy.deepcopy(mOrigin)
# 	cost = 0
# 	while (k-i) > 1:
# 		m[i][1] = m[i+1][1]
# 		del m[i+1]
# 		k -= 1
# 		j -= 1

# 	while( (j - k) >= 2):

# 		m[k][1] = m[k+1][1]
# 		del m[k+1]
# 		j -= 1

# 	cost = m[i][0]*m[i][1]*m[i+1][1]
# 	return cost
memo = []

def bestForm(m,i,j):
	if (j - i) <= 1:
		return 0

	if(memo[i][j-1] != 0):
		return memo[i][j-1]

	minCost = float('inf')
	tempValue = 0
	k_0 = i+1
	for k in range(i+1,j):

		cost_ikj = m[i][0] * m[k][0] * m[j-1][1]

		tempValue = bestForm(m,i,k) + bestForm(m,k,j) + cost_ikj
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

def multiplyMatrices(matrices, i, j):

	if( j - i <= 1 ):
		return matrices[i]

	if( j - i <= 2):
		return mult(matrices[i], matrices[i+1])

	k = memo[j-1][i]
	return mult(multiplyMatrices(matrices, i, k), multiplyMatrices(matrices, k, j))

def printMatrix(matrix):

	for i in range(len(matrix)):
		print(" ".join(map(str, (matrix[i]))))

n = int(input())
m = []
matrices = []
for i in range(n):
	print("Type the dimensions of the matrix:")
	m.append(list(map(int,input().split(' '))))

	matrices.append([])
	print("Type the matrix:")
	for j in range(m[-1][0]):
		matrices[i].append(list(map(int,input().split(' '))))

memo = [ [0] * n for i in range(n) ]

print("Cost:")
print(bestForm(m,0,len(m)))

print("Result:")
printMatrix(multiplyMatrices(matrices, 0, len(m)))

# while n != 0:

# 	for i in range(n):
# 		m.append(list(map(int,input().split(' '))))

# 	memo = [ [0] * n for i in range(n) ]
# 	memo_matrix = []

# 	print(m)
# 	print(bestForm(m,0,len(m)))
# 	print(memo)
# 	m = []
# 	n = int(input())