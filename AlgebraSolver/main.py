# Go through, then cleanup and add error codes! (After completed) #
def fix_equation(var):
    if len(find(r'\b(x)\b', var)) > 0:
        var = re.sub(r'\b(x)\b', '1x', var)
        if len(find(r'\b(y)\b', var)) > 0:
            var = re.sub(r'\b(y)\b', '1y', var)
    return var


def error(n):
    # Executes When error and points to error location
    print(f'\nError {n}')
    print('\nAn error has occured.')
    input('Resetting program on enter key press...')
    main()
    exit(1)


def find(charecter, string):
    return_string = ''
    for char in string:
        if char == charecter:
            return_string = return_string + char
    return return_string


def find_location(match, string):
    for char in string:
        return_value += 1
        if char == match:
            return return_value - 1
    return False


def find_charecters_between_charecters(charecters_one, charecters_two, string):
    start_index = find_location(string, charecters_one)
    if start_index == False:
        return False
    end_index = find_location(string, charecters_two)
    if end_index == False:
        return False
    return string[start_index:end_index]


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

###### INNER PARAN CHECK PROBLEM ######
def parantheses(var):
    if len(find_charecters_between_charecters('(', ')', var)) > 0:
        check = find_charecters_between_charecters('(', ')', var)
        original_check = check
        while True:
            ###### PARAN CHECK PROBLEM ######
            paran_check = find_location('(')
            if len(find('**', var)) > 0:
                check = exponents(check)
            ###### PARAN CHECK PROBLEM ######
            elif len(find_charecters_between_charecters('(', ')', paran_check)) > 0:
                check = parantheses(paran_check)
            elif len(find('*', check)) > 0:
                check = multiplication(check)
            elif len(find('/', check)) > 0:
                check = division(check)
            
            else:
                var = var.replace(original_check, check)
                return var
            
##### NEEDS FIXING (INNER PARAN CHECK PROBLEM) #####
def exponents(var):
    print('exponents loaded')
    if len(find('**', var)) > 0:
        print('working')
        if len(find(r'\((.+?)\)\s\*{2}\s\((.+?)\)', var)) > 0:
            check = find(r'(\((.+?)\)\s\*{2}\s\((.+?)\))', var)[0]
            check = parantheses(check)
            check = parantheses(check)
            var = var.replace(find(r'(\((.+?)\)\s\*{2}\s\((.+?)\))', var)[0], check)
            print('brackets left and right')
            return var
        elif len(find(r'\((.+?)\)\s\*{2}\s', var)) > 0:
            check = find(r'\((.+?)\)\s\*{2}\s', var)[0]
            check = parantheses(check)
            var = var.replace(find(r'\((.+?)\)\s\*{2}\s', var)[0], check)
            print('brackets left')
            return var
        elif len(find(r'\s\*{2}\s\((.+?)\)', var)) > 0:
            check = find(r'\s\*{2}\s\((.+?)\)', var)[0]
            check = parantheses(check)
            var = var.replace(find(r'\s\*{2}\s\((.+?)\)', var)[0], check)
            print('brackets right')
            return var


def number_mover(var, split_var):
    if len(find(r'-*(\d+)[^\w]', split_var[0])) > 0:
        moving_number = find(r'(-*\d+)[^\w]', split_var[0])[0]
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
    checklist = split_var[1].split(' ')
    for item in checklist:
        found_xy = find_location(item)
        found_numbers = find_location(item)

        if len(split_var[0]) == 0:
            if len(split_var[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                var = var.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
            else:
                var = var.replace(checklist[item] + ' ' + checklist[item+1], '')

            split_var = var.split('=')
            var = split_var[0] + str(-int(found_numbers)) + found_xy + split_var[1]
            return var
        
        elif len(split_var[0]) > 0:
            if len(split_var[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                var = var.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
            else: 
                var = var.replace(checklist[item] + ' ' + checklist[item+1], '')
                
            split_var = var.split('=')
            var = split_var[0] + ' + ' + str(-int(found_numbers)) + found_xy + split_var[1]
            return var


def eval_x_and_or_y(var, split_var):
    x_or_y = r"(\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b|\bx\b|\by\b)"
    long_x_or_y = r"(\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b)"
    xy_string = find(r"\b(-*\d*)\b" + x_or_y, split_var[0])
    original_xy_string = str(xy_string)
    xy_string = str(xy_string).replace('(', '').replace(')', '').replace("'", '').split(',')
    
    if 'x' and 'y' in xy_string:
        for list_object in x_or_y:
            for i in xy_string[list_object]:
                x_storage = find(r"(x)", xy_string[list_object])[i]
                x_storage = len(x_storage)
                y_storage = find(r"(y)", xy_string[list_object])[i]
                y_storage = len(y_storage)
            digit_storage = find(r"\b(-*\d*)\b" , xy_string[list_object])[0]
            digit_storage = int(digit_storage)
            xy_string[list_object] = f"{digit_storage + x_storage}x * {digit_storage + y_storage}y"
        temp_storage = find(r"\b(-*\d*)\b" + x_or_y, xy_string)
        for list_object in temp_storage:
            if 'x' in temp_storage[list_object]:
                digit_storage = find(r"\b(-*\d*)\b" , temp_storage[list_object])[0]
                digit_storage = int(digit_storage)
                x_storage = x_storage + digit_storage
            elif 'y' in temp_storage[list_object]:
                digit_storage = find(r"\b(-*\d*)\b" , temp_storage[list_object])[0]
                digit_storage = int(digit_storage)
                y_storage = y_storage + digit_storage
        if len(find(long_x_or_y, original_xy_string)) > 0:
            xy_string = f"{x_storage}x * {y_storage}y"
        else:
            xy_string = f"{x_storage}x + {y_storage}y"
        return xy_string

    elif 'x' in xy_string:
        for list_object in x_or_y:
            for i in xy_string[list_object]:
                x_storage = find(r"(x)", xy_string[list_object])[i]
                x_storage = len(x_storage)
            digit_storage = find(r"\b(-*\d*)\b" , xy_string[list_object])[0]
            digit_storage = int(digit_storage)
            xy_string[list_object] = f"{digit_storage + x_storage}x"
        return xy_string
    
    else:
        error(1)


def solve_xy(var, split_var, original_var):
    evaled_x_and_or_y = eval_x_and_or_y(var, split_var)
    print(f"evaled_x&%y = {eval_x_and_or_y}")
    if 'x' and 'y' in evaled_x_and_or_y:
        pass
    elif 'x' and not 'y' in evaled_x_and_or_y:
        split_var[1] = split_var[1] + ' / ' + find(r"\b(-*\d*)\b", eval_x_and_or_y)[0]
        
    else:
        if split_var[1] == 0:
            print(f'The solution of {original_var} is {split_var[1]} = 0\n')
            exit(0)
        elif split_var[1] != 0:
            print(f'There are no solutions of {original_var}\n')
            exit(0)
        else:
            error(1)
    #return var


def solve(var, split_var, original_var):
    print('\nsolve initiated!\n')
    print(var)
    # Solves the equation and returns the value of x and or y
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
    
    if len(find(r'\s*-*\b(\d+)\b\s*', split_var[0])) != 0:
        var = number_mover(var, split_var)
        return var

    elif len(find(r'(x|y)+', split_var[1])) != 0:
        print('started')
        var = xy_mover(var, split_var)
        return var

    else:
        solve_xy(var, split_var, original_var)


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
