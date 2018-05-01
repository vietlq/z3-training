#!/usr/bin/env python3

from z3 import *

'''
Sudoku cell coordinates:
------------------------------
00 01 02 | 03 04 05 | 06 07 08
10 11 12 | 13 14 15 | 16 17 18
20 21 22 | 23 24 25 | 26 27 28
------------------------------
30 31 32 | 33 34 35 | 36 37 38
40 41 42 | 43 44 45 | 46 47 48
50 51 52 | 53 54 55 | 56 57 58
------------------------------
60 61 62 | 63 64 65 | 66 67 68
70 71 72 | 73 74 75 | 76 77 78
80 81 82 | 83 84 85 | 86 87 88
------------------------------
'''

s = Solver()

# Construct Sudoku 2D matrix using Python list comprehension
cells = [[Int('cell%d%d' % (row, col)) for col in range(9)] for row in range(9)]

# http://www.norvig.com/sudoku.html
# http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
puzzle="..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."

# Process text line
cur_row, cur_col = 0, 0

for c in puzzle:
    if c != '.':
        s.add(cells[cur_row][cur_col] == int(c))
    # Move to the next column
    cur_col = cur_col + 1
    # Move to the beginning of the next row
    if cur_col == 9:
        cur_col = 0
        cur_row = cur_row + 1

# Make sure all cells are within [1; 9] for correctness
for r in range(9):
    for c in range(9):
        s.add(cells[r][c] >= 1)
        s.add(cells[r][c] <= 9)

# For 9 rows
for r in range(9):
    s.add(Distinct(
        cells[r][0],
        cells[r][1],
        cells[r][2],
        cells[r][3],
        cells[r][4],
        cells[r][5],
        cells[r][6],
        cells[r][7],
        cells[r][8]))

# For 9 colums
for c in range(9):
    s.add(Distinct(
        cells[0][c],
        cells[1][c],
        cells[2][c],
        cells[3][c],
        cells[4][c],
        cells[5][c],
        cells[6][c],
        cells[7][c],
        cells[8][c]))

# Enumerate all squares
for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        # Add constraints for each 3*3 square
        s.add(Distinct(
            cells[r][c],
            cells[r][c+1],
            cells[r][c+2],
            cells[r+1][c],
            cells[r+1][c+1],
            cells[r+1][c+2],
            cells[r+2][c],
            cells[r+2][c+1],
            cells[r+2][c+2]))

print(s.check())
m = s.model()

for r in range(9):
    for c in range(9):
        sys.stdout.write(str(m[cells[r][c]]) + " ")
    print("")
