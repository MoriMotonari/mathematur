#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#%%
sns.set(rc={'figure.figsize': (12, 12)}, font_scale=1.75)
# POWER
# n is heighest power, lim is xy-limit
n, lim = 7, 1.5
arr = np.arange(-lim*2, lim*2, 0.01)
for i in range(n+1):
    # plt.subplot(1, n, i+1)
    plt.plot(arr, arr ** i, label=f'$y = x^{i}$')

plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim((-lim, lim))
plt.ylim((-lim, lim))
plt.legend()
plt.savefig('power.png', format='png', dpi=plt.gcf().dpi, edgecolor='white', facecolor='white')
plt.show()
#%%
# ROOT
# n is heighest root, lim is xy-limit
n, lim = 7, 1.5
arr = np.arange(-lim*2, lim*2, 0.001)
for i in range(2, n+1):
    # plt.subplot(1, n, i+1)
    plt.plot(arr, arr ** (1/i), label=f'$y = x^{{\\frac{{1}}{{{i}}}}}$')
    plt.plot(arr, arr ** (-1/i), label=f'$y = x^{{-\\frac{{1}}{{{abs(i)}}}}}$')

plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim((-.5, lim))
plt.ylim((-lim, lim))
plt.legend()
plt.savefig('roots.png', format='png', dpi=plt.gcf().dpi, edgecolor='white', facecolor='white')
plt.show()
#%%
# EXPONTENTIAL
# n is heighest base, lim is xy-limit
n, lim = 3, 2
arr = np.arange(-lim*2, lim*2, 0.001)
for i in range(2, n+1):
    # plt.subplot(1, n, i+1)
    plt.plot(arr, i ** arr, label=f'$y = {i}^x$')
    plt.plot(arr, -i ** arr, label=f'$y = -{i}^x$')
    plt.plot(arr, (1/i) ** arr, label=f'$y = (1/{i})^x$')
    plt.plot(arr, -(1/i) ** arr, label=f'$y = -(1/{i})^x$')

plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim((-lim, lim))
plt.ylim((-lim, lim))
plt.legend()
plt.savefig('exponents.png', format='png', dpi=plt.gcf().dpi, edgecolor='white', facecolor='white')
plt.show()
#%%
# MINUS POWER
# n is heighest base, lim is xy-limit
n, lim = 7, 2
arr = np.arange(-lim*2, lim*2, 0.001)
for i in range(-n, 0):
    # plt.subplot(1, n, i+1)
    plt.plot(arr, arr ** i, label=f'$y = x^{{{i}}}$')

plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim((-lim, lim))
plt.ylim((-lim, lim))
plt.legend()
plt.savefig('minuspower.png', format='png', dpi=plt.gcf().dpi, edgecolor='white', facecolor='white')
plt.show()
#%%
# LOGARITHMS
# n is heighest base, lim is xy-limit
n, lim = 7, 2
arr = np.arange(-lim*2, lim*2, 0.001)
for i in range(1, n+1):
    # plt.subplot(1, n, i+1)
    plt.plot(arr, np.log(arr) / np.log(i), label=f'$y = log_{i}(x)$')

plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim((-.5, lim))
plt.ylim((-lim, lim))
plt.legend()
plt.savefig('logarithms.png', format='png', dpi=plt.gcf().dpi, edgecolor='white', facecolor='white')
plt.show()
#%%
# TRIGONOMETRY
# n is heighest base, lim is xy-limit
n, lim = 7, 5
arr = np.arange(-lim*2, lim*2, 0.001)
plt.plot(arr, np.cos(arr), label='$cos(x)$')
plt.plot(arr, np.sin(arr), label='$sin(x)$')
y = np.tan(arr)
threshold = 100
y[y>threshold] = np.inf
y[y<-threshold] = np.inf
plt.plot(arr, y, label='$tan(x)$')
plt.plot(arr, np.arccos(arr), label='$cos^{-1}(x)$')
plt.plot(arr, np.arcsin(arr), label='$sin^{-1}(x)$')
plt.plot(arr, np.arctan(arr), label='$tan^{-1}(x)$')

plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim((-lim, lim))
plt.ylim((-lim, lim))
plt.legend()
plt.savefig('trigonometry.png', format='png', dpi=plt.gcf().dpi, edgecolor='white', facecolor='white')
plt.show()

#%%
