import math


def normal(x, mean, sd):
    var = float(sd) ** 2
    pi = 3.1415926
    denom = (2 * pi * var) ** .5
    num = math.exp(-(float(x) - float(mean)) ** 2 / (2 * var))
    return num / denom


def poisson(events, avg):
    e = math.e

    result = (pow(e, -avg) * pow(avg, events)) / math.factorial(events)


    return result