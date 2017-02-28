# Jarrod Li
# 11 November 2016
# Program to solve ax**2 + bx = c

import math


def quadratic(a, b, c):

    d = math.sqrt((b ** 2) - 4 * a * c)

    print("x1 =", ((-b + d) / 2 * a))

    print("x2 =", ((-b - d) / 2 * a))

quadratic(int(input("a: ")), int(input("b: ")), int(input("c: ")))
