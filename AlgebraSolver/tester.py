import sympy


x = sympy.Symbol('x') #adds x as a python obj
y = sympy.Symbol('y') #adds y as a python obj

eq_test = sympy.solve(x * x * y, x)[0]
print(eq_test)

eq_test = sympy.solve(x ** x * y)
print(eq_test)