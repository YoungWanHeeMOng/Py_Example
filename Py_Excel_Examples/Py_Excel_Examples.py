
### test classification dataset
##from sklearn.datasets import make_classification
### define dataset
##X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=1)
### summarize the dataset
##print(X.shape, y.shape)

## evaluate logistic regression using repeated stratified k-fold cross-validation
#from numpy import mean
#from numpy import std
#from sklearn.datasets import make_classification
#from sklearn.model_selection import RepeatedStratifiedKFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score
## create dataset
#X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=1)
## prepare the cross-validation procedure
#cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
#scores = list()
#for train_ix, test_ix in cv.split(X, y):
#	# split the data
#	X_train, X_test = X[train_ix], X[test_ix]
#	y_train, y_test = y[train_ix], y[test_ix]
#	# fit model
#	model = LogisticRegression()
#	model.fit(X_train, y_train)
#	# evaluate model
#	y_hat = model.predict(X_test)
#	acc = accuracy_score(y_test, y_hat)
#	scores.append(acc)
## report performance
#print('Accuracy: %.3f (%.3f)' % (mean(scores), std(scores)))

## evaluate logistic regression using test-time augmentation
#from numpy.random import seed
#from numpy.random import normal
#from numpy import mean
#from numpy import std
#from scipy.stats import mode
#from sklearn.datasets import make_classification
#from sklearn.model_selection import RepeatedStratifiedKFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score

## create a test set for a row of real data with an unknown label
#def create_test_set(row, n_cases=3, feature_scale=0.2):
#	test_set = list()
#	test_set.append(row)
#	# make copies of row
#	for _ in range(n_cases):
#		# create vector of random gaussians
#		gauss = normal(loc=0.0, scale=feature_scale, size=len(row))
#		# add to test case
#		new_row = row + gauss
#		# store in test set
#		test_set.append(new_row)
#	return test_set

## make predictions using test-time augmentation
#def test_time_augmentation(model, X_test):
#	# evaluate model
#	y_hat = list()
#	for i in range(X_test.shape[0]):
#		# retrieve the row
#		row = X_test[i]
#		# create the test set
#		test_set = create_test_set(row)
#		# make a prediction for all examples in the test set
#		labels = model.predict(test_set)
#		# select the label as the mode of the distribution 
#		label, _ = mode(labels)
#		# store the prediction
#		y_hat.append(label)
#	return y_hat

## initialize numpy random number generator
#seed(1)
## create dataset
#X, y = make_classification(n_samples=100, n_features=20, n_informative=5, n_redundant=5, random_state=1)
## prepare the cross-validation procedure
#cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
#scores = list()
#for train_ix, test_ix in cv.split(X, y):
#	# split the data
#	X_train, X_test = X[train_ix], X[test_ix]
#	y_train, y_test = y[train_ix], y[test_ix]
#	# fit model
#	model = LogisticRegression()
#	model.fit(X_train, y_train)
#	# make predictions using test-time augmentation
#	y_hat = test_time_augmentation(model, X_test)
#	# calculate the accuracy for this iteration
#	acc = accuracy_score(y_test, y_hat)
#	# store the result
#	scores.append(acc)
## report performance
#print('Accuracy: %.3f (%.3f)' % (mean(scores), std(scores)))


## compare the number of synthetic examples created during the test-time augmentation
#from numpy.random import seed
#from numpy.random import normal
#from numpy import mean
#from numpy import std
#from scipy.stats import mode
#from sklearn.datasets import make_classification
#from sklearn.model_selection import RepeatedStratifiedKFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score
#from matplotlib import pyplot

## create a test set for a row of real data with an unknown label
#def create_test_set(row, n_cases=3, feature_scale=0.2):
#	test_set = list()
#	test_set.append(row)
#	# make copies of row
#	for _ in range(n_cases):
#		# create vector of random gaussians
#		gauss = normal(loc=0.0, scale=feature_scale, size=len(row))
#		# add to test case
#		new_row = row + gauss
#		# store in test set
#		test_set.append(new_row)
#	return test_set

## make predictions using test-time augmentation
#def test_time_augmentation(model, X_test, cases):
#	# evaluate model
#	y_hat = list()
#	for i in range(X_test.shape[0]):
#		# retrieve the row
#		row = X_test[i]
#		# create the test set
#		test_set = create_test_set(row, n_cases=cases)
#		# make a prediction for all examples in the test set
#		labels = model.predict(test_set)
#		# select the label as the mode of the distribution
#		label, _ = mode(labels)
#		# store the prediction
#		y_hat.append(label)
#	return y_hat

## evaluate different number of synthetic examples created at test time
#examples = range(1, 121)
#results = list()
#for e in examples:
#	# initialize numpy random number generator
#	seed(1)
#	# create dataset
#	X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=1)
#	# prepare the cross-validation procedure
#	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
#	scores = list()
#	for train_ix, test_ix in cv.split(X, y):
#		# split the data
#		X_train, X_test = X[train_ix], X[test_ix]
#		y_train, y_test = y[train_ix], y[test_ix]
#		# fit model
#		model = LogisticRegression()
#		model.fit(X_train, y_train)
#		# make predictions using test-time augmentation
#		y_hat = test_time_augmentation(model, X_test, e)
#		# calculate the accuracy for this iteration
#		acc = accuracy_score(y_test, y_hat)
#		# store the result
#		scores.append(acc)
#	# report performance
#	print('>%d, acc: %.3f (%.3f)' % (e, mean(scores), std(scores)))
#	results.append(mean(scores))
## plot the results
#pyplot.plot(examples, results)
#pyplot.show()




# compare amount of noise added to examples created during the test-time augmentation
from numpy.random import seed
from numpy.random import normal
from numpy import arange
from numpy import mean
from numpy import std
from scipy.stats import mode
from sklearn.datasets import make_classification
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

# create a test set for a row of real data with an unknown label
def create_test_set(row, n_cases=3, feature_scale=0.2):
	test_set = list()
	test_set.append(row)
	# make copies of row
	for _ in range(n_cases):
		# create vector of random gaussians
		gauss = normal(loc=0.0, scale=feature_scale, size=len(row))
		# add to test case
		new_row = row + gauss
		# store in test set
		test_set.append(new_row)
	return test_set

# make predictions using test-time augmentation
def test_time_augmentation(model, X_test, noise):
	# evaluate model
	y_hat = list()
	for i in range(X_test.shape[0]):
		# retrieve the row
		row = X_test[i]
		# create the test set
		test_set = create_test_set(row, feature_scale=noise)
		# make a prediction for all examples in the test set
		labels = model.predict(test_set)
		# select the label as the mode of the distribution
		label, _ = mode(labels)
		# store the prediction
		y_hat.append(label)
	return y_hat

# evaluate different number of synthetic examples created at test time
noise = arange(0.01, 0.31, 0.01)
results = list()
for n in noise:
	# initialize numpy random number generator
	seed(1)
	# create dataset
	X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=1)
	# prepare the cross-validation procedure
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
	scores = list()
	for train_ix, test_ix in cv.split(X, y):
		# split the data
		X_train, X_test = X[train_ix], X[test_ix]
		y_train, y_test = y[train_ix], y[test_ix]
		# fit model
		model = LogisticRegression()
		model.fit(X_train, y_train)
		# make predictions using test-time augmentation
		y_hat = test_time_augmentation(model, X_test, n)
		# calculate the accuracy for this iteration
		acc = accuracy_score(y_test, y_hat)
		# store the result
		scores.append(acc)
	# report performance
	print('>noise=%.3f, acc: %.3f (%.3f)' % (n, mean(scores), std(scores)))
	results.append(mean(scores))
# plot the results
pyplot.plot(noise, results)
pyplot.show()