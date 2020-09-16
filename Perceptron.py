from math import e

class Perseptron:
	list = [1,1,0,1,1,0,0,0]
	w1 = 0.9
	w2 = 0.2

	def __init__(self, x1, x2, y):
		self.x1 = x1
		self.x2 = x2
		self.y = y
		
		#table_truth = [1,1,-1, 1,1,-1,-1,-1]
		#function = x1 and x2
		#learning_order_pointer = 0


	def function(self, func):
		func = (self.x1 or self.x2)
		print(bool(func))


	def sigmoidActivation(self):
		w1 = 0.9
		w2 = 0.2
		sigma = (w1* self.x1+ w2*self.x2)
		print (sigma)
		Perseptron(1,1,1).outputLayer(sigma) #=1.1



	def outputLayer(self, sigma):
		a1 = 1/(1+e**(-sigma))
		print(a1)
		return a1

	def costFunction(self, a1):
		totalCost = 0.5*((self.y-a1)**2)
		print ("a1 = ", a1)
		print(totalCost)
		return totalCost

	def errorOutput(self):
		error = (self.y - a1) * a1 * (1 - a1)
		return error



first = Perseptron(1, 1, 1).function(True)
second = Perseptron(1, 0 , 1).function(True)
thrid = Perseptron(0, 1, 1).function(True)
fourth = Perseptron(0, 0, 0).function(True)


one = Perseptron(1,1,1).sigmoidActivation()
two = Perseptron(1,1,1).costFunction(a1)
#one = Perseptron(1,1,1).outputLayer(Perseptron(1,1,1).sigmoidActivation())
#two = Perseptron(1,1,1).costFunction(Perseptron(1,1,1).outputLayer(sigma))






