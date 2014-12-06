"""The class definition for our class 
which controls all function of a n dimesnional point
"""
import numpy as np

class Point:
	
	def __init__(self,vec):
		#checks
		if type(vec) != np.ndarray:
			raise TypeError("Only ndarray allowed for point declaraion.")
		else:
			pass
		self.vec = vec
		self.dim = len(self.vec)

	def __add__(self,b):
		if self.dim != b.dim:
			raise TypeError("Two points being added must have same dimension.")
		else:
			pass
		nvec = self.vec+b.vec
		return Point(nvec)

	def __str__(self):
		return str(self.vec)
	
	def __repr__(self):
		return str(self)

	def __len__(self):
		return self.dim
	
	def __getitem__(self,i):
		return self.vec[i]
	
	def __setitem__(self,i,val):
		self.vec[i] = val
		return True
