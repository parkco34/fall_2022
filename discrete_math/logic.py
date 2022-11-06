#!/usr/bin/env python

def negation(p):
    return not p

print("p    a")
for p in [True, False]:
    a = negation(p)
    print(p,a)

