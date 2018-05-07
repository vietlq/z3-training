#!/usr/bin/env python3

from z3 import *

x = BitVec('x', 32)
y = BitVec('y', 32)
output = BitVec('output', 32)
s = Solver()
s.add(x ^ y == output)
s.add(((y & x) * 0xFFFFFFFE) + (y + x) != output)

print("For x and are 32-bit integers:")
if s.check() == unsat:
    print("The formula is valid: x XOR y == (y & x)*0xFFFFFFFE + (y + x)")
else:
    print("The formula is invalid: x XOR y == (y & x)*0xFFFFFFFE + (y + x)")
