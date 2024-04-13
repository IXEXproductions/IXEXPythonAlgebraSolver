import re 
string = 'xxyxxyxyxy yxxy yyx xy'
x_or_y = r"(\bx\b|\by\b|\bx(?:[^\s]+)y\b|\by(?:[^\s]+)x\b|\bx(?:[^\s]+)x\b|\by(?:[^\s]+)y\b|\bxy\b|\byx\b)"
found = re.findall(x_or_y, string)
print(found)

string = ' 6x '
print(re.findall(r'\b\d*' + 'x', string))