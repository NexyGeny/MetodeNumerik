import numpy as np
from sympy import Symbol, lambdify

N_MAKS = 30
x = Symbol('x')

def hitung_error(x_baru, x_lama):
    return np.abs(x_baru - x_lama)

def biseksi(a, b, f_x, toleransi):
    a, b = np.float64(a), np.float64(b)
    f = lambdify(x, f_x)
    f_a, f_b = f(a), f(b)
    if f_a * f_b > 0:
        return np.nan, []  # Tidak memenuhi syarat

    hasil_iterasi = []
    iterasi = 1

    while True:
        c = (a + b) / 2
        f_c = f(c)
        lebar = np.abs(b - a)

        hasil_iterasi.append({
            'Iterasi': iterasi,
            'a': a,
            'b': b,
            'c': c,
            'f(a)': f_a,
            'f(b)': f_b,
            'f(c)': f_c,
            'Error': lebar
        })

        if f_c * f_a < 0:
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c

        if lebar < toleransi or iterasi >= N_MAKS:
            break

        iterasi += 1

    return c, hasil_iterasi

def regula_falsi(a, b, f_x, toleransi):
    a, b = np.float64(a), np.float64(b)
    f = lambdify(x, f_x)
    hasil_iterasi = []
    iterasi = 1

    while True:
        f_a, f_b = f(a), f(b)
        c = (f_b * a - f_a * b) / (f_b - f_a)
        f_c = f(c)

        hasil_iterasi.append({
            'Iterasi': iterasi,
            'a': a,
            'b': b,
            'c': c,
            'f(a)': f_a,
            'f(b)': f_b,
            'f(c)': f_c,
            'Error': np.abs(f_c)
        })

        if np.abs(f_c) < toleransi or iterasi >= N_MAKS:
            break

        if f_a * f_c < 0:
            b = c
        else:
            a = c

        iterasi += 1

    return c, hasil_iterasi

def iterasi_sederhana(x_awal, f_x, toleransi):
    f = lambdify(x, f_x)
    x_r = np.float64(x_awal)
    hasil_iterasi = []

    for i in range(1, N_MAKS + 1):
        x_r_1 = f(x_r)
        error = hitung_error(x_r_1, x_r)

        hasil_iterasi.append({
            'Iterasi': i,
            'x_r': x_r,
            'x_r+1': x_r_1,
            'Error': error
        })

        if error < toleransi:
            return x_r_1, hasil_iterasi

        x_r = x_r_1

    return np.inf, hasil_iterasi

def newton_raphson(x_awal, f_x, toleransi):
    f = lambdify(x, f_x)
    f_prime = lambdify(x, f_x.diff(x))
    x_r = np.float64(x_awal)
    hasil_iterasi = []
    iterasi = 1

    while iterasi <= N_MAKS:
        f_val = f(x_r)
        f_deriv = f_prime(x_r)
        if f_deriv == 0:
            return np.nan, hasil_iterasi

        x_r_1 = x_r - f_val / f_deriv
        error = hitung_error(x_r_1, x_r)

        hasil_iterasi.append({
            'Iterasi': iterasi,
            'x_r': x_r,
            'f(x_r)': f_val,
            "f'(x_r)": f_deriv,
            'x_r+1': x_r_1,
            'Error': error
        })

        if error < toleransi:
            return x_r_1, hasil_iterasi

        x_r = x_r_1
        iterasi += 1

    return np.inf, hasil_iterasi

def secant(x_prev, x_curr, f_x, toleransi):
    f = lambdify(x, f_x)
    hasil_iterasi = []
    iterasi = 1

    while iterasi <= N_MAKS:
        f_prev, f_curr = f(x_prev), f(x_curr)
        if f_curr - f_prev == 0:
            return np.nan, hasil_iterasi

        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        error = hitung_error(x_next, x_curr)

        hasil_iterasi.append({
            'Iterasi': iterasi,
            'x_prev': x_prev,
            'x_curr': x_curr,
            'f(x_prev)': f_prev,
            'f(x_curr)': f_curr,
            'x_next': x_next,
            'Error': error
        })

        if error < toleransi:
            return x_next, hasil_iterasi

        x_prev, x_curr = x_curr, x_next
        iterasi += 1

    return np.inf, hasil_iterasi
