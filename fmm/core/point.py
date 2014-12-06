"""The class definition for our class 
which controls all function of a n dimesnional point
"""
import numpy as np

class Point(object):
	
	def __init__(self,vec=None):
		#checks
		if type(vec) != np.ndarray:
			if vec==None:
				vec = np.array([])
				pass
			else:
				raise TypeError("Only ndarray allowed for point declaraion.")
		else:
			pass
		self.vec = vec
		self.dim = len(self.vec)

	def __str__(self):
		return str(self.vec)
	
	def __repr__(self):
		return "Point: " + str(self)

	def __len__(self):
		return self.dim
	
	def __getitem__(self,i):
		return self.vec[i]
	
	def __setitem__(self,i,val):
		self.vec[i] = val
		return True
