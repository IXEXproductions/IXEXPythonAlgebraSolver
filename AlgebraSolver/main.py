try:
    import sympy
except Exception as e:
    print('Error with import, please install imports.')
    print('Hint - \'pip install sympy\'')


def solve(var, original_var):

    x = sympy.Symbol('x')
    y = sympy.Symbol('y')

    if '=' in var:
        split_var = var.split('=')

        print('eq')
        print(var, '\n')

        if 'x' in var and not 'y' in var:
            if sympy.solve(split_var[0], x) == sympy.solve(split_var[1], x):
                result = f'The result of {original_var} is x = {sympy.solve(split_var[0], x)[0]}'

        elif 'y' in var and not 'x' in var:
            if sympy.solve(split_var[0], y) == sympy.solve(split_var[1], y):
                result = f'The result of {original_var} is y = {sympy.solve(split_var[0], y)[0]}'

        elif 'x' and 'y' in var:
            pass

    else:
        opj_var = sympy.simplify(original_var)
        print(str(opj_var)) ## do not make opj_var a str, its a python opj right now

        if 'x' in str(opj_var) and 'y' not in str(opj_var):
            # Solve for X
            result = sympy.solve(opj_var, x)
            print(result)

        if 'y' in str(opj_var) and 'x' not in str(opj_var):
            # Solve for Y
            result = sympy.solve(opj_var, y)
            print(result)
        
        if 'x' in str(opj_var) and 'y' in str(opj_var):
            # Solve for X and Y
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
