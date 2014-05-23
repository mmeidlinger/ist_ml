import numpy as np
import ml

if __name__ == '__main__':

	#Read artificial1 training/testing data
	A = np.genfromtxt('artificial1-train.txt')
	X_1 = A[:,:-1]
	Y_1 = A[:,-1]
	A = np.genfromtxt('artificial1-test.txt')
	X_2 = A[:,:-1]
	Y_2 = A[:,-1]

	#Perceptron
	perc = ml.Perceptron()
	E_1, E_2 = perc.train(X_1, Y_1, X_2, Y_2)
	np.savetxt('artificial1-trainerror-perc.txt', E_1, fmt='%d')
	np.savetxt('artificial1-testerror-perc.txt', E_2, fmt='%d')

	#AdaBoost
	boost = ml.AdaBoost()
	E_1, E_2 = boost.train(X_1, Y_1, 100, X_2, Y_2)
	np.savetxt('artificial1-trainerror-boost.txt', E_1, fmt='%d')
	np.savetxt('artificial1-testerror-boost.txt', E_2, fmt='%d')

	#Read artificial2 dataset
	A = np.genfromtxt('artificial2-train.txt')
	X_1 = A[:,:-1]
	Y_1 = A[:,-1]
    
	#Perceptron
	perc = ml.Perceptron()
	E_1, E_2 = perc.train(X_1, Y_1, X_2, Y_2)
	np.savetxt('artificial2-trainerror-perc.txt', E_1, fmt='%d')
	np.savetxt('artificial2-testerror-perc.txt', E_2, fmt='%d')

	#AdaBoost
	boost = ml.AdaBoost()
	E_1, E_2 = boost.train(X_1, Y_1, 100, X_2, Y_2)
	np.savetxt('artificial2-trainerror-boost.txt', E_1, fmt='%d')
	np.savetxt('artificial2-testerror-boost.txt', E_2, fmt='%d')

	#Wine dataset
	A = np.genfromtxt('wine-train.txt')
	X_1 = A[:,1:]
	Y_1 = A[:,0]
	A = np.genfromtxt('wine-test.txt')
	X_2 = A[:,1:]
	Y_2 = A[:,0]

	#Create multiclass problem
	boosts = []
	replacements = []
	for c in np.unique(Y_1):
		new_labels = Y_1.copy()
		new_labels[Y_1 == c] = 1
		new_labels[Y_1 != c] = -1

		#Train AdaBoost
		b = ml.AdaBoost()
		import ipdb; ipdb.set_trace()
		b.train(X_1, new_labels, 100, X_2, Y_2)

		replacements.append(c)

		boosts.append(b)

	#TODO: This is just unique(wine_labels_train)
	replacements = np.array(replacements)

	#Multiclass classification
	#This is quite ugly
	confidence = np.vstack([b.classify(X_2)[1] for b in boosts])

	max_conf = np.argmax(confidence, axis=0)
	best_label = replacements[max_conf]
	wine_test_error = np.sum(best_label != Y_2)

	print 'wine test error:' , wine_test_error

