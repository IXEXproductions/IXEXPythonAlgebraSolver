import re

try:
    import sympy
except Exception as e:
    print('Error with import, please install imports.')
    print('Hint - \'pip install sympy\'')


def find_location(match, string):
    for char in string:
        return_value += 1
        if char == match:
            return return_value - 1
    return False


def find_all_numbers(string):
    return_string = ''
    for char in string:
        if char.isdigit():
            return_string = return_string + char
    return return_string


def find_all_xy(string):
    return_string = ''
    for char in string:
        if char == "x":
            return_string = return_string + char
        elif char == "y": 
            return_string = return_string + char
    return return_string


def find_charecters_between_charecters(charecters_one, charecters_two, string):
    start_index = find_location(string, charecters_one)
    if start_index == False:
        return False
    end_index = find_location(string, charecters_two)
    if end_index == False:
        return False
    return string[start_index:end_index]


def find(charecter, string):
    return_string = ''
    for char in string:
        if char == charecter:
            return_string = return_string + char
    return return_string


def multiplication(var):
    if len(find_location(' * ', var)) > 0:
        multiplcation_equation_variable = find_charecters_between_charecters(' ', ' *', var) + ',' + find_charecters_between_charecters('* ', ' ', var)
        multiplcation_equation_variable = multiplcation_equation_variable.split(',')

        variable_0_variable_string = find_all_xy(multiplcation_equation_variable[0])
        variable_1_variable_string = find_all_xy(multiplcation_equation_variable[1])
        variable_0_number_value = find('-', multiplcation_equation_variable[0]) + find_all_numbers(multiplcation_equation_variable[0])
        variable_1_number_value = find('-', multiplcation_equation_variable[0]) + find_all_numbers(multiplcation_equation_variable[1])

        multiplication_equation = variable_0_number_value + variable_0_variable_string + ' * ' + variable_1_number_value + variable_1_variable_string

        if len(multiplication_equation) == 0:
            var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
            return var
        elif len(multiplication_equation) > 0:
            var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) * int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
            return var


def division(var):
    if len(find_location(' / ', var)) > 0:
        multiplcation_equation_variable = find_charecters_between_charecters(' ', ' /', var) + ',' + find_charecters_between_charecters('/ ', ' ', var)
        multiplcation_equation_variable = multiplcation_equation_variable.split(',')

        variable_0_variable_string = find_all_xy(multiplcation_equation_variable[0])
        variable_1_variable_string = find_all_xy(multiplcation_equation_variable[1])
        variable_0_number_value = find('-', multiplcation_equation_variable[0]) + find_all_numbers(multiplcation_equation_variable[0])
        variable_1_number_value = find('-', multiplcation_equation_variable[0]) + find_all_numbers(multiplcation_equation_variable[1])

        multiplication_equation = variable_0_number_value + variable_0_variable_string + ' / ' + variable_1_number_value + variable_1_variable_string
        
        if len(multiplication_equation) == 0:
            var = var[:var.find(multiplication_equation)] + ' ' + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
            return var
        elif len(multiplication_equation) > 0:
            var = var[:var.find(multiplication_equation)] + str(int(variable_0_number_value) / int(variable_1_number_value)) + variable_0_variable_string + variable_1_variable_string + ' ' + var[var.find(multiplication_equation) + len(multiplication_equation):]
            return var
        

def parantheses(string):
    parantheses_check = []
    for charecter in string:
        if charecter == '(' or charecter == ')':
            parantheses_check.append[charecter]
    for item in parantheses_check:
        if '(' == parantheses_check[len(item) + 1]:
            parantheses_check = parantheses_check.pop(item)
        elif ')' == parantheses_check[len(item) + 1]:
            if len(find_location(')', parantheses_check.pop(item))) == 0:
                for i, charecter in string:
                    if charecter == ')':
                        if counter == close_parantheses_popcounter + 1:
                            check = string[find_location('(', string):i]
                            original_check = check
                            while True:
                                modified_string = string.pop(find_location('(', string)).pop(i)
                                if len(find('**', var)) > 0:
                                    check = exponents(string)
                                elif '(' in modified_string:
                                    check = parantheses(modified_string)
                                elif len(find('*', check)) > 0:
                                    check = multiplication(check)
                                elif len(find('/', check)) > 0:
                                    check = division(check)
                                else:
                                    var = var.replace(original_check, check)
                        else:
                            counter += 1
            else:
                parantheses_check = parantheses_check.pop(item)
                close_parantheses_popcounter += 1


def exponents(var):
    print('exponents loaded')
    if len(find('**', var)) > 0:
        print('working')
        if re.findall(r'(\((.+?)\)\s\*{2}\s\((.+?)\))', var)[0] in var:
            check = re.findall(r'(\((.+?)\)\s\*{2}\s\((.+?)\))', var)[0]
            original_check = check
            check = parantheses(check)
            check = parantheses(check)
            var = var.replace(original_check, check)
            print('brackets left and right')
            return var
        elif re.findall(r'\((.+?)\)\s\*{2}\s', var)[0] in var:
            check = re.findall(r'\((.+?)\)\s\*{2}\s', var)[0]
            original_check = check
            check = parantheses(check)
            var = var.replace(original_check, check)
            print('brackets left')
            return var
        elif re.findall(r'\s\*{2}\s\((.+?)\)', var) in var:
            check = re.findall(r'\s\*{2}\s\((.+?)\)', var)[0]
            original_check = check
            check = parantheses(check)
            var = var.replace(original_check, check)
            print('brackets right')
            return var
        elif len(re.findall(r'(\d+(?:x|y)*) \*{2} (\d+(?:x|y)*)', var)) > 0:
            exponents_digit_value = re.findall(r'(-*\d+)(?:x|y)* \*{2} (-*\d+)(?:x|y)*', var)
            exponents_variable = re.findall(r'-*\d+((?:x|y)*) \*{2} -*\d+((?:x|y)*)', var)
            return exponents_digit_value[0] ** exponents_digit_value[1] + exponents_variable[0] ** exponents_variable[1]
            
                


def number_mover(var, split_var, symbols):
    for charecter in split_var[0]:
        if split_var[0][find_location(charecter) + 1].isdigit():
            if ' ' + charecter + split_var[0][find_location(charecter) + 1]:
                moving_number.append(charecter)
        elif charecter.isdigit() and not symbols in split_var[0][find_location(charecter) + 1]:
            if ' ' + charecter in split_var[0]:
                moving_number.append(charecter) 
            elif ' -' + charecter in split_var[0]:
                moving_number = moving_number.pop().append(moving_number[-1] + charecter)
    if len(moving_number) > 0:
        for item in  moving_number:
            if '0' in moving_number[0]:
                # Removes the current value on the left
                var = var[:var.find(moving_number[item])] + var[var.find(moving_number[item]) + len(moving_number[item]):]
                # Adds the the value to the other side
                var = var[var.find('='):] + ' + ' + moving_number[item] + '' + var[:var.find('=')]
                return var
            else:
                # Removes the current value on the left
                var = var[:var.find(moving_number[item])] + var[var.find(moving_number[item]) + len(moving_number[item]):]
                # Adds the the value to the other side
                var = var[var.find('='):] + ' + ' + -int(moving_number[item]) + '' + var[:var.find('=')]
                return var
            

def isolate_y(var):
    print('looking for y')
    checklist = split_var[1].split(' ')
    try:
        split_var = var.split('=')
        if 'x' in split_var[0]:
            isolate_x(var)
    finally:
        for item in checklist:
            found_y = find_location('y', item)
            found_numbers = found_numbers(item)
            if len(split_var[0]) == 0:
                if len(split_var[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                    var = var.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
                else:
                    var = var.replace(checklist[item] + ' ' + checklist[item+1], '')
                split_var = var.split('=')
                var = split_var[0] + str(-int(found_numbers)) + found_y + split_var[1]
                return var
            elif len(split_var[0]) > 0:
                if len(split_var[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                    var = var.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
                else: 
                    var = var.replace(checklist[item] + ' ' + checklist[item+1], '')
                split_var = var.split('=')
                var = split_var[0] + ' + ' + str(-int(found_numbers)) + found_y + split_var[1]
                return var


def isolate_x(var):
    checklist = split_var[1].split(' ')
    for item in checklist:
        found_x = find_location('x', item)
        found_numbers = found_numbers(item)
        if len(split_var[0]) == 0:
            if len(split_var[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                var = var.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
            else:
                var = var.replace(checklist[item] + ' ' + checklist[item+1], '')
            split_var = var.split('=')
            var = split_var[0] + str(-int(found_numbers)) + found_x + split_var[1]
            return var
        elif len(split_var[0]) > 0:
            if len(split_var[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                var = var.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
            else: 
                var = var.replace(checklist[item] + ' ' + checklist[item+1], '')
            split_var = var.split('=')
            var = split_var[0] + ' + ' + str(-int(found_numbers)) + found_x + split_var[1]
            return var


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
            parantheses_check = len(find(r'\((.+?)\)', var)) 
            exponents_check = len(find(r'\s(\*{2})\s', var))
            multiplication_check = len(find(r'\s\*\s', var))
            division_check = len(find(r'\s\/\s', var))
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
                
        elif len(find(r'\s*-*\b(\d+)\b\s*', split_var[0])) != 0:
            var = number_mover(var, split_var, x or y)
            return var
        
        else:
            if 'y' in var:
                if 'y' in split_var[1]:
                    print('started')
                    var = isolate_y(var, split_var)
                    return var
            elif 'x' in var:
                pass
            else:
                print('No Solution')
                exit(0)

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
