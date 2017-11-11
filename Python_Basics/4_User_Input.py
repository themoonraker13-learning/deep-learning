def add(num1, num2):
    """Returns addition of two numbers"""
    return num1 + num2


def main():
    my_name = input("What is your name? ")
    print("Hi " + my_name)
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("The sum of the numbers is: " + str(add(num1, num2)))


main()