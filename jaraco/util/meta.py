"""
meta.py

Some useful metaclasses.
"""

from __future__ import unicode_literals

class LeafClassesMeta(type):
	"""
	A metaclass for classes that keeps track of all of them that
	aren't base classes.
	"""

	_leaf_classes = set()

	def __init__(cls, name, bases, attrs):
		if not hasattr(cls, '_leaf_classes'):
			cls._leaf_classes = set()
		leaf_classes = getattr(cls, '_leaf_classes')
		leaf_classes.add(cls)
		# remove any base classes
		leaf_classes -= set(bases)
