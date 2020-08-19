import random
import os

N = 40
nI = [-1, -1, -1, 0, 1, 1,  1,  0]
nJ = [-1,  0,  1, 1, 1, 0, -1, -1]

# * alive
# _ dead

def allZero(matrix):

	for i in matrix:
		for j in i:
			if j == '*':
				return False

	return True

def cellularAutomate(M1, M2):

	for i in range(N):
		for j in range(N):

			liveCells = 0

			for move in range(8):
				if 0 <= i + nI[move] < N and 0 <= j + nJ[move] < N and M1[i + nI[move]][j + nJ[move]] == '*':
					liveCells += 1

			if M1[i][j] == '*':

				if liveCells < 2:
					M2[i][j] = '_'

				if 2 <= liveCells <= 3:
					M2[i][j] = '*'

				if liveCells >= 4:
					M2[i][j] = '_'

			elif liveCells == 3:
				M2[i][j] = '*'



M1 = [['_' for _ in range(N)]
		 for __ in range(N)]

M2 = [['_' for _ in range(N)]
		 for __ in range(N)]

for i in range(300):
	x, y = random.randint(0, N-1), random.randint(0, N-1)
	M1[x][y] = '*'


while not allZero(M1) or allZero(M2):

	os.system('cls')

	for i in M1:
		for j in i:
			print(j + " ", end="")
		print()
	print()

	cellularAutomate(M1, M2)
	M1 = M2[:]