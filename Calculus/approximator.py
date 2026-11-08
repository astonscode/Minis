import math

def validate(text, choices):
    validated = False
    while not validated:
        try:
            choice = input(text)
            if choices == "alltext":
                validated = True
                return choice
            elif choice in choices:
                validated = True
                return choice
            elif int(choice) in choices:
                validated = True
                return int(choice)
            else:
                raise ValueError
        except ValueError:
            print("Please try again.")

def delta(a, b, n):
    return ( b - a ) / n

def range_inclusive(a, b, n):
    dx = delta(a, b, n)
    return [a + i * dx for i in range(n + 1)] #gu

def midpoint(a, b, n, f):
    dx = delta(a, b, n)
    x = range_inclusive(a, b, n)
    total = 0
    # print(x)
    def genMidpoints(x_values):
        # print(x_values)
        midpoints = []
        for i in range(len(x_values) -1):
            midpoints.append((x_values[i] + x_values[i+1]) / 2)
        return midpoints
    for i in genMidpoints(x):
        # print(f(i), total)
        total += f(i)

    # print(dx * total)
    return dx * total

    # generate midpoints
    # for a,b = 0,4 and n = 4: [0, 1] [1, 2] [2, 3] [3, 4]
    # set[M]: [0.5] [1.5] [2.5] [3.5]

def trapezoidal(a, b, n, f):
    dx = delta(a, b, n)
    x = range_inclusive(a, b, n)
    total = 0

    for i in range(0, n + 1):
        if i == 0 or i == n:
            total += f(x[i])
        else:
            total += 2 * f(x[i])
    return (dx/2) * total

def simpson(a, b, n, f):
    dx = delta(a, b, n)
    x = range_inclusive(a, b, n)
    total = 0
    for i in range(0, n+1):
        if i == 0 or i == n:
            total += f(x[i])
        elif i % 2 == 1:
            total += 4 * f(x[i])
        elif i % 2 == 0:
            total += 2 * f(x[i])
    return (dx / 3) * total

assert trapezoidal(0, 4, 4, lambda x: x / 5) == 1.6
assert round(simpson(1, 2, 4, lambda x: 1 / x), 3) == 0.693
assert midpoint(0, 8, 4, lambda x: pow(x, 2)) == 168

def main():
    print("Welcome to Approximator v1.0!")
    select = validate("What approximation would you like to use?\n[1] Midpoint\n[2] Trapezoidal\n[3] Simpson\n> ", range(1,4)) - 1
    intervals = validate("How many intervals (1 < n < 1001)?:\n> ", range(1,1001))
    a = validate("From? (a)\n> ", "alltext")
    b = validate("To? (b)\n> ", "alltext")
    f = validate("Function to parse: ", "alltext")
    print(select, intervals, a, b, f)

main() 


