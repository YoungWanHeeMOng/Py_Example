
# summarize the horse colic dataset
from pandas import read_csv
# load dataset
#url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/horse-colic.csv'
url='test1.csv'
dataframe = read_csv(url, header=None, na_values='?')
# summarize the first few rows
print(dataframe.head())
# summarize the number of rows with missing values for each column
for i in range(dataframe.shape[1]):
	# count number of rows with missing values
	n_miss = dataframe[[i]].isnull().sum()
	perc = n_miss / dataframe.shape[0] * 100
	print('> %d, Missing: %d (%.1f%%) %s' % (i, n_miss, perc, dataframe[i][2]))
