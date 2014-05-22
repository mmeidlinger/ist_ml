import numpy as np
import perceptron

if __name__ == '__main__':
	p = perceptron.Perceptron()
	D = np.genfromtxt('training1.txt')
	T = np.genfromtxt('testing.txt')

	#Split into data and labels
	Y = D[:,-1]
	X = D[:,:-1]
	T_Y = T[:,-1]
	T = T[:,:-1]

	train_err, test_err = p.train(X,Y,T,T_Y)
	np.savetxt('trainerror1.txt', train_err, fmt='%d')
	np.savetxt('testerror1.txt', test_err, fmt='%d')

	p = perceptron.Perceptron()
	D = np.genfromtxt('training2.txt')

	#Split into data and labels
	Y = D[:,-1]
	X = D[:,:-1]

	train_err, test_err = p.train(X,Y,T,T_Y)
	np.savetxt('trainerror2.txt', train_err, fmt='%d')
	np.savetxt('testerror2.txt', test_err, fmt='%d')
