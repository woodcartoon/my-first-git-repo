# this code i wrote it to practice multiple def functions
# my challenge was to use multiple def functions to get the user's name, surname and age and then print a message with the user's name, surname and age
def name():
    user_name = input("please enter your name: ".strip().upper())
    return user_name


def surname():
    user_surname = input("please enter your surname: ".strip().upper())
    return user_surname


def age():
    user_age = int(input("please enter your age: "))
    return user_age


def output():
    user_n = name()
    user_s = surname()
    user_a = age()
    print(f"hello {user_n} {user_s}, now we know you are {user_a}")


output()
# this code is used to get the user's name, surname and age and then print a message with the user's name, surname and age
