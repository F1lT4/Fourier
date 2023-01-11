from math import sin, cos, atan, pi
# define the signal time step
dt_step = 0.02

yt_point_list = []  # will add the points y from file

signal_string = ""

# open the signal
with open("Y(t).txt", "r") as f:
    for line in f:
        signal_string += line

string_list = list(signal_string.split("\n"))

for i in range(0, len(string_list)):
    yt_point_list.append(float(string_list[i]))

# basic variables

duration = dt_step * (len(yt_point_list) - 1)

freq_max = 0.5 / dt_step

freq_min = 1 / duration

d_freq = freq_max

k_v = 1

while d_freq >= freq_min:
    d_freq = freq_max / (2 ** k_v)

    k_v += 1

# define l steps (number of frequencies)

l_steps = 50

# fft

# fi list
freq_list = []

fi = d_freq  # first frequency

for i in range(0, l_steps):
    freq_list.append(fi)
    fi += d_freq

# ki list

ki_list = []

for j in range(0, len(freq_list)):
    ki_list.append(freq_list[j] * (duration + dt_step))
# Ck (cos(2pk/n)) list and Sk list (sin(2pk/n))

Ck_list = []
Sk_list = []

N_steps = len(yt_point_list)

for k in range(0, len(ki_list)):
    ck_step = 0
    sk_step = 0
    for n in range(1, N_steps+1):
        ck_step += yt_point_list[n - 1] * cos(2 * pi * ki_list[k] * n / N_steps)
        sk_step += yt_point_list[n - 1] * sin(2 * pi * ki_list[k] * n / N_steps)

    Ck_list.append(ck_step)
    Sk_list.append(sk_step)
# Amplitude list and phase list
Fk_list = []
phase_list = []


for k in range(0, len(Ck_list)):
    Fk_list.append(dt_step * (Ck_list[k] ** 2 + Sk_list[k] ** 2) ** 0.5)
    phase_list.append(-atan(Sk_list[k] / Ck_list[k]))

with open("FFT.txt", "w") as f:
    st = "          fi       |          Fk       |         phk       |\n"
    for i in range(0, len(freq_list)):
        st += str(freq_list[i]).ljust(19) + " "
        st += str(round(Fk_list[i], 14)).ljust(19) + " "
        st += str(round(phase_list[i], 14)).ljust(19) + "\n"
    f.write(st)
