# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

def narcissistic(value):
    i = 1
    x = 1
    mylist = []
    while i != 0:
        i = value // x % 10
        x *= 10
        if i != 0:
            mylist.append(i)
        else:
            break
    mylist.reverse()
    y = len(mylist)
    a = 0
    for item in mylist:
        z = item**y
        a += z
    if value == a:
        print(True)
        print(f'{value} is narcissistic')
    else:
        print(False)
        print(f'{value} is not narcissistic')


narcissistic(7)
narcissistic(153)
narcissistic(371)
narcissistic(1652)
narcissistic(48877884)
