# (123) 456-7890
def create_phone_number(n):
    b = '('
    for index, val in enumerate(n):
        if index <= 2:
            b += f'{val}'
    b += ') '
    for index, val in enumerate(n):
        if 2 < index <= 5:
            b += f'{val}'
    b += '-'
    for index, val in enumerate(n):
        if 5 < index <= 9:
            b += f'{val}'
    return b


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
