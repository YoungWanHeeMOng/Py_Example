

## example of a normalization
#from numpy import asarray
#from sklearn.preprocessing import MinMaxScaler
## define data
#data = asarray([[100, 0.001],
#				[8, 0.05],
#				[50, 0.005],
#				[88, 0.07],
#				[4, 0.1]])
#print(data)
## define min max scaler
#scaler = MinMaxScaler()
## transform data
#scaled = scaler.fit_transform(data)
#print(scaled)


# load and summarize the sonar dataset
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.csv"
dataset = read_csv(url, header=None)
# summarize the shape of the dataset
print(dataset.shape)
# summarize each variable
print(dataset.describe())
# histograms of the variables
dataset.hist()
pyplot.show()
