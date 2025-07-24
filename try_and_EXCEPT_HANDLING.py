try:

    num1 = int(input("please enter a number to divide with: "))
    num2 = int(input("please a number: "))

    division = num1 / num2

    print(division)
except ValueError:
    print("enter an integer")
except ZeroDivisionError:
    print("number cannot be divided by zero")


# try and except function is a function that interrupts a program from running into an error
