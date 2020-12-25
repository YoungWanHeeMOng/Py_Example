
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

days = [1, 2, 3, 4, 5]

eat =   [1, 3, 4, 3, 2]
study = [8, 5, 6, 8, 10]
code =  [6, 8, 7, 4, 1]
sleep = [9, 8, 7, 9, 11]

labels = ['eat', 'study', 'code', 'sleep']

colors = ['m', 'c', 'r', 'k']

plt.stackplot( days, eat, study, code, sleep, labels=labels, colors=colors)

plt.legend(loc=(0.06,0.06))

plt.title("Stack plot")
plt.tight_layout()
plt.grid(True)
plt.show()