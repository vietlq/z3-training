#!/usr/bin/env python3

from z3 import *

# Find all combinations of 1p, 2p, 5p, 10p, 20p, 50p, 1GBP, 2GBP that add up to 2GBP
a, b, c, d, e, f, g, h = Ints('a b c d e f g h')

s = Solver()
s.add(1*a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h == 200,
        a >= 0, b >= 0, c >= 0, d >= 0, e >= 0, f >= 0, g >= 0, h >= 0)
results = []

while True:
    if s.check() == sat:
        m = s.model()
        print(m)
        results.append(m)
        # Create a new constraint the blocks the current model
        block = []
        for d in m:
            # d is a declaration
            if d.arity() > 0:
                raise Z3Exception("Uninterpreted functions are not supported")
            # Create a constant from the declaration
            c = d()
            if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
                raise Z3Exception("Arrays and uninterpreted sorts are not supported")
            block.append(c != m[d])
        s.add(Or(block))
    else:
        print(len(results))
        break
