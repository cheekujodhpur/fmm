"""The class definition for our class 
which controls all function of a n dimesnional point
"""
import numpy as np

class Point(object):
	
	def __init__(self,vec):
		#checks
		if type(vec) != np.ndarray:
			raise TypeError("Only ndarray allowed for point declaraion.")
		else:
			pass
		self.vec = vec
		self.dim = len(self.vec)
