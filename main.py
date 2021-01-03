from sympy import *

x = Symbol('x')

def threePointEndpoint(f, x0, h):
    # building values table for the func:
    g = {x0: f.subs(x, x0), x0 + h: f.subs(x, x0 + h), x0 + 2 * h: f.subs(x, x0 + 2 * h)}
    # calculating the derivative
    return (((-3) * g[x0]) + (4 * g[x0 + h]) - (g[x0 + 2 * h])) / (2 * h)


def threePointMidpoint(f, x0, h):
    # building values table for the func:
    g = {x0 + h: f.subs(x, x0 + h), x0 - h: f.subs(x, x0 - h)}
    # calculating the derivative
    return (g[x0 + h] + (-1) * (g[x0 - h])) / (2 * h)


def fivePointMidpoint(f, x0, h):
    # building values table for the func:
    g = {x0 - 2 * h: f.subs(x, x0 - 2 * h), x0 - h: f.subs(x, x0 - h), x0 + h: f.subs(x, x0 + h),
         x0 + 2 * h: f.subs(x, x0 + 2 * h)}
    # calculating the derivative
    return (g[x0 - 2 * h] + (-8) * g[x0 - h] + 8 * g[x0 + h] - (
        g[x0 + 2 * h])) / (12 * h)


def fivePointEndpoint(f, x0, h):
    # building values table for the func:
    g = {x0: f.subs(x, x0), x0 + h: f.subs(x, x0 + h), x0 + 2 * h: f.subs(x, x0 + 2 * h),
         x0 + 3 * h: f.subs(x, x0 + 3 * h), x0 + 4 * h: f.subs(x, x0 + 4 * h)}
    # calculating the derivative
    return ((-25) * g[x0] + 48 * g[x0 + h] + (- 36) * g[x0 + 2 * h] + 16 * g[
        x0 + 3 * h] + (- 3) * g[x0 + 4 * h]) / (12 * h)


f = x ** 3 - 8 * (x ** 2) + 3
x0 = float(input("please enter x0: "))
h = float(input("please enter h: "))
choise = int(input(
    "which method do you want?\n1.Three Point Endpoint\n2.Three Point Midpoint\n3.Five Point Midpoint\n4.Five Point Endpoint"))
if choise == 1:
    print("f'(x0) = "+str(threePointEndpoint(f, x0, h)))
elif choise == 2:
    print("f'(x0) = "+str(threePointMidpoint(f, x0, h)))
elif choise == 3:
    print("f'(x0) = " + str(fivePointMidpoint(f, x0, h)))
elif choise == 4:
    print("f'(x0) = "+str(fivePointEndpoint(f, x0, h)))
