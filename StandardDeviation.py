# Jarrod Li
# 11 November 2016
# Program to determine the standard deviation of a set of numbers

import math

numbers = []
rt = 0
ul = []
nrt = 0


def main(n):

    global numbers
    global rt
    global ul
    global nrt

    if not n:

        for i in numbers:
            rt += int(i)

        mean = int(rt) / len(numbers)

        for i in numbers:
            x = ((int(i) - int(mean))**2)
            ul.append(x)

        for i in ul:
            nrt += i

        print("σ =", math.sqrt(nrt / len(numbers)))

    else:

        numbers.append(n)
        main(input("x1: "))

main(input("x1: "))




