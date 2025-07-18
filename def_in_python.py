digit_one = int(input("Enter the first digit: "))
digit_two = int(input("Enter the second digit: "))


def add_two_number(x, y):
    # this function adds, multiplies and divides two numbers
    sum = x + y
    multiplication = x * y
    division = x/y

    return sum, multiplication, division


# in this code below i am calling this function
# this returns each  of the result in a next line
add_two_number(digit_one, digit_two)

# this prints the results in a tupple set
print(add_two_number(digit_one, digit_two))
