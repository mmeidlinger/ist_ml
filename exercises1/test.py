import numpy as np
import ml

if __name__ == '__main__':

	#Read training/testing data
	D = np.genfromtxt('training1.txt')
	T = np.genfromtxt('testing.txt')

	#Split into data and labels
	Y = D[:,-1]
	X = D[:,:-1]
	T_Y = T[:,-1]
	T = T[:,:-1]

	p = ml.Perceptron()
	ab = ml.AdaBoost()

	train_err, test_err = p.train(X,Y,T,T_Y)
	np.savetxt('trainerror1-perc.txt', train_err, fmt='%d')
	np.savetxt('testerror1-perc.txt', test_err, fmt='%d')

	train_err, test_err = ab.train(X,Y,10,T,T_Y)
	np.savetxt('trainerror1-boost.txt', train_err, fmt='%d')
	np.savetxt('testerror1-boost.txt', test_err, fmt='%d')

	#Reset classifiers
	p = ml.Perceptron()
	ab = ml.AdaBoost()

	D = np.genfromtxt('training2.txt')

	##Split into data and labels
	Y = D[:,-1]
	X = D[:,:-1]

	train_err, test_err = p.train(X,Y,T,T_Y)
	np.savetxt('trainerror2-perc.txt', train_err, fmt='%d')
	np.savetxt('testerror2-perc.txt', test_err, fmt='%d')

	train_err, test_err = ab.train(X,Y,100,T,T_Y)
	np.savetxt('trainerror2-boost.txt', train_err, fmt='%d')
	np.savetxt('testerror2-boost.txt', test_err, fmt='%d')

	#Read training/testing data
	wine_train = np.genfromtxt('wine-train.txt')
	wine_test = np.genfromtxt('wine-test.txt')

	#Create multiclass problem
	wine_labels_train = wine_train[:,0]
	wine_data_train = wine_train[:,1:]
	wine_labels_test = wine_test[:,0]
	wine_data_test = wine_test[:,1:]

	boosts = []
	replacements = []
	for c in np.unique(wine_labels_train):
		new_labels = wine_labels_train.copy()
		new_labels[wine_labels_train == c] = 1
		new_labels[wine_labels_train != c] = -1

		#Train AdaBoost
		b = ml.AdaBoost()
		b.train(wine_data_train, new_labels, 100, wine_data_test, wine_labels_test)

		replacements.append(c)

		boosts.append(b)

	#TODO: This is just unique(wine_labels_train)
	replacements = np.array(replacements)

	#Multiclass classification
	#This is quite ugly
	confidence = np.vstack([b.classify(wine_data_test)[1] for b in boosts])

	max_conf = np.argmax(confidence, axis=0)
	best_label = replacements[max_conf]
	wine_test_error = np.sum(best_label != wine_labels_test)

	print 'wine test error:' , wine_test_error

