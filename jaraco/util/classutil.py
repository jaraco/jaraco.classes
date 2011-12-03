# -*- coding: UTF-8 -*-

"""
ClassUtil.py
Provides quick routines for obtaining the class names
of an object and its parent classes.

Copyright © 2004, 2009, 2011 Jason R. Coombs
"""

from __future__ import absolute_import, unicode_literals

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'

from collections import Sequence
import itertools

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

# borrowed from http://code.activestate.com/recipes/576949-find-all-subclasses-of-a-given-class/
def itersubclasses(cls, _seen=None):
	"""
	itersubclasses(cls)

	Generator over all subclasses of a given class, in depth-first order.

	>>> bool in list(itersubclasses(int))
	True
	>>> class A(object): pass
	>>> class B(A): pass
	>>> class C(A): pass
	>>> class D(B,C): pass
	>>> class E(D): pass
	>>>
	>>> for cls in itersubclasses(A):
	...		print(cls.__name__)
	B
	D
	E
	C
	>>> # get ALL (new-style) classes currently defined
	>>> [cls.__name__ for cls in itersubclasses(object)] #doctest: +ELLIPSIS
	['type', ...'tuple', ...]
	"""

	if not isinstance(cls, type):
		raise TypeError('itersubclasses must be called with '
			'new-style classes, not %.100r' % cls)
	if _seen is None: _seen = set()
	try:
		subs = cls.__subclasses__()
	except TypeError: # fails only when cls is type
		subs = cls.__subclasses__(cls)
	for sub in subs:
		if sub in _seen:
			continue
		_seen.add(sub)
		yield sub
		for sub in itersubclasses(sub, _seen):
			yield sub


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=1)
