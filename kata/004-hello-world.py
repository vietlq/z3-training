#!/usr/bin/env python3

from z3 import *

# H+E+L+L+O = W+O+R+L+D = 25

D, E, H, L, O, R, W = Ints('D E H L O R W')

s = Solver()

s.add(Distinct(D, E, H, L, O, R, W))
s.add(And(D >= 0, D <= 9))
s.add(And(E >= 0, E <= 9))
s.add(And(H >= 0, H <= 9))
s.add(And(L >= 0, L <= 9))
s.add(And(O >= 0, O <= 9))
s.add(And(R >= 0, R <= 9))
s.add(And(W >= 0, W <= 9))

s.add(H+E+L+L+O == W+O+R+L+D == 25)

print(s.check())
print(s.model())
