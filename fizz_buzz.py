
# FizzBuzz Game
def fizz_buzz_1():
    for number in range(1, 101):
        if number % 5 == 0:
            if number % 3 == 0:
                print("FizzBuz")
            else:
                print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


def fizz_buzz_2():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


print("fizz_buzz_1:", timeit.timeit(fizz_buzz_1, number=1000))
print("fizz_buzz_2:", timeit.timeit(fizz_buzz_2, number=1000))
