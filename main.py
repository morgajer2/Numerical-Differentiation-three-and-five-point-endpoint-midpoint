from sympy import *


def threePointEndpoint(f, x0, h):
    # building values table for the func:
    g = {x0: f(x0), x0 + h: f(x0 + h), x0 + 2 * h: f(x0 + 2 * h)}
    # calculating the derivative
    return (((-3) * g[x0]) + (4 * g[x0 + h]) - (g[x0 + 2 * h])) / (2 * h)


def threePointMidpoint(f, x0, h):
    # building values table for the func:
    g = {x0 + h: f(x0 + h), x0 - h: f(x0 - h)}
    # calculating the derivative
    return (g[x0 + h] + (-1) * (g[x0 - h])) / (2 * h)


def fivePointMidpoint(f, x0, h):
    # building values table for the func:
    g = {x0 - 2 * h: f(x0 - 2 * h), x0 - h: f(x0 - h), x0 + h: f(x0 + h),
         x0 + 2 * h: f(x0 + 2 * h)}
    # calculating the derivative
    return (g[x0 - 2 * h] + (-8) * g[x0 - h] + 8 * g[x0 + h] - (
        g[x0 + 2 * h])) / (12 * h)


def fivePointEndpoint(f, x0, h):
    # building values table for the func:
    g = {x0: f(x0), x0 + h: f(x0 + h), x0 + 2 * h: f(x0 + 2 * h),
         x0 + 3 * h: f(x0 + 3 * h), x0 + 4 * h: f(x0 + 4 * h)}
    # calculating the derivative
    return ((-25) * g[x0] + 48 * g[x0 + h] + (- 36) * g[x0 + 2 * h] + 16 * g[
        x0 + 3 * h] + (- 3) * g[x0 + 4 * h]) / (12 * h)


#main

# getting the func
x = var('x')
user_func = input("please enter the function: ")
expr = sympify(user_func)
f = lambdify(x, expr)

# getting x0 and h
x0 = float(input("please enter x0: "))
h = float(input("please enter h: "))

print("please choose from the following methods:\n1.Three Point Endpoint")
print("2.Three Point Midpoint\n3.Five Point Midpoint\n4.Five Point Endpoint")
choice = int(input("your choice: "))

if choice == 1:
    print("f'(x0) = " + str(threePointEndpoint(f, x0, h)))
elif choice == 2:
    print("f'(x0) = " + str(threePointMidpoint(f, x0, h)))
elif choice == 3:
    print("f'(x0) = " + str(fivePointMidpoint(f, x0, h)))
elif choice == 4:
    print("f'(x0) = " + str(fivePointEndpoint(f, x0, h)))
