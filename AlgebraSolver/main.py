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


def get_all_xy_var(string):
    for char in string:
        if char == "x":
            while True:
                counter += 1
                if counter == 1:
                    temp_string + char
                elif counter == 1 and string[char + 1] == 'y':
                    temp_string = temp_string + string[char + 1]
                elif string[char - counter] in '-1234567890':
                    temp_string = string[char - counter] + temp_string
                else:
                    break
            xylist = xylist.append(temp_string)
        elif char == "y": 
            while True:
                counter += 1
                if counter == 1:
                    temp_string + char
                elif counter == 1 and string[char + 1] == 'x':
                    temp_string = temp_string + string[char + 1]
                elif string[char - counter] in '-1234567890':
                    temp_string = string[char - counter] + temp_string
                else:
                    break
        xylist = xylist.append(temp_string)
    return xylist


def get_all_numbers(string):
    for char in string:
        while True:
            counter += 1
            if counter == 1:
                string.pop(string[char + counter])
                string.pop(char)
                temp_string = temp_string + char
            elif string[char + counter] in '-1234567890':
                string.pop(string[char + counter])
                temp_string = temp_string + string[char + counter]
            elif string[char - counter] in '-1234567890':
                string.pop(string[char - counter])
                temp_string = string[char - counter] + temp_string
            else:
                break
        digits = digits.append(temp_string)


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


def multiplication(string):
    if len(find_location(' * ', string)) > 0:
        multiplcation_equation_stringiable = find_charecters_between_charecters(' ', ' *', string) + ',' + find_charecters_between_charecters('* ', ' ', string)
        multiplcation_equation_stringiable = multiplcation_equation_stringiable.split(',')

        stringiable_0_stringiable_string = find_all_xy(multiplcation_equation_stringiable[0])
        stringiable_1_stringiable_string = find_all_xy(multiplcation_equation_stringiable[1])
        stringiable_0_number_value = find('-', multiplcation_equation_stringiable[0]) + find_all_numbers(multiplcation_equation_stringiable[0])
        stringiable_1_number_value = find('-', multiplcation_equation_stringiable[0]) + find_all_numbers(multiplcation_equation_stringiable[1])

        multiplication_equation = stringiable_0_number_value + stringiable_0_stringiable_string + ' * ' + stringiable_1_number_value + stringiable_1_stringiable_string

        if len(multiplication_equation) == 0:
            string = string[:string.find(multiplication_equation)] + ' ' + str(int(stringiable_0_number_value) * int(stringiable_1_number_value)) + stringiable_0_stringiable_string + stringiable_1_stringiable_string + ' ' + string[string.find(multiplication_equation) + len(multiplication_equation):]
            return string
        elif len(multiplication_equation) > 0:
            string = string[:string.find(multiplication_equation)] + str(int(stringiable_0_number_value) * int(stringiable_1_number_value)) + stringiable_0_stringiable_string + stringiable_1_stringiable_string + ' ' + string[string.find(multiplication_equation) + len(multiplication_equation):]
            return string


def division(string):
    if len(find_location(' / ', string)) > 0:
        multiplcation_equation_stringiable = find_charecters_between_charecters(' ', ' /', string) + ',' + find_charecters_between_charecters('/ ', ' ', string)
        multiplcation_equation_stringiable = multiplcation_equation_stringiable.split(',')

        stringiable_0_stringiable_string = find_all_xy(multiplcation_equation_stringiable[0])
        stringiable_1_stringiable_string = find_all_xy(multiplcation_equation_stringiable[1])
        stringiable_0_number_value = find('-', multiplcation_equation_stringiable[0]) + find_all_numbers(multiplcation_equation_stringiable[0])
        stringiable_1_number_value = find('-', multiplcation_equation_stringiable[0]) + find_all_numbers(multiplcation_equation_stringiable[1])

        multiplication_equation = stringiable_0_number_value + stringiable_0_stringiable_string + ' / ' + stringiable_1_number_value + stringiable_1_stringiable_string
        
        if len(multiplication_equation) == 0:
            string = string[:string.find(multiplication_equation)] + ' ' + str(int(stringiable_0_number_value) / int(stringiable_1_number_value)) + stringiable_0_stringiable_string + stringiable_1_stringiable_string + ' ' + string[string.find(multiplication_equation) + len(multiplication_equation):]
            return string
        elif len(multiplication_equation) > 0:
            string = string[:string.find(multiplication_equation)] + str(int(stringiable_0_number_value) / int(stringiable_1_number_value)) + stringiable_0_stringiable_string + stringiable_1_stringiable_string + ' ' + string[string.find(multiplication_equation) + len(multiplication_equation):]
            return string


def getparan(string):
    parantheses_check = []
    for charecter in string:
        if charecter == '(' or charecter == ')':
            parantheses_check.append[charecter]
    for item in parantheses_check:
        if '(' == parantheses_check[len(item) + 1]:
            parantheses_check = parantheses_check.pop(item)
        elif ')' == parantheses_check[len(item) + 1]:
            if len(find(')', parantheses_check.pop(item))) == 0:
                  for i, charecter in string:
                    if charecter == ')':
                        if counter == close_parantheses_popcounter + 1:
                            result = string[find_location('(', string):i]
                            return result
                        else:
                            counter += 1

            else:
                parantheses_check = parantheses_check.pop(item)
                close_parantheses_popcounter += 1
    return ' '


def parantheses(string):
    check = getparan(string)
    original_check = check
    while True:
        modified_string = string.pop(string[0]).pop(string[-1])
        if len(find('**', string)) > 0:
            check = exponents(string)
        elif '(' in modified_string:
            check = parantheses(modified_string)
        elif len(find('*', check)) > 0:
            check = multiplication(check)
        elif len(find('/', check)) > 0:
            check = division(check)
        else:
            string = string.replace(original_check, check)


def left_right_expontent_paranthese_check(string):
    original_string = string
    while True:
        parantheses_set_one = getparan(string)
        parantheses_set_two = getparan(string)
        if find(f'{parantheses_set_one} ** {parantheses_set_two}') in string:
            print('brackets left and right')
            pass
        elif find(f'{parantheses_set_one} **') in string:
            print('brackets left')
            string = string.pop(parantheses_set_two)
        elif find(f'** {parantheses_set_two}') in string:
            print('brackets right')
            string = string.pop(parantheses_set_one)
        else:
            string = string.pop(parantheses_set_one).pop(parantheses_set_two)
        if '(' not in string.pop(parantheses_set_one).pop(parantheses_set_two):
            print('Breaking')
            break
    if find(f'{parantheses_set_one} ** {parantheses_set_two}') in string:
        print('brackets left and right')
        solved_parantheses_set_one = parantheses(parantheses_set_one)
        solved_parantheses_set_two = parantheses(parantheses_set_two)
        return original_string.replace(parantheses_set_one, solved_parantheses_set_one).replace(parantheses_set_two, solved_parantheses_set_two)
    elif find(f'{parantheses_set_one} **') in string:
        print('brackets left')
        solved_parantheses_set_one = parantheses(parantheses_set_one)
        return original_string.replace(parantheses_set_one, solved_parantheses_set_one)
    elif find(f'** {parantheses_set_two}') in string:
        print('brackets right')
        solved_parantheses_set_two = parantheses(parantheses_set_two)
        return original_string.replace(parantheses_set_two, solved_parantheses_set_two)
    
    
def exponents(string):
    print('exponents working')
    string = left_right_expontent_paranthese_check(string)
    original_string = string
    print('initializingallxyvar')
    all_xy_var = get_all_xy_var(string)
    while True:
        if find(f'{all_xy_var[0]} ** {all_xy_var[1]}') in string:
            print('xy left and right')
        elif find(f'{all_xy_var[0]} **') in string:
            print('xy left')
            string = string.pop(all_xy_var[1])
            saved_left = all_xy_var[0]
        elif find(f'** {all_xy_var[1]}') in string:
            print('xy right')
            string = string.pop(all_xy_var[0])
            saved_right = all_xy_var[1]
        else:
            try:
                string = string.pop(all_xy_var[0]).pop(all_xy_var[1])
            except:
                if len(saved_left) > 0:
                    all_numbers = get_all_numbers(string)
                    while True:
                        if find(f'{saved_left} ** {all_numbers[1]}') in string:
                            saved_left_digits = find('-') + find_all_numbers(saved_left)
                            saved_left_xy = find_all_xy(saved_left)
                            number = all_numbers[1]
                            result = saved_left_digits ** number + saved_left_xy
                            break
                        else:
                            all_numbers.pop(all_numbers[1])
                elif len(saved_right) > 0:
                    all_numbers = get_all_numbers(string)
                    while True:
                        if find(f'{all_numbers[1]} ** {saved_right}') in string:
                            saved_right_digits = find('-') + find_all_numbers(saved_right)
                            saved_right_xy = find_all_xy(saved_right)
                            number = all_numbers[1]
                            result = saved_right_digits ** number + saved_right_xy
                            break
                        else:
                            all_numbers.pop(all_numbers[1])
                else:
                    string = str(original_string)
                    all_numbers = get_all_numbers(string)
                    if find(f'{all_numbers[0]} ** {all_numbers[1]}') in string:
                        print('xy left and right')
                    elif find(f'{all_numbers[0]} **') in string:
                        print('xy left')
                        string = string.pop(all_numbers[1])
                        saved_left = all_numbers[0]
                    elif find(f'** {all_numbers[1]}') in string:
                        print('xy right')
                        string = string.pop(all_numbers[0])
                        saved_right = all_numbers[1]
                    else:
                        try:
                            string = string.pop(all_xy_var[0]).pop(all_xy_var[1])
                        except:
                            result = saved_left ** saved_right
                            break
        string = str(original_string)
        variable = []
        for char in string:
            if char == '*':
                if string[char - 1] + char + string[char + 1] + string[char + 2] == ' ** ':
                    temp_list = []
                    counter = 1
                    while True:
                        counter += 1
                        if string[char - counter] in '-1234567890xy':
                            temp_list.replace(temp_list[0], temp_list[0] + string[char - counter])
                        else: 
                            break
                    counter = 2
                    temp_list.append('')
                    while True:
                        counter += 1
                        if string[char + counter] in '-1234567890xy':
                            temp_list.replace(temp_list[1], temp_list[1] + string[char - counter])
                        else: 
                            break
                    variable = variable.append(temp_list)
            else:
                pass
        variable_one = variable[0][0]
        variable_two = variable[0][1]
        return original_string.replace(f'{variable_one} ** {variable_two}', result)
            

def number_mover(string, split_string, symbols):
    for charecter in split_string[0]:
        if split_string[0][find_location(charecter) + 1].isdigit():
            if ' ' + charecter + split_string[0][find_location(charecter) + 1]:
                moving_number.append(charecter)
        elif charecter.isdigit() and not symbols in split_string[0][find_location(charecter) + 1]:
            if ' ' + charecter in split_string[0]:
                moving_number.append(charecter) 
            elif ' -' + charecter in split_string[0]:
                moving_number = moving_number.pop().append(moving_number[-1] + charecter)
    if len(moving_number) > 0:
        for item in  moving_number:
            if '0' in moving_number[0]:
                # Removes the current value on the left
                string = string[:string.find(moving_number[item])] + string[string.find(moving_number[item]) + len(moving_number[item]):]
                # Adds the the value to the other side
                string = string[string.find('='):] + ' + ' + moving_number[item] + '' + string[:string.find('=')]
                return string
            else:
                # Removes the current value on the left
                string = string[:string.find(moving_number[item])] + string[string.find(moving_number[item]) + len(moving_number[item]):]
                # Adds the the value to the other side
                string = string[string.find('='):] + ' + ' + -int(moving_number[item]) + '' + string[:string.find('=')]
                return string
            

def isolate_y(string, split_string):
    print('looking for y')
    checklist = split_string[1].split(' ')
    try:
        split_string = string.split('=')
        if 'x' in split_string[0]:
            isolate_x(string)
    finally:
        for item in checklist:
            found_y = find_location('y', item)
            found_numbers = found_numbers(item)
            if len(split_string[0]) == 0:
                if len(split_string[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                    string = string.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
                else:
                    string = string.replace(checklist[item] + ' ' + checklist[item+1], '')
                split_string = string.split('=')
                string = split_string[0] + str(-int(found_numbers)) + found_y + split_string[1]
                return string
            elif len(split_string[0]) > 0:
                if len(split_string[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                    string = string.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
                else: 
                    string = string.replace(checklist[item] + ' ' + checklist[item+1], '')
                split_string = string.split('=')
                string = split_string[0] + ' + ' + str(-int(found_numbers)) + found_y + split_string[1]
                return string


def isolate_x(string, split_string):
    checklist = split_string[1].split(' ')
    for item in checklist:
        found_x = find('x', item)
        found_numbers = find_all_numbers(item)
        if len(split_string[0]) == 0:
            if len(split_string[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                string = string.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
            else:
                string = string.replace(checklist[item] + ' ' + checklist[item+1], '')
            split_string = string.split('=')
            string = split_string[0] + str(-int(found_numbers)) + found_x + split_string[1]
            return string
        elif len(split_string[0]) > 0:
            if len(split_string[1].replace(checklist[item] + ' ' + checklist[item+1], '')) > 0:
                string = string.replace(checklist[item] + ' ' + checklist[item+1] + ' ', '')
            else: 
                string = string.replace(checklist[item] + ' ' + checklist[item+1], '')
            split_string = string.split('=')
            string = split_string[0] + ' + ' + str(-int(found_numbers)) + found_x + split_string[1]
            return string


def solve(string):
    print('solve initalized')
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')

    if '=' not in string:
        print('no =')
        string = f'{string} = {string}'

    split_string = string.split('=')

    print('eq')
    print(string, '\n')

    parantheses_check = len(find(r'\((.+?)\)', string)) 
    exponents_check = len(find(r'\s(\*{2})\s', string))
    multiplication_check = len(find(r'\s\*\s', string))
    division_check = len(find(r'\s\/\s', string))
    check = '(' or ')' or '*' or '/'
    while check not in string:
        if parantheses_check > 0:
            string = parantheses(string)
            print(string)
            return string
        elif exponents_check > 0:
            string = exponents(string)
            print(string)
            return string
        elif multiplication_check > 0:
            string = multiplication(string)
            print(string)
            return string
        elif division_check > 0:
            string = division(string)
            print(string)
            return string     
        
        elif len(find(r'\s*-*\b(\d+)\b\s*', split_string[0])) != 0:
            string = number_mover(string, split_string, x or y)
            print(string)
            return string

        else:
            if 'y' in string:
                if 'y' in split_string[1]:
                    print('started')
                    string = isolate_y(string, split_string)
                    print(string)
                    exit(1)
                exit(1)
            elif 'x' in string:
                string = isolate_x(string, split_string)
                print(string)
                exit(1)
            else:
                print('No Solution')
                exit(0)


def main():
    while True:
        
        print('Please enter an equation')
        eq = input('> ').lower().strip()

        if 'quit' == eq.lower():
            break

        elif 'exit' == eq.lower():
            break

        elif 'close' == eq.lower():
            break

        else:
            solve(eq)


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
