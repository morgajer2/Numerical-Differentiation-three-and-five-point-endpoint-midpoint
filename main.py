def threePointEndpoint(f, x0, h):
    return (((-3) * f[x0]) + (4 * f[round(x0 + h, 10)]) - (f[round(x0 + 2 * h, 10)])) / (2 * h)

def threePointMidpoint(f, x0, h):
    return(f[round(x0 + h, 10)] + (-1) * (f[round(x0 - h, 10)])) / (2 * h)


def fivePointMidpoint(f, x0, h):
    return (f[round(x0 - 2 * h, 10)] + (-8) * f[round(x0 - h, 10)] + 8 * f[round(x0 + h, 10)] - (f[round(x0 + 2 * h, 10)]))/ (12 * h)


def fivePointEndpoint(f, x0, h):
    return ((-25) * f[round(x0, 10)] + 48 * f[round(x0 + h, 10)] + (- 36) * f[round(x0 + 2 * h, 10)] + 16 * f[
        round(x0 + 3 * h, 10)] + (- 3) * f[round(x0 + 4 * h, 10)]) / (12 * h)

#x^3 -8*x^2 +3


x0 = 0
h = 0.1
f = {-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = 0.5
h = 0.1
f = {0.3: 2.307, 0.4: 1.784, 0.5: 1.125, 0.6: 0.336, 0.7: -0.577, 0.8: -1.608, 0.9: 2.751}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = -0.4
h = 0.1
f = {-0.6:-0.096,-0.5:0.875,-0.4:1.656,-0.3:2.253,-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = 1
h = 0.1
f = {0.3: 2.307, 0.4: 1.784, 0.5: 1.125, 0.6: 0.336, 0.7: -0.577, 0.8: -1.608, 0.9: -2.751, 1:-4, 1.1:-5.349, 1.2:-6.792, 1.3:-8.323, 1.4:-9.936}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = 1.5
h = 0.1
f = {0.3: 2.307, 0.4: 1.784, 0.5: 1.125, 0.6: 0.336, 0.7: -0.577, 0.8: -1.608, 0.9: 2.751, 1:-4, 1.1:-5.349, 1.2:-6.792, 1.3:-8.323, 1.4:-9.936, 1.5:-11.625, 1.6:-13.384,1.7:-15.207,1.8:-17.088,1.9:-19.021}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = -1
h = 0.1
f = {-1.2:-10.248,-1.1:-8.011,-1:-6,-0.9:-4.209,-0.8:-2.632,-0.7:-1.263,-0.6:-0.096,-0.5:0.875,-0.4:1.656,-0.3:2.253,-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))


print("-----")
x0 = -3
h = 0.1
f = {-3.1:-103.671,-3.2:-111.688,-3.0:-96,-2.9:-88.669,-2.8:-81.672,-2.7:-75.003,-2.6:-68.656,-1.2:-10.248,-1.1:-8.011,-1:-6,-0.9:-4.209,-0.8:-2.632,-0.7:-1.263,-0.6:-0.096,-0.5:0.875,-0.4:1.656,-0.3:2.253,-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))


print("-----")
x0 = -5
h = 0.1
f = {-5:-322,-5.1:-337.731,-5.2:-353.928,-4.9:-306.729,-4.8:-291.912,-4.7:-277.543,-4.6:-263.616,-1.2:-10.248,-1.1:-8.011,-1:-6,-0.9:-4.209,-0.8:-2.632,-0.7:-1.263,-0.6:-0.096,-0.5:0.875,-0.4:1.656,-0.3:2.253,-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = 3
h = 0.1
f = {3:-42,2.9:-39.891,2.8:-37.768,3.1:-44.089,3.2:-46.152,3.3:-48.183,3.4:-50.176,-1.2:-10.248,-1.1:-8.011,-1:-6,-0.9:-4.209,-0.8:-2.632,-0.7:-1.263,-0.6:-0.096,-0.5:0.875,-0.4:1.656,-0.3:2.253,-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))

print("-----")
x0 = 5
h = 0.1
f = {5:-72,4.9:-71.431,4.8:-70.728,5.1:-72.429,5.2:-72.712,5.3:-72.843,5.4:-72.816,3:-42,2.9:-39.891,2.8:-37.768,3.1:-44.089,3.2:-46.152,3.3:-48.183,3.4:-50.176,-1.2:-10.248,-1.1:-8.011,-1:-6,-0.9:-4.209,-0.8:-2.632,-0.7:-1.263,-0.6:-0.096,-0.5:0.875,-0.4:1.656,-0.3:2.253,-0.2: 2.672, -0.1: 2.919, 0.0: 3, 0.1: 2.921, 0.2: 2.688, 0.3: 2.307, 0.4: 1.784}
print(threePointEndpoint(f, x0, h))
print(threePointMidpoint(f, x0, h))
print(fivePointMidpoint(f, x0, h))
print(fivePointEndpoint(f, x0, h))