from math import pi, cos, sin
import matplotlib.pyplot as plt
import numpy as np

# define the functions
# Number of sample points

N = 800*8

i = 1

# sample spacing

T = 1.0 / 800.0

x = np.linspace(-8, N*T, N, endpoint=False)


def block_inter(func, low, up, step=0.0001):
    i = low
    area = 0
    while i < up:
        area += func(i) * step
        i += step
    return area


def funcy(xf):
    fy = 5 * abs((((xf - 1) % 4) + 4) % 4 - 2) - 5
    return fy


def funcy1(xf):
    global i
    fy = (5 * abs((((xf - 1) % 4) + 4) % 4 - 2) - 5) * cos(i * xf)
    return fy


def funcy2(xf):
    global i
    fy = (5 * abs((((xf - 1) % 4) + 4) % 4 - 2) - 5) * sin(i * xf)
    return fy


# define the funtsion series
alpha_zero = block_inter(funcy, -pi, pi) / 2 / pi
new_fanc_y = str(alpha_zero)

while i < 100:

    alpha_one = block_inter(funcy1, -pi, pi) / 2 / pi
    alpha_two = block_inter(funcy2, -pi, pi) / 2 / pi

    if alpha_one >= 0:
        new_fanc_y += "+" + str(alpha_one) + "*" + f"cos({i}*j)"
    else:
        new_fanc_y += str(alpha_one) + "*" + f"cos({i}*j)"

    if alpha_two >= 0:
        new_fanc_y += "+" + str(alpha_two) + "*" + f"sin({i}*j)"
    else:
        new_fanc_y += str(alpha_two) + "*" + f"sin({i}*j)"
    i += 1

print(new_fanc_y)

def str_to_number(num):
    global new_fanc_y
    j = num
    res = eval(new_fanc_y)
    return res


y = np.vectorize(str_to_number)

plt.plot(x, y(x))

plt.grid()

plt.show()
