
import numpy as np
from matplotlib import pyplot as plt

# print( plt.style.available )
plt.style.use('fivethirtyeight')

year = [ 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

width = 0.25
indices = np.arange(len(year))

population_china = [1.359, 1.397, 1.403, 1.409, 1.415, 1.42, 1.424, 1.428, 1.431, 1.434]

population_india = [1.23, 1.309, 1.324, 1.339, 1.354, 1.368, 1.383, 1.397, 1.411, 1.425]

plt.bar(indices - width, population_india, width=width, label="India", color="green")

plt.bar(indices, population_china, width=width, label="China", color="red")

plt.title(" Population Comparison between India and China")
plt.xlabel('Year')
plt.ylabel('Population in Billions')
plt.legend()

plt.xticks(ticks=indices, labels=year)



plt.tight_layout()
plt.grid(True)
plt.show()