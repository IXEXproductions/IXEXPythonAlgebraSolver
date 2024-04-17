import re

# Go through, then cleanup and add error codes! (After completed) #
def fix_equation(var):
    if len(re.findall(r'\b(x)\b', var)) > 0:
        var = re.sub(r'\b(x)\b', '1x', var)
        if len(re.findall(r'\b(y)\b', var)) > 0:
            var = re.sub(r'\b(y)\b', '1y', var)
    return var


def error(n):
    # Executes When error and points to error location
    print(f'\nError {n}')
    print('\nAn error has occured.')
    input('Resetting program on enter key press...')
    main()
    exit(1)


def multiplication(var):
    if len(re.findall(r'\s\*\s', var)) > 0:
        multiplcation_equation_variable = str(re.findall(r'\b([^\s]+)\s\*\s([^\s]+)\b', var)).replace('[(', '').replace(')]', '').replace("'", '').split(', ')
        x_or_y_found = r"\b\d*([^\d]+)\b"
        if len(re.findall(x_or_y_found, multiplcation_equation_variable[0])) > 0:
            if len(re.findall(x_or_y_found, multiplcation_equation_variable[1])) > 0:
                variable_0_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[0])[0]
                variable_1_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[1])[0]
                variable_0_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[0])[0]
                variable_1_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[1])[0]
                multiplication_equation = re.findall(r'(\b[^\s]+\s\*\s[^\s]+\s)', var)[0]
                if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                    var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
                elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                    var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
            else:
                variable_0_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[0])[0]
                variable_0_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[0])[0]
                variable_1_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[1])[0]
                multiplication_equation = re.findall(r'(\b[^\s]+\s\*\s[^\s]+\s)', var)[0]
                if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                    var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_0_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
                elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                    var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_0_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
        elif len(re.findall(x_or_y_found, multiplcation_equation_variable[1])) > 0:
            variable_1_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[1])[0]
            variable_0_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[0])[0]
            variable_1_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[1])[0]
            multiplication_equation = re.findall(r"(\b[^\s]+\s\*\s[^\s]+\s)", var)[0]
            if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var
            elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var
        else:
            variable_0_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[0])[0]
            variable_1_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[1])[0]
            multiplication_equation = re.findall(r"(\b[^\s]+\s\*\s[^\s]+\s)", var)[0]
            if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) * int(variable_1_number_value)) + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var
            elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) * int(variable_1_number_value)) + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var


def division(var):
    if len(re.findall(r'\s\/\s', var)) > 0:
        division_equation_variable = str(re.findall(r'\b([^\s]+)\s\/\s([^\s]+)\b', var)).replace('[(', '').replace(')]', '').replace("'", '').split(', ')
        x_or_y_found = r"\b\d*([^\d]+)\b"
        if len(re.findall(x_or_y_found, division_equation_variable[0])) > 0:
            if len(re.findall(x_or_y_found, division_equation_variable[1])) > 0:
                variable_0_variable_string = re.findall(x_or_y_found, division_equation_variable[0])[0]
                variable_1_variable_string = re.findall(x_or_y_found, division_equation_variable[1])[0]
                variable_0_number_value = re.findall(r'\b(\d*)', division_equation_variable[0])[0]
                variable_1_number_value = re.findall(r'\b(\d*)', division_equation_variable[1])[0]
                division_equation = re.findall(r'(\b[^\s]+\s\/\s[^\s]+\s)', var)[0]
                if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                    var = var[:var.find(division_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(division_equation) + len(division_equation):]
                    return var
                elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                    var = var[:var.find(division_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(division_equation) + len(division_equation):]
                    return var
            else:
                variable_0_variable_string = re.findall(x_or_y_found, division_equation_variable[0])[0]
                variable_1_number_value = re.findall(r'\b(\d*)', division_equation_variable[1])[0]
                variable_0_number_value = re.findall(r'\b(\d*)', division_equation_variable[0])[0]
                division_equation = re.findall(r'(\b[^\s]+\s\/\s[^\s]+\s)', var)[0]
                if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                    var = var[:var.find(division_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + ' ' + var[var.find(division_equation) + len(division_equation):]
                    return var
                elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                    var = var[:var.find(division_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + ' ' + var[var.find(division_equation) + len(division_equation):]
                    return var
        elif len(re.findall(x_or_y_found, division_equation_variable[1])) > 0:
            variable_1_variable_string = re.findall(x_or_y_found, division_equation_variable[1])[0]
            variable_0_number_value = re.findall(r"\b(\d*)", division_equation_variable[0])[0]
            variable_1_number_value = re.findall(r"\b(\d*)", division_equation_variable[1])[0]
            division_equation = re.findall(r"(\b[^\s]+\s\/\s[^\s]+\s)", var)[0]
            if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                var = var[:var.find(division_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_1_variable_string + ' ' + var[var.find(division_equation) + len(division_equation):]
                return var
            elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                var = var[:var.find(division_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_1_variable_string + ' ' + var[var.find(division_equation) + len(division_equation):]
                return var
        else:
            variable_0_number_value = re.findall(r"\b(\d*)", division_equation_variable[0])[0]
            variable_1_number_value = re.findall(r"\b(\d*)", division_equation_variable[1])[0]
            division_equation = re.findall(r"(\b[^\s]+\s\/\s[^\s]+\s)", var)[0]
            if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                var = var[:var.find(division_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + ' ' + var[var.find(division_equation) + len(division_equation):]
                return var
            elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                var = var[:var.find(division_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + ' ' + var[var.find(division_equation) + len(division_equation):]
                return var
            

def parantheses(var):
    if len(re.findall(r'\((.+?)\)', var)) > 0:
        check = re.findall(r'\((.+?)\)', var)[0]
        while True:
            if len(re.findall(r'\s(\*{2})\s', var)) > 0:
                check = exponents(check)
            elif len(re.findall(r'\((.+?)\)', var)) > 0:
                check = parantheses(check)
            elif len(re.findall(r'\s\*\s', check)) > 0:
                check = multiplication(check)
            elif len(re.findall(r'\s\/\s', check)) > 0:
                check = division(check)
            elif len(re.findall(r'\s(\*{2})\s', var)) > 0:
                check = exponents(check)
            
            else:
                var = var.replace(re.findall(r'\((.+?)\)', var)[0], check)
                return var
            

def exponents(var):
    print('loaded')
    if len(re.findall(r'\s(\*{2})\s', var)) > 0:
        print('working')
        if len(re.findall(r'\((.+?)\)\s\*{2}\s\((.+?)\)', var)) > 0:
            check = re.findall(r'(\((.+?)\)\s\*{2}\s\((.+?)\))', var)[0]
            check = parantheses(check)
            check = parantheses(check)
            var = var.replace(re.findall(r'(\((.+?)\)\s\*{2}\s\((.+?)\))', var)[0], check)
            print('brackets left and right')
            return var
        elif len(re.findall(r'\((.+?)\)\s\*{2}\s', var)) > 0:
            check = re.findall(r'\((.+?)\)\s\*{2}\s', var)[0]
            check = parantheses(check)
            var = var.replace(re.findall(r'\((.+?)\)\s\*{2}\s', var)[0], check)
            print('brackets left')
            return var
        elif len(re.findall(r'\s\*{2}\s\((.+?)\)', var)) > 0:
            check = re.findall(r'\s\*{2}\s\((.+?)\)', var)[0]
            check = parantheses(check)
            var = var.replace(re.findall(r'\s\*{2}\s\((.+?)\)', var)[0], check)
            print('brackets right')
            return var


def number_mover(var, split_var):
    if len(re.findall(r'-*(\d+)[^\w]', split_var[0])) > 0:
        moving_number = re.findall(r'(-*\d+)[^\w]', split_var[0])[0]
        if '0' in moving_number:
            # Removes the current value on the left
            var = var[:var.find(moving_number)] + var[var.find(moving_number) + len(moving_number):]
            # Adds the the value to the other side
            var = var[var.find('='):] + ' + ' + moving_number + '' + var[:var.find('=')]
            return var
        else:
            # Removes the current value on the left
            var = var[:var.find(moving_number)] + var[var.find(moving_number) + len(moving_number):]
            # Adds the the value to the other side
            var = var[var.find('='):] + ' + ' + -int(moving_number) + '' + var[:var.find('=')]
            return var

    else:
        return var


def xy_mover(var, split_var):
    print('looking for x/y')
    x_or_y = r"(?:\bx\b|\by\b|\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b)"
    x_or_y_found = r"(\bx\b|\by\b|\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b)"
    xy_value = re.findall(r"-(\d)" + x_or_y, split_var[1])[0]
    xy_variable = re.findall(r"-\d" + x_or_y_found, split_var[1])[0]
    xy_string = re.findall(r"(-\d)" + x_or_y_found, split_var[1])[0]

    if len(split_var[0]) == 0:
        var = re.sub(xy_string + r" =\s+(.*)", ' ')
        var = re.sub(r"=", -int(xy_value) + xy_variable + " =")
        return var
    
    elif len(split_var[0]) > 0:
        var = re.sub(xy_string + r" =\s+(.*)", ' ')
        var = re.sub(r"=",' + ' + -int(xy_value) + xy_variable + " =")
        return var

    
    else:
        return var


def eval_x_and_or_y(var, split_var):
    x_or_y = r"(\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b|\bx\b|\by\b)"
    long_x_or_y = r"(\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b)"
    xy_string = re.findall(r"\b(-*\d*)\b" + x_or_y, split_var[0])
    original_xy_string = str(xy_string)
    xy_string = str(xy_string).replace('(', '').replace(')', '').replace("'", '').split(',')
    
    if 'x' and 'y' in xy_string:
        for list_object in x_or_y:
            for i in xy_string[list_object]:
                x_storage = re.findall(r"(x)", xy_string[list_object])[i]
                x_storage = len(x_storage)
                y_storage = re.findall(r"(y)", xy_string[list_object])[i]
                y_storage = len(y_storage)
            digit_storage = re.findall(r"\b(-*\d*)\b" , xy_string[list_object])[0]
            digit_storage = int(digit_storage)
            xy_string[list_object] = f"{digit_storage + x_storage}x * {digit_storage + y_storage}y"
        temp_storage = re.findall(r"\b(-*\d*)\b" + x_or_y, xy_string)
        for list_object in temp_storage:
            if 'x' in temp_storage[list_object]:
                digit_storage = re.findall(r"\b(-*\d*)\b" , temp_storage[list_object])[0]
                digit_storage = int(digit_storage)
                x_storage = x_storage + digit_storage
            elif 'y' in temp_storage[list_object]:
                digit_storage = re.findall(r"\b(-*\d*)\b" , temp_storage[list_object])[0]
                digit_storage = int(digit_storage)
                y_storage = y_storage + digit_storage
        if len(re.findall(long_x_or_y, original_xy_string)) > 0:
            xy_string = f"{x_storage}x * {y_storage}y"
        else:
            xy_string = f"{x_storage}x + {y_storage}y"
        split_var[0] = xy_string
        var = split_var[0] + split_var[1]
        return var

    elif 'x' in xy_string:
        for list_object in x_or_y:
            for i in xy_string[list_object]:
                x_storage = re.findall(r"(x)", xy_string[list_object])[i]
                x_storage = len(x_storage)
            digit_storage = re.findall(r"\b(-*\d*)\b" , xy_string[list_object])[0]
            digit_storage = int(digit_storage)
            xy_string[list_object] = f"{digit_storage + x_storage}x"
        split_var[0] = xy_string
        var = split_var[0] + split_var[1]
        return var
    
    else:
        error(1)

def solve_xy(var, split_var):
    var = eval_x_and_or_y(var, split_var)
    print(f"var = {var}")
    #return var


def solve(var, split_var, original_var):
    print('\nsolve initiated!\n')
    print(var)
    # Solves the equation and returns the value of x and or y
    parantheses_check = len(re.findall(r'\((.+?)\)', var)) 
    exponents_check = len(re.findall(r'\s(\*{2})\s', var))
    multiplication_check = len(re.findall(r'\s\*\s', var))
    division_check = len(re.findall(r'\s\/\s', var))
    while parantheses_check and exponents_check and multiplication_check and division_check > 0:
        if parantheses_check > 0:
            var = parantheses(var)
            return var
        elif exponents_check > 0:
            var = exponents(var)
            return var
        elif multiplication_check > 0:
            var = multiplication(var)
            return var
        elif division_check > 0:
            var = division(var)
            return var
    
    if len(re.findall(r'\s*-*\b(\d+)\b\s*', split_var[0])) != 0:
        var = number_mover(var, split_var)
        return var

    elif len(re.findall(r'(x)', split_var[1])) > 0 or len(re.findall(r'(y)', split_var[1])) > 0:
        print('started')
        var = xy_mover(var, split_var)
        return var

    else:
        var = solve_xy(var, split_var)
        print(f'The solution of {original_var} is {split_var[1]} = {split_var[0]}\n')
        exit(0)


def main():
    print('Please enter an equation')
    eq = input('>').lower()
    original_eq = str(eq)
    running = True
    while running:
        if '=' in eq:
            split_eq = eq.split('=')
            eq = fix_equation(eq)
            print('eq')
            print(eq, '\n')
            eq = solve(eq, split_eq, original_eq)


        elif 'quit' == eq.lower():
            
            exit(0)

        else:
            # Executes When There Is An Error With Formatting
            print_statment = '''\nPlease follow the correct formatting structure. 
            \nIf your equation has only one variable, make sure the variable is set to "x". 
            \nIf it is a two variable equation set one variable to "x" and one to "y".
            \nThere cannot be a space inbetween the chevron and your equation.
            \nPress Enter to reset program'''
            input(print_statment)
            main()
            exit(1)


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
