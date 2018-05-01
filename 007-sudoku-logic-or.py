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
cells = [[BitVec('cell%d%d' % (row, col), 16) for col in range(9)] for row in range(9)]

# http://www.norvig.com/sudoku.html
# http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
puzzle="..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."

# Process text line
cur_row, cur_col = 0, 0

for c in puzzle:
    if c != '.':
        s.add(cells[cur_row][cur_col] == BitVec(int(c), 16))
    # Move to the next column
    cur_col = cur_col + 1
    # Move to the beginning of the next row
    if cur_col == 9:
        cur_col = 0
        cur_row = cur_row + 1

one = BitVecVal(1, 16)
mask = BitVecVal(0b1111111110, 16)

# For 9 rows
for r in range(9):
    s.add((
        (one << cells[r][0]) |
        (one << cells[r][1]) |
        (one << cells[r][2]) |
        (one << cells[r][3]) |
        (one << cells[r][4]) |
        (one << cells[r][5]) |
        (one << cells[r][6]) |
        (one << cells[r][7]) |
        (one << cells[r][8])) == mask)

# For 9 colums
for c in range(9):
    s.add((
        (one << cells[0][c]) |
        (one << cells[1][c]) |
        (one << cells[2][c]) |
        (one << cells[3][c]) |
        (one << cells[4][c]) |
        (one << cells[5][c]) |
        (one << cells[6][c]) |
        (one << cells[7][c]) |
        (one << cells[8][c])) == mask)

# Enumerate all squares
for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        # Add constraints for each 3*3 square
        s.add((
            (one << cells[r][c]) |
            (one << cells[r][c+1]) |
            (one << cells[r][c+2]) |
            (one << cells[r+1][c]) |
            (one << cells[r+1][c+1]) |
            (one << cells[r+1][c+2]) |
            (one << cells[r+2][c]) |
            (one << cells[r+2][c+1]) |
            (one << cells[r+2][c+2])) == mask)

print(s.check())
m = s.model()

for r in range(9):
    for c in range(9):
        sys.stdout.write(str(m[cells[r][c]]) + " ")
    print("")
