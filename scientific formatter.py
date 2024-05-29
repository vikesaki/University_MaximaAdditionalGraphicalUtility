import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Sample data
z = range(10)
x = [i * 100 for i in z]
y = [i * 100 for i in x]

fig, ax = plt.subplots()
ax.plot(x, y)

# Define a formatter function
def scientific_formatter(x, pos):
    if x == 0:
        return '0'
    exponent = int(np.floor(np.log10(np.abs(x))))
    coefficient = x / (10**exponent)
    return f'{coefficient:.1f}x$10^{{{exponent}}}$'

# Apply the custom formatter
ax.xaxis.set_major_formatter(ticker.FuncFormatter(scientific_formatter))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(scientific_formatter))

plt.show()