from scipy import optimize
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import sys
import time

class Primal:

	def __init__(self, C):
		self.C = C

	def cost_function(self, x):
		w = x[:self.d]
		ksi = x[self.d:]

		return w[:-1].dot(w[:-1]) / 2 + self.C * np.sum(ksi)

	def train(self, X,Y):

		n = X.shape[0]

		X_orig = X

		#Augment input array
		X = np.hstack((X, np.ones((X.shape[0],1))))

		d = X.shape[1]

		self.d = d


		#Create constraints
		cons = [{'type': 'ineq', 'fun': lambda x,t=t,y=y,d=d,i=i: y * (x[:d].dot(t)) - 1 + x[d+i]} for t,y,i in zip(X,Y,xrange(len(Y)))]
		cons.extend([{'type': 'ineq', 'fun': lambda x,d=d,i=i: x[d+i]} for i in xrange(n)])

		#Initial x
		x0 = np.zeros(d + n)

		result = optimize.minimize(self.cost_function, x0, method='SLSQP', constraints = cons)

		print 'minimized cost function', self.cost_function(result.x)

		self.w = result.x[:2]
		self.b = result.x[2]

		L = self.classify(X_orig)
		test_error = np.sum(L != Y)
		print 'test error:', test_error

	def classify(self, X):
		label = np.sign(X.dot(self.w) + self.b)
		label[label == 0] = -1
		return label

class Subgradient:

	def __init__(self, C):
		self.C = C

	#Sieht sehr gut aus
	def cost_function2(self, w):
		import ipdb; ipdb.set_trace()

		return w[:-1].dot(w[:-1]) / 2 + self.C * np.sum(np.maximum(0,1 - self.Y * self.X.dot(w)))

	def cost_function(self, w):

		return w[:-1].dot(w[:-1]) / 2 + self.C * np.sum(np.maximum(0,1 - self.Y * self.X.dot(w)))

	def subgradient_optimize(self,w):

		T = 10000


		n = self.X.shape[0]
		X = self.X.copy()
		Y = self.Y.copy()


		W = np.empty((T,self.X.shape[1]))
		F = np.empty(T)
		W[0,:] = w
		F[0] = self.cost_function(w)

		eta0 = 1.0

		for t in xrange(1,T):
			eta = eta0/(t)

			if t-1 % n == 0:
				randIdx = np.random.permutation(n)

				X = X[randIdx,:]
				Y = Y[randIdx]

			r = (t-1) % n

			x = self.X[r,:]
			y = self.Y[r]

			if y * x.dot(w) < 1:
				w = (1 - eta) * w + n * self.C * eta * y * x
			else:
				w = (1 - eta) * w

			W[t,:] = w
			F[t] = self.cost_function(w)

		best = np.argmin(F)

		print 'best iteration', best

		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		T = np.array(range(T))
		ax.plot(T[30:], F[30:])
		plt.show()

		return W[best,:]

	def train(self, X,Y):
		#Augment input array
		X_orig = X
		X = np.hstack((X, np.ones((X.shape[0],1))))

		self.X = X
		self.Y = Y


		n = X.shape[0]

		d = X.shape[1]

		#Initial x
		x0 = np.zeros(d)

		result = self.subgradient_optimize(x0)

		#result = optimize.minimize(self.cost_function, x0, method='SLSQP')

		print 'minimized cost function', self.cost_function(result)

		self.w = result[:2]
		self.b = result[2]

		L = self.classify(X_orig)
		test_error = np.sum(L != Y)
		print 'test error:', test_error

	def classify(self, X):
		label = np.sign(X.dot(self.w) + self.b)
		label[label == 0] = -1
		return label

class Dual:

	def __init__(self, C):
		self.C = C

	#Seems really correct
	def cost_function(self, a):
		return np.sum(np.inner(a[:,None], a[:,None]) * self.yiyjxixj) / 2 - np.sum(a)

	def train(self, X,Y):

		n = len(X)

		#Augment input array
		#X = np.hstack((X, np.ones((X.shape[0],1))))

		yiyj = np.inner(Y[:,None], Y[:,None])
		xixj = np.inner(X,X)

		yiyjxixj = yiyj*xixj

		self.yiyjxixj = yiyjxixj

		#Create constraints
		cons = [{'type': 'ineq', 'fun': lambda a,i=i: a[i]} for i in xrange(n)]
		cons.extend([{'type': 'ineq', 'fun': lambda a,i=i: self.C - a[i]} for i in xrange(n)])

		cons.append({'type': 'eq', 'fun': lambda a,Y=Y: np.sum(a*Y)})

		#Initial a
		a0 = np.zeros(n)

		result = optimize.minimize(self.cost_function, a0, method='SLSQP', constraints = cons)

		a = result.x

		self.w = np.sum(a*Y*X.T, axis=1)

		#Find non-zero a
		indices = np.nonzero(a > 1e-5)

		i = indices[0][0]

		self.b = 1 - Y[i] * X[i,:].dot(self.w)

		self.a = a

		L = self.classify(X)
		test_error = np.sum(L != Y)
		print 'test error:', test_error

	def classify(self, X):
		label = np.sign(X.dot(self.w) + self.b)
		label[label == 0] = -1
		return label

plt.close("all")
plt.ion()
N = 100
OFFSET = 10

X1 = random.standard_normal((N,2))
#X1 = np.vstack((X1, [OFFSET,OFFSET]))
X2 = random.standard_normal((N,2)) + OFFSET #Move them far away
#X2 = np.vstack((X2, [0,0]))
X = np.vstack((X1,X2))

Y1 = np.ones(X1.shape[0])
Y2 = np.ones(X2.shape[0]) * -1
Y = np.hstack((Y1,Y2))

C = 1

subgradient = Subgradient(C)
primal = Primal(C)
dual = Dual(C)

tic = time.time()
subgradient.train(X,Y)
toc = time.time()
print 'subgradient:', toc - tic
#tic = time.time()
#primal.train(X,Y)
#toc = time.time()
#print 'primal:', toc - tic
#tic = time.time()
#dual.train(X,Y)
#toc = time.time()
#print 'dual:', toc - tic

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.scatter(X1[:,0], X1[:,1], c='b')
ax1.scatter(X2[:,0], X2[:,1], c='r')

#Draw svm decision boundarie
#w1 = primal.w
#b1 = primal.b
#
#w2 = dual.w
#b2 = dual.b
#
w3 = subgradient.w
b3 = subgradient.b

p1 = np.array([0,OFFSET])
#p2p = (-w1[0]*p1 - b1) / w1[1]
#p2d = (-w2[0]*p1 - b2) / w2[1]
p2s = (-w3[0]*p1 - b3) / w3[1]
#
#ax1.plot(p1,p2p)
#ax1.plot(p1,p2d)
ax1.plot(p1,p2s)
#
plt.show()
