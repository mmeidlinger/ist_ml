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

	train_err, test_err = ab.train(X,Y,10,T,T_Y)
	np.savetxt('trainerror2-boost.txt', train_err, fmt='%d')
	np.savetxt('testerror2-boost.txt', test_err, fmt='%d')
