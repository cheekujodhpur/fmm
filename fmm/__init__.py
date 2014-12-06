"""FMM, as its name suggests is a Python library for
implementing the fast multipole method. Applications include 
all spheres where large number particle simulations
and n-body numerical solutions are needed.

See the webpage for more information and documentation:

   http://yettocome.org
"""

from __future__ import absolute_import

#Version check
import sys
if sys.version_info[0] == 2 and sys.version_info[1] < 6:
	raise ImportError("Python Version 2.6 or above is reqired for FMM.")
else:	#Python 3
	pass
	#here we can check for specific Python 3 versions if ever needed

del sys

from .core import *
