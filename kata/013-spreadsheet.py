#!/usr/bin/env python3

from z3 import *
import sys
import re


def coord_to_name(row, col):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[row] + str(col)


fh = open(sys.argv[1], 'r')

in_array = filter(None, [item.rstrip().split() for item in fh.readlines()])

fh.close()

WIDTH = len(in_array[0])
HEIGHT = len(in_array)

cells = {}

for row in range(HEIGHT):
    for col in range(WIDTH):
        name = coord_to_name(row, col)
        cells[name] = Int(name)

s = Solver()

cur_row, cur_col = 0, 0

for row in in_array:
    for col in row:
        # Convert strings A0 + B2 to cells["A0"] + cells["B2"]
        col = re.sub(r'(A-Z{1}[0-9]+)', r'cells["\1"]', col)
        st = '''cells["%s"] == %s''' % (coord_to_name(cur_row, cur_col), col)
        # Evalue string. Z3Py expression is constructed at this step:
        e = eval(st)
        # Add constraint
        s.add(e)
        cur_col = cur_col + 1
    cur_row = cur_row + 1
    cur_col = 0

result = str(s.check())
print(result)
if result == "sat":
    m = s.model()
    for row in range(HEIGHT):
        for col in range(WIDTH):
            sys.stdout.write(str(m[cells[coord_to_name(r, c)]]) + "\t")
        sys.stdout.write("\n")
