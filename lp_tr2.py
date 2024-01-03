import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def traprule(a, b, expr):
    n = int(b * 100)
    a = float(a)
    b = float(b)
    h = float((b - a) / n)
    p = [0.0] * (n + 1)
    y = [0.0] * (n + 1)
    x = sp.symbols('x')
    expr = sp.sympify(expr)
    for i in range(0, n + 1):
        p[i] = a + i * h
    for i in range(0, n + 1):
        y[i] = expr.subs(x, p[i]).evalf()
    ans = (y[0] + y[n]) / 2
    for i in range(1, n):
        ans = ans + y[i]
    ans = ans * h
    return ans

def upperbound(expr, l):
    upp_bd = 10
    x = sp.symbols('x')
    while upp_bd <= 1000000:
        val = expr.subs(x, upp_bd)
        if abs(val - l) <= 0.000001:
            return upp_bd
        else:
            upp_bd = upp_bd * 10
    return "non-computable"

def lap_transform(expr_str, s_values):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    results = []
    for s in s_values:
        lap_expr = sp.exp(-s * x) * expr
        limit_at_infinity = sp.limit(lap_expr, x, sp.oo)
        if limit_at_infinity == sp.oo:
            results.append(float('inf'))
        else:
            limit_at_infinity = float(limit_at_infinity)
            upp_bd = upperbound(lap_expr, limit_at_infinity)
            if upp_bd != "non-computable":
                upp_bd = float(upp_bd)
                result = traprule(0.0, upp_bd, lap_expr)
                results.append(result)
            else:
                results.append(float('nan'))
    return results

# Prompt user for the function f(x)
expr_str = input("Enter the function f(x) for which you want to calculate the Laplace transform: ")

# Define the range of s values from 0.1 to 5 in steps of 0.1
s_values = np.arange(1, 10, 1)

# Calculate Laplace transform for different s values
results = lap_transform(expr_str, s_values)

# Define the custom model function
def custom_func(s, a, b, c):
    return 1 / (a * s ** 2 + b * s + c)

# Fit the function to the data
popt, pcov = curve_fit(custom_func, s_values, results)

# Plot the original data
plt.plot(s_values, results, 'ko', label='Original data')

# Plot the fitted function
s_fit = np.linspace(0.1, 5, 100)
plt.plot(s_fit, custom_func(s_fit, *popt), 'r-', label='Fitted function: 1 / ({:.3f} * s^2 + {:.3f} * s + {:.3f})'.format(*popt))

# Add labels and legend
plt.xlabel('s')
plt.ylabel('Laplace Transform')
plt.title('Fitting 1/(polynomial of s) Function to Data')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
