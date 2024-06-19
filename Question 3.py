#Write a python program that calculates the factorial of a given number.
def FACTORIAL(f):
    if f < 0:
        return 0
    elif f == 0 or f ==1:
        return 1
    else:
        factorial = 1
        while (f>1):
                factorial *=f
                f -= 1

        print(factorial)


f = int(input("Enter a number: "))
print(FACTORIAL(f))