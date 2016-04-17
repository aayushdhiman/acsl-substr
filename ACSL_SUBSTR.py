s = input("Enter a string:  ")


def int_converter(z):
    try:
        return int(z)
    except ValueError:
        print('The input "'+x+'" is invalid.')
        raise SystemExit


def sub_str(a, b):
    a = int_converter(a)
    b = int_converter(b)
    if b == 0:
        return s[a:]
    elif b > 0:
        length = a + b
        return s[a:length]
    elif b < 0:
        length = b
        return s[a:length]

inputs = 5
while inputs > 0:
    x, y = input("Enter your next two numbers: ").split(",")
    inputs -= 1
    print(sub_str(x, y))
