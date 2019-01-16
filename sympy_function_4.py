from sympy import *
import numpy as np
import sys

a, b, c, d, e = map(float, input('Please input a, b, c, d, e\n').split())

var("a:z")  

func = a*x**4 + b*x**3 + c*x**2 + d*x + e
print(func)

result = solve(func, x)
print(result)

#init_printing()
#display(result)