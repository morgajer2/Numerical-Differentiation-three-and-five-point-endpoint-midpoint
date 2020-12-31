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

