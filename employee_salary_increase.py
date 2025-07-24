# this file is used to increase the salary of an employee by a certain percentage for three employees

count = 0

while count < 3:
    salary = int(input("please enter your salary: "))
    increase = int(input("please enter the percentage increase: "))

    def increase_salary(salary, increase):

        new_salary = salary + (salary * increase / 100)
        print(f"Your new salary is: R{new_salary}")
        return new_salary
    increase_salary(salary, increase)
    count += 1
