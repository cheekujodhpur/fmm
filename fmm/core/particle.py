"""Particles are modeled as points with properties
such as weight, charge and other elementary properties
We currently support only the explicitly mentioned ones above
"""

import numpy as np
import point

class Particle(object):
	def __init__(self,pos=None,mass=1,charge=0):
		if pos==None:
			self.pos = point.Point(pos)
		elif type(pos) == np.ndarray:
			self.pos = point.Point(pos)
		elif type(pos) == point.Point:
			self.pos = pos
		else:
			raise TypeError("An ndarray or a point object are only valid types for pos")
		self.mass = mass
		self.charge = charge

	def __str__(self):
		pstr = "[Mass:"
		pstr += str(self.mass) + "\nCharge:" + str(self.charge) + "\n"
		pstr += str(self.pos) + "]"
		return pstr

	def __repr__(self):
		return "Particle: " + str(self)
