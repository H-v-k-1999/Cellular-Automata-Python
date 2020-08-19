# Cellular-Automata-Python
The Conway's Game of Life - Cellular Automata implementation in python.

Different starting positions can result in very different results and might create new possibilities.
The cellular automata is governed by 4 basic principles.

1. If the cell is alive and the COF (Count of neighbour) < 2, the cell dies.
2. If the cell is alive and the 2 <= COF <= 3, the cell remains alive.
3. If the cell is alive and the COF >= 4, the cell dies.
4. If the cell is dead and the COF == 3, the cell revives.
