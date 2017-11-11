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
    """Get User Input"""
    try:
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

    except:
        print("Invalid Input!! The program will now exit.")

main()