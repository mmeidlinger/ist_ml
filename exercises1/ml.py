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

class WeakLearner:

	column = None
	value = None

	def classify(self, X):
		labels = 2*(X[:,self.column] == self.value) - 1
		return labels

class AdaBoost:

	#T is number of iterations
	def train(self, X, Y, T, X2,Y2):

		n = X.shape[0]
		m = X.shape[1]

		#Create weak learners
		H = []
		for c in xrange(m):
			for v in np.unique(X[:,c]):
				h = WeakLearner()
				h.column = c
				h.value = v
				H.append(h)

		#Make sure we don't run out of weak classifiers
		T = min(T,len(H))

		#Initial weights	
		w = np.ones(n) / n

		#Ensemble
		F = []

		#ensemble weight
		alpha_t = np.zeros(T)
		
		for t in xrange(T):

			#Compute errors of weak classifiers
			E_h = np.zeros(len(H))
			for i in xrange(len(H)):
				E_h[i] = np.sum(w*(H[i].classify(X) != Y))

			#Find best weak classifier
			#TODO: break ties?
			h_best = np.argmin(E_h)
			e_h = E_h[h_best]

			#Classifier importance
			alpha = np.log((1-e_h)/e_h)/ 2 

			#Add to ensemble
			ht = H[h_best]
			F.append(ht)
			alpha_t[t] = alpha

			#Re-weigh training examples
			labels = ht.classify(X)
			correct = labels == Y
			incorrect = labels != Y

			w[incorrect] = w[incorrect] * (np.e**alpha) 
			w[correct] = w[correct] * (np.e**-alpha) 

			#Normalize
			w = w / sum(w)

		self.alpha_t = alpha_t
		self.F = F

		#Compute train_error
		L = self.classify(X)
		train_error = np.sum(L != Y)
		print 'train error:', train_error
		train_err.append(train_error)

		#Compute test_error
		L = self.classify(X2)
		test_error = np.sum(L != Y2)
		print 'test error:', test_error
		test_err.append(test_error)

		return np.array(train_err), np.array(test_err)

	def classify(self, X):
		augment = np.ones((X.shape[0],1))
		X = np.hstack((X, augment)) #Augment input vector
		label = np.sign(X.dot(self.w))
		label[label == 0] = -1
		return label

class WeakLearner:

	column = None
	threshold = None
	only_greater = False

	def classify(self, X):
		if self.only_greater:
			labels = X[:,self.column] > self.value
		else:
			labels = X[:,self.column] <= self.value
		labels = 2 * labels - 1
		return labels

class AdaBoost:

	#T is number of iterations
	def train(self, X, Y, T, X2,Y2):
		train_err = []
		test_err = []

		n = X.shape[0]
		m = X.shape[1]

		#Create weak learners
		H = []
		for c in xrange(m):
			v = np.mean(X[:,c])

			h1 = WeakLearner()
			h1.column = c
			h1.value = v
			h1.only_greater = True

			h2 = WeakLearner()
			h2.column = c
			h2.value = v
			h2.only_greater = False

			H.append(h1)
			H.append(h2)

		#Make sure we don't run out of weak classifiers
		T = min(T,len(H))

		#Initial weights	
		w = np.ones(n) / n

		#Ensemble
		self.F = []

		#ensemble weight
		self.alpha_t = np.zeros(T)
		
		for t in xrange(T):

			#Compute errors of weak classifiers
			E_h = np.zeros(len(H))
			for i in xrange(len(H)):
				E_h[i] = np.sum(w*(H[i].classify(X) != Y))

			#Find best weak classifier
			#TODO: break ties?
			h_best = np.argmin(E_h)
			e_h = E_h[h_best]

			#Classifier importance
			alpha = np.log((1-e_h)/e_h)/ 2 

			#Add to ensemble
			ht = H[h_best]
			self.F.append(ht)
			self.alpha_t[t] = alpha

			#Re-weigh training examples
			labels = ht.classify(X)
			correct = labels == Y
			incorrect = labels != Y

			w[incorrect] = w[incorrect] * (np.e**alpha) 
			w[correct] = w[correct] * (np.e**-alpha) 

			#Normalize
			w = w / sum(w)

			#Compute train_error
			L = self.classify(X)
			train_error = np.sum(L != Y)
			print 'train error:', train_error
			train_err.append(train_error)

			#Compute test_error
			L = self.classify(X2)
			test_error = np.sum(L != Y2)
			print 'test error:', test_error
			test_err.append(test_error)

		return np.array(train_err), np.array(test_err)

	def classify(self, X):

		response = np.zeros(X.shape[0])
		for f in xrange(len(self.F)):
			response = response + self.alpha_t[f] * self.F[f].classify(X)

		labels = np.sign(response)
		labels[labels==0] = -1

		return labels


	def classify(self, X):

		response = np.zeros(X.shape[0])
		for f in xrange(len(self.F)):
			response = response + self.alpha_t[f] * self.F[f].classify(X)

		labels = np.sign(response)
		labels[labels==0] = -1

		return labels, response

