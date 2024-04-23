string = 'xy xyyx lol pineapplle xy'
def find_all_xy(string):
    return_string = ''
    for char in string:
        if char == "x":
            return_string = return_string + char
        elif char == "y": 
            return_string = return_string + char
    return return_string
print(find_all_xy(string))