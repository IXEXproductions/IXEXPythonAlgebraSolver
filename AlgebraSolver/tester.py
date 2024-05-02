try:
    import sympy
except Exception as e:
    print('Error with import, please install imports.')
    print('Hint - \'pip install sympy\'')


def solve(var, original_var):

    x = sympy.Symbol('x')
    y = sympy.Symbol('y')

    if '=' in var:
        temp = var.split('=')
        temp = [sympy.simplify(temp[0]), sympy.simplify(temp[1])]
        temp = sympy.solve(temp[0] == temp[1], x, y)
        print(temp)

    else:
        opj_var = sympy.simplify(original_var)
        print(str(opj_var)) ## do not make opj_var a str, its a python opj right now

        if 'x' in str(opj_var) and 'y' not in str(opj_var):
            # Solve for "x"
            result = sympy.solve(opj_var, x)
            print(result)

        if 'y' in str(opj_var) and 'x' not in str(opj_var):
            # Solve for "y"
            result = sympy.solve(opj_var, y)
            print(result)
        
        if 'x' in str(opj_var) and 'y' in str(opj_var):
            # Solve for "x" and "y"
            result = sympy.solve(opj_var, x, y)
            print(result)


def main():
    while True:
        
        print('Please enter an equation')
        eq = input('>').lower().strip()
        original_eq = str(eq)

        if 'quit' == eq.lower():
            break

        elif 'exit' == eq.lower():
            break

        elif 'close' == eq.lower():
            break

        else:
            solve(eq, original_eq)


if __name__ == '__main__':
    main()

# Testing Equations
# x ** 2 + 6 * x + 9 = 0
# 0 = x ** 2 + 6 * x + 9
# 60 * x = 0
# x = 0
# 0 = x
# x ** (2) = 9
# x * xy =  x ** x * y 
# xy / x = y
# x ** x = 0
