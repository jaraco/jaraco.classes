#!python

# $Id$

"""
meta.py

Some useful metaclasses.
"""

class LeafClassesMeta(type):
	"""
	A metaclass for classes that keeps track of all of them that
	aren't base classes.
	"""

	_leaf_classes = set()
	_all_classes = set()

	def _init_(cls, name, bases, attrs):
		cls._all_clasess.add(cls)
		cls._leaf_classes.add(cls)
		# remove any base classes
		cls._leaf_classes -= set(bases)
