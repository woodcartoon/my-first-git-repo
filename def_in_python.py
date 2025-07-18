digit_one = int(input("Enter the first digit: "))
digit_two = int(input("Enter the second digit: "))


def add_two_number(x, y):
    # this function adds, multiplies and divides two numbers
    sum = x + y
    addition = print(sum)
    multiplication = x * y
    times = print(multiplication)
    division = x/y
    div = print(division)

    return addition, times, div


# in this code below i am calling this function
# this code will print each result in a new line
add_two_number(digit_one, digit_two)
