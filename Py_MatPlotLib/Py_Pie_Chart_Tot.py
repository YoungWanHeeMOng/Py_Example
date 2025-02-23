
import numpy as np
from matplotlib import pyplot as plt

# print( plt.style.available )
plt.style.use('fivethirtyeight')

slices = [1433783686, 1366417754, 329064917, 270625568, 216565318 ]

labels = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', ]

explode = [0, 0, 0.2, 0, 0]

colors = ['#C70039', '#FF5733', '#FFC300', '#DAF7A6']

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black', 'linewidth': 1 }, colors=colors)


plt.title("Population Pie Chart")
plt.grid(True)
plt.show()