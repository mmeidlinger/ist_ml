import numpy as np

class Perceptron:

	MAX_ITER = 100

	def train_iteration(self,X,Y):
		w_was_updated = False

		#Augment input vectors
		augment = np.ones((X.shape[0],1))
		X = np.hstack((X, augment)) #Augment input vector

		w = self.w

		for x,y in zip(X,Y):

			#Compute activation
			a = np.dot(x,w)

			#print 'classifying', x

			if y*a <= 0:
				#print 'misclassified.'
				w = w + y * x

				w_was_updated = True

				#print 'new w:', w

		self.w = w

		return w_was_updated


	def train(self, X, Y, T, T_Y):
		#w includes bias
		self.w = np.zeros((X.shape[1]+1))

		w_was_updated = True

		i = 0
		train_err = []
		test_err = []
		while w_was_updated:
			i = i + 1

			if i >= self.MAX_ITER:
				print 'number of maximally allowed iterations exceeded, stopping.'
				break

			print 'Iteration', i
			w_was_updated = self.train_iteration(X, Y)
			#Compute test error
			L = self.classify(X)
			train_error = np.sum(L != Y)
			print 'train error:', train_error
			train_err.append(train_error)

			L = self.classify(T)
			test_error = np.sum(L != T_Y)
			print 'test error:', test_error
			test_err.append(test_error)


		return np.array(train_err), np.array(test_err)

	def classify(self, X):
		augment = np.ones((X.shape[0],1))
		X = np.hstack((X, augment)) #Augment input vector
		label = np.sign(X.dot(self.w))
		label[label == 0] = -1
		return label

