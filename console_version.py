import random # For random initial position
import os # For proper display in console

N = 40 # Size of the grid (40 x 40)

# 8 neighbours of any cell in the grid
nI = [-1, -1, -1, 0, 1, 1,  1,  0]
nJ = [-1,  0,  1, 1, 1, 0, -1, -1]

# * alive
# _ dead

# This will terminate the program if all the cells die.
def allZero(matrix):

	for i in matrix:
		for j in i:
			if j == '*':
				return False

	return True

# Updating the M2 grid on the basis of M1 grid.
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


# Two grids to update alternatively

M1 = [['_' for _ in range(N)]
		 for __ in range(N)]

M2 = [['_' for _ in range(N)]
		 for __ in range(N)]

# Randon starting position for the grid
for i in range(300):
	x, y = random.randint(0, N-1), random.randint(0, N-1)
	M1[x][y] = '*'


while not allZero(M1) or allZero(M2):

	# To clear the screen so matrix gets printed in the same position
	os.system('cls')

	# Printing the grid
	for i in M1:
		for j in i:
			print(j + " ", end="")
		print()
	print()

	cellularAutomate(M1, M2) # Calling the update function
	M1 = M2[:] #Copying M2 in M1
