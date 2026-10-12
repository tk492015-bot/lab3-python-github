def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


def even_odd(n):
    if n % 2 == 0:
        print(n, "Is an even number")
    else:
        print(n, "Is an odd number")


def percentage(a, b):
    if b == 0:
        return "Percentage cannot be found with respect to zero"
    return (a / b) * 100

print("==========Simple calculator============")

while True:
    text = str(input("Type 'Exit' to quit,or press enter to continue =  "))
    if (text == "Exit" or text == "EXIT" or text == "exit"):
        break

    a = int(input("Enter first number = "))
    b = int(input("Enter second number = "))

    print("Addition of numbers = ", addition(a, b))
    print("Subtraction of numbers = ", subtraction(a, b))
    print("Multiplication of numbers = ", multiplication(a, b))
    print("Division of numbers = ", division(a, b))

    c = str(input("Do you want to check whether a number is even/odd =  "))
    if (c == "Yes" or c == "yes"):
        even_odd(a)
        even_odd(b)

    c = str(input("Do you want to find percentage of "+ str(a)+ " with respect to " + str(b) + " = "))
    if (c == "Yes" or c == "yes"):
        print("Percentage is = ", percentage(a, b))
