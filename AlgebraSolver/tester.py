import os
import time

os.system("cls")

try:
    import sympy
except Exception as e:
    print('Error with import, please install imports.')
    print('Hint - \'pip install sympy\'')

def simplify(original_var):
    obj_var = sympy.simplify(original_var)
    return obj_var

def change_var(original_var, int_var, change):
    output_var = str(original_var).replace(str(int_var), f"{change}")
    return output_var

def change_x_y(obj_var, intinputx, intinputy, addorremove):
    if addorremove == "add":
        temp_var_change = "+"
        
    if addorremove == "remove":
        temp_var_change = "-"

    temp_obj_var = str(obj_var)

    if 'x' in str(obj_var):
        temp_var = "x"
        temp_obj_var = str(temp_obj_var).replace(temp_var, f"{temp_var_change}{intinputx}")

    if 'y' in str(obj_var):
        temp_var = "y"
        temp_obj_var = str(temp_obj_var).replace(temp_var, f"{temp_var_change}{intinputy}")
    
    return temp_obj_var

def pre_solver(original_var, x, y):
    try:
        obj_var = simplify(original_var)
        ## do not make obj_var a str, its a python obj right now

        if 'x' in str(obj_var) and 'y' not in str(obj_var):
            # Solve for "x"
            result = sympy.solve(obj_var, x)

        elif 'y' in str(obj_var) and 'x' not in str(obj_var):
            # Solve for "y"
            result = sympy.solve(obj_var, y)
        
        elif 'x' in str(obj_var) and 'y' in str(obj_var):
            # Solve for "x" and "y"
            result = sympy.solve(obj_var, x, y)
        
        else:
            result = obj_var

    except Exception as e:
        print(f"Any Error as happened: {str(e)}")
        result = obj_var
    
    return result


def solve(var, original_var):
    # x ** (2) = 9
    temp_var_str_print = ""

    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    if '=' in var:
        print("Equal sign detected")
        sides = var.split('=')

        var_x = 0
        var_y = 0

        soft_cap = 100

        left_pre_result = sides[0]
        right_pre_result = sides[1]

        print(f"Left Pre Result: {left_pre_result}")
        print(f"Right Pre Result: {right_pre_result}")
        
        print(f"Thinking please wait...")

        while True:
            try:
                math_list_temp = []
                soft_cap = soft_cap + 1

                for number_x in range(int(soft_cap) - 1):
                    var_x = number_x
                
                    pos_left_pre_temp_result = change_x_y(left_pre_result, var_x, var_y, "add")
                    pos_right_pre_temp_result = change_x_y(right_pre_result, var_x, var_y, "add")

                    neg_left_pre_temp_result = change_x_y(left_pre_result, var_x, var_y, "remove")
                    neg_right_pre_temp_result = change_x_y(right_pre_result, var_x, var_y, "remove")
                    
                    pos_left_pre_solver = pre_solver(pos_left_pre_temp_result, x, y)
                    pos_right_pre_solver = pre_solver(pos_right_pre_temp_result, x, y)
                    
                    neg_left_pre_solver = pre_solver(neg_left_pre_temp_result, x, y)
                    neg_right_pre_solver = pre_solver(neg_right_pre_temp_result, x, y)
                    
                    math_list_temp.append(pos_left_pre_solver)
                    math_list_temp.append(pos_right_pre_solver)
                    math_list_temp.append(neg_left_pre_solver)
                    math_list_temp.append(neg_right_pre_solver)

                    for number_y in range(int(soft_cap) - 1):
                        var_y = number_y
                    
                        pos_left_pre_temp_result = change_x_y(left_pre_result, var_x, var_y, "add")
                        pos_right_pre_temp_result = change_x_y(right_pre_result, var_x, var_y, "add")

                        neg_left_pre_temp_result = change_x_y(left_pre_result, var_x, var_y, "remove")
                        neg_right_pre_temp_result = change_x_y(right_pre_result, var_x, var_y, "remove")
                        
                        pos_left_pre_solver = pre_solver(pos_left_pre_temp_result, x, y)
                        pos_right_pre_solver = pre_solver(pos_right_pre_temp_result, x, y)
                        
                        neg_left_pre_solver = pre_solver(neg_left_pre_temp_result, x, y)
                        neg_right_pre_solver = pre_solver(neg_right_pre_temp_result, x, y)

                        math_list_temp.append(pos_left_pre_solver)
                        math_list_temp.append(pos_right_pre_solver)
                        math_list_temp.append(neg_left_pre_solver)
                        math_list_temp.append(neg_right_pre_solver)

                for i in range(len(math_list_temp) - 1):
                    print(f"Checking {math_list_temp[i]} vs {math_list_temp[i + 1]}")
                    if math_list_temp[i] == math_list_temp[i + 1]:
                        result = f"{math_list_temp[i]} = {math_list_temp[i + 1]}"
                        found_math_yes = True
                        break
                    else:
                        found_math_yes = False
                        pass
                
                if found_math_yes:
                    break
                else:
                    raise Exception

            except Exception as error:
                print(f"{str(error)} trying more stuff")

    else:
        result = pre_solver(original_var, x, y)
    
    print(str(result))


def main():
    exit_list = ["quit", "close", "exit"]
    while True:
        eq = input('Please enter an equation: ')
        original_eq = str(eq).strip().replace(" ", "")

        if eq.lower() in exit_list:
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
# x * xy = x ** x * y 
# xy / x = y
# x ** x = 0
