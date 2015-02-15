"""
Routines for obtaining the class names
of an object and its parent classes.
"""

from __future__ import absolute_import, unicode_literals

import warnings

import jaraco.itertools

def ensure_sequence(el):
	"""
	*Deprecated*

	if item is not a sequence, return the item as a singleton in a list

	>>> ensure_sequence(3)
	[3]
	>>> ensure_sequence([3,4])
	[3, 4]
	"""
	msg = "Deprecated. Use jaraco.itertools.always_iterable"
	warnings.warn(msg, DeprecationWarning)
	return list(jaraco.itertools.always_iterable(el))

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
	>>> res = [cls.__name__ for cls in itersubclasses(object)]
	>>> 'type' in res
	True
	>>> 'tuple' in res
	True
	>>> len(res) > 100
	True
	"""

	if not isinstance(cls, type):
		raise TypeError('itersubclasses must be called with '
			'new-style classes, not %.100r' % cls)
	if _seen is None: _seen = set()
	try:
		subs = cls.__subclasses__()
	except TypeError:  # fails only when cls is type
		subs = cls.__subclasses__(cls)
	for sub in subs:
		if sub in _seen:
			continue
		_seen.add(sub)
		yield sub
		for sub in itersubclasses(sub, _seen):
			yield sub
