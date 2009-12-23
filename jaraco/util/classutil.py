# -*- coding: UTF-8 -*-

"""
ClassUtil.py
Provides quick routines for obtaining the class names
of an object and its parent classes.

Copyright © 2004, 2009 Jason R. Coombs  
"""

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'
__version__ = '$Rev$'[6:-2]
__svnauthor__ = '$Author$'[9:-2]
__date__ = '$Date$'[7:-2]

import types
from collections import Sequence

from jaraco.util.iter_ import flatten

def ensure_sequence(el):
	"""
	if item is not a sequence, return the item as a singleton in a list
	>>> ensure_sequence(3)
	[3]
	>>> ensure_sequence([3,4])
	[3, 4]
	"""
	if isinstance(el, Sequence):
		return el
	return [el]

def all_bases(c):
	"""
	return a tuple of all base classes the class c has as a parent.
	>>> object in all_bases(list)
	True
	"""
	return c.mro()[1:]

def all_classes(c):
	"""
	return a tuple of all classes to which c belongs
	>>> list in all_classes(list)
	True
	"""
	return c.mro()
