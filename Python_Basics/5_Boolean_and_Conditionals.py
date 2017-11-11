print(True == True)

print(1 < 2)

print('a' > 'b')

print(5 <= 2)

print('a' >= 'b')


def add(num1, num2):
    """:returns addition of two number"""
    return num1 + num2


def sub(num1, num2):
    """:returns subtraction of two number"""
    return num1 - num2


def mul(num1, num2):
    """:returns multiplication of two number"""
    return num1 * num2


def div(num1, num2):
    """:returns division of two number"""
    return num1 / num2


def main():
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))
    opr = input("Enter operator(+,-,*,/): ")
    if (opr == '+'):
        print(add(n1, n2))
    elif (opr == '-'):
        print(sub(n1, n2))
    elif (opr == '*'):
        print(mul(n1, n2))
    elif (opr == '/'):
        print(div(n1, n2))
    else:
        print("Ivalid operator!!")


main()