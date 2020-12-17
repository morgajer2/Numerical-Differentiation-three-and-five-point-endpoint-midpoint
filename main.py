def threePointEndpoint(f, x0, h):
    return (((-3) * f[x0]) + (4 * f[round(x0 + h, 10)]) - (f[round(x0 + 2 * h, 10)])) / (2 * h)

def threePointMidpoint(f, x0, h):
    return(f[round(x0 + h, 10)] + (-1) * (f[round(x0 - h, 10)])) / (2 * h)


def fivePointMidpoint(f, x0, h):
    return (f[round(x0 - 2 * h, 10)] + (-8) * f[round(x0 - h, 10)] + 8 * f[round(x0 + h, 10)] - (f[round(x0 + 2 * h, 10)]))/ (12 * h)


def fivePointEndpoint(f, x0, h):
    return ((-25) * f[round(x0, 10)] + 48 * f[round(x0 + h, 10)] + (- 36) * f[round(x0 + 2 * h, 10)] + 16 * f[
        round(x0 + 3 * h, 10)] + (- 3) * f[round(x0 + 4 * h, 10)]) / (12 * h)

