import numpy as np
data = np.loadtxt(
    fname = 'data/inflammation-01.csv'
    delimiter = ','
)

import matplotlib.pyplot as plt

fig =  matplotlib.pyplot.figure.(figsize=(3.0,8.0))

axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig.tight_layout()
