import time
import os
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
        multiplcation_equation_variable = str(re.findall(r'\b([^\s]+)\s\/\s([^\s]+)\b', var)).replace('[(', '').replace(')]', '').replace("'", '').split(', ')
        x_or_y_found = r"\b\d*([^\d]+)\b"
        if len(re.findall(x_or_y_found, multiplcation_equation_variable[0])) > 0:
            if len(re.findall(x_or_y_found, multiplcation_equation_variable[1])) > 0:
                variable_0_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[0])[0]
                variable_1_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[1])[0]
                variable_0_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[0])[0]
                variable_1_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[1])[0]
                multiplication_equation = re.findall(r'(\b[^\s]+\s\/\s[^\s]+\s)', var)[0]
                if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                    var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
                elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                    var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
            else:
                variable_0_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[0])[0]
                variable_1_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[1])[0]
                variable_0_number_value = re.findall(r'\b(\d*)', multiplcation_equation_variable[0])[0]
                multiplication_equation = re.findall(r'(\b[^\s]+\s\/\s[^\s]+\s)', var)[0]
                if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                    var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
                elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                    var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                    return var
        elif len(re.findall(x_or_y_found, multiplcation_equation_variable[1])) > 0:
            variable_1_variable_string = re.findall(x_or_y_found, multiplcation_equation_variable[1])[0]
            variable_0_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[0])[0]
            variable_1_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[1])[0]
            multiplication_equation = re.findall(r"(\b[^\s]+\s\/\s[^\s]+\s)", var)[0]
            if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var
            elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var
        else:
            variable_0_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[0])[0]
            variable_1_number_value = re.findall(r"\b(\d*)", multiplcation_equation_variable[1])[0]
            multiplication_equation = re.findall(r"(\b[^\s]+\s\/\s[^\s]+\s)", var)[0]
            if len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) == 0:
                var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
                return var
            elif len(re.findall(r'(\s[^\s]+\s*\s[^\s]+\s)', var)) > 0:
                var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
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
    # Checks if there are numebers not attatched to a x or y variable on the left side of the "="
    if len(re.findall(r"\b\d+\b", split_var[0])) > 0:
        inval = int(re.findall(r'\b(\d+)\b', split_var[0])[0])
        snval = str(re.findall(r'\b(\d+)\b', split_var[0])[0])
        if len(split_var[1]) == 0:
            if inval == 0:
                # Removes the current value on the left
                var = var[:var.find(snval)] + var[var.find(snval) + len(snval):]
                print(var)
                # Adds the the value to the other side
                var = var[var.find('='):] + ' ' + snval + ' ' + var[:var.find('=')]
                return var
            elif inval != 0:
                # Removes the current value on the left
                var = var[:var.find(snval)] + var[var.find(snval) + len(snval):]
                # Adds the opposite of the value to the other side
                var = var[var.find('='):] + ' -' + snval + ' ' + var[:var.find('=')]
                return var
            else:
                error()
        elif len(split_var[1]) > 0:
            if inval == 0:
                # Removes the current value on the left
                var = var[:var.find(snval)] + var[var.find(snval) + len(snval):]
                # Adds the the value to the other side
                var = var[var.find('='):] + ' ' + snval + ' ' + var[:var.find('=')]
                return var
            elif inval != 0:
                # Removes the current value on the left
                var = var[:var.find(snval)] + var[var.find(snval) + len(snval):]
                # Adds the opposite of the value to the other side
                var = var[var.find('='):] + ' - ' + snval + ' ' + var[:var.find('=')]
                return var
            else:
                error()
        else:
            error()

    # Checks if there are negative numebers not attatched to a x or y variable on the left side of the "="
    elif len(re.findall(r"\b-\d+\b", split_var[0])) > 0:
        if len(split_var[1]) == 0:
            if inval == 0:
                error(-0)
            elif inval != 0:
                # Removes the current value on the left
                var = var[:var.find(snval)] + var[var.find(snval) + len(snval):]
                # Adds the opposite of the value to the other side
                var = var[var.find('='):] + ' -' + snval + ' ' + var[:var.find('=')]
                return var
            else:
                error()
        elif len(split_var[1]) > 0:
            if inval == 0:
                error(-0)
            elif inval != 0:
                # Removes the current value on the left
                var = var[:var.find(snval)] + var[var.find(snval) + len(snval):]
                # Adds the opposite of the value to the other side
                var = var[var.find('='):] + '+ -' + snval + ' ' + var[:var.find('=')]
                return var
            else:
                error()
        else:
            error()
    
    else:
        #return var
        pass


def x_mover(var, split_var):
    x_or_y = r"(\bx\b|\by\b|\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b)"
    neg_x_or_y = r"(\b-x\b|\b-y\b|\b-x(?:[^\s]+)y\b|\b-y(?:[^\s]+)x\b|\b-x(?:[^\s]+)x\b|\b-y(?:[^\s]+)y\b|\b-xy\b|\b-yx\b)"
    if len(re.findall(x_or_y, var)) > 0:
        if len(re.findall(x_or_y, split_var[1])) > 0:
            print('looking for x')
            # Checks if "x" is a negative value on the right side of the "="
            if len(re.findall(neg_x_or_y, re.sub(r"[0-9]", '', split_var[1])))[0]:
                if len(split_var[0]) == 0:
                    # Strings of x value
                    xyvar = re.findall(r"(-\b\d*\b)", split_var[1])[0]
                    xyval = re.findall(r"-\b(\d*)\bx", split_var[1])[0]
                    # Removes the current "x" value on the right
                    var = var[:var.find(xyvar)] + ' ' +  var[var.find(xyvar) + len(xyvar):]
                    # Adds the opposite of the "x" value to the other side
                    var = var[:var.find('=')] + ' ' + xval + 'x ' + var[var.find('='):]
                    return var
                
                elif len(split_var[0]) > 0:
                    # Strings of x value
                    x = re.findall(r"(-\b\d*\bx)", split_var[1])[0]
                    xval = re.findall(r"-\b(\d*)\bx", split_var[1])[0]
                    # Removes the current "x" value on the right
                    var = var[:var.find(x)] + ' ' +  var[var.find(x) + len(x):]
                    # Adds the opposite of the "x" value to the other side
                    var = var[:var.find('=')] + ' + -' + xval + 'x ' + var[var.find('='):]
                    return var
        
            elif 'x' in split_var[1]:
                if len(split_var[0]) == 0:
                    # Strings of x value
                    x = re.findall(r"(\b\d*\bx)", split_var[1])[0]
                    xval = re.findall(r"\b(\d*)\bx", split_var[1])[0]
                    # Removes the current "x" value on the right
                    var = var[:var.find(x)] + ' ' +  var[var.find(x) + len(x):]
                    # Adds the opposite of the "x" value to the other side
                    var = var[:var.find('=')] + ' ' + xval + 'x ' + var[var.find('='):]
                    return var
                
                elif len(split_var[0]) > 0:
                    # Strings of x value
                    x = re.findall(r"(\b\d*\bx)", split_var[1])[0]
                    xval = re.findall(r"\b(\d*)\bx", split_var[1])[0]
                    # Removes the current "x" value on the right
                    var = var[:var.find(x)] + ' ' +  var[var.find(x) + len(x):]
                    # Adds the opposite of the "x" value to the other side
                    var = var[:var.find('=')] + ' + -' + xval + 'x ' + var[var.find('='):]
                    return var
                
                else:
                    return var  
                
            else: 
                return var


def svx(var, split_var):
    xs = re.findall(r"\b([^\s]*-*\d*)x\b", split_var[0])
    str(xs).replace('(', '').replace(')', '').replace("'", '').replace(',', '')
    print(xs)


def svxy(var, split_var):
    pass


def solve(var, split_var, original_var):
                print('\nsolve initiated!\n')
                # Solves the equation and returns the value of x and or y
                p = len(re.findall(r'\((.+?)\)', var)) 
                e = len(re.findall(r'\s(\*{2})\s', var))
                m = len(re.findall(r'\s\*\s', var))
                d = len(re.findall(r'\s\/\s', var))
                while p and e and m and d > 0:
                    if p > 0:
                        var = parantheses(var)
                        return var
                    elif e > 0:
                        var = exponents(var)
                        return var
                    elif m > 0:
                        var = multiplication(var)
                        return var
                    elif d > 0:
                        var = division(var)
                        return var
                
                if len(re.findall(r'\s*-*\b(\d+)\b\s*', split_var[1])) > 0:
                    var = number_mover(var, split_var)
                    return var


                elif len(re.findall(r'\s*-*\b(\d+)\b\s', split_var[0])) != len(split_var[0]):
                    var = x_mover(var, split_var)
                    #x_y_mover(var, split_var)
                    ssv = str(eval(split_var[0]))
                    var = var[:var.find(split_var[0])] + ssv +  var[var.find(split_var[0]) + len(split_var[0]):]
                    return var
                

                elif len(re.findall('x', split_var[1])) and len(re.findall('y', split_var[1])) == 0:
                    print(len(re.findall('y', split_var[1])))
                    print(len(re.findall('x', split_var[1])))
                    if 'x' and 'y' in var:
                        svxy(var, split_var)
                        return var
                    elif 'x' in var:
                        svx(var, split_var)
                        return var
                    else:
                        pass


                else:
                    os.system('clear')
                    print(f'The solution of {original_var}\n{split_var[1]} = {split_var[0]}\n')
                    running = False
                    exit(0)


def main():
    print('Please enter an equation')
    eq = input('>').lower()
    original_eq = str(eq)
    time.sleep(1)
    numbers = r"[0-9]"
    running = True
    while running:
        time.sleep(1)
        if '=' in eq:
            split_eq = eq.split('=')
            eq = fix_equation(eq)
            print('eq')
            print(eq, '\n')
            time.sleep(1)
            eq = solve(eq, split_eq, original_eq)


        elif 'quit' == eq.lower():
            os.system('clear')
            exit(0)

        else:
            # Executes When There Is An Error With Formatting
            print_statment = '''\nPlease follow the correct formatting structure. 
            If your equation has only one variable, make sure the variable is set to "x". 
            If it is a two variable equation set one variable to "x" and one to "y".
            There cannot be a space inbetween the chevron and your equation.
            If you wish to exit the program type "quit".
            Resetting program...'''
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