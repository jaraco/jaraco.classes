"""
Routines for obtaining the class names
of an object and its parent classes.
"""

import itertools


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


# borrowed from
# http://code.activestate.com/recipes/576949-find-all-subclasses-of-a-given-class/


def iter_subclasses(cls):
    """
    Generator over all subclasses of a given class, in depth-first order.

    >>> bool in list(iter_subclasses(int))
    True
    >>> class A(object): pass
    >>> class B(A): pass
    >>> class C(A): pass
    >>> class D(B,C): pass
    >>> class E(D): pass
    >>>
    >>> for cls in iter_subclasses(A):
    ...		print(cls.__name__)
    B
    D
    E
    C
    >>> # get ALL classes currently defined
    >>> res = [cls.__name__ for cls in iter_subclasses(object)]
    >>> 'type' in res
    True
    >>> 'tuple' in res
    True
    >>> len(res) > 100
    True
    """
    return unique_everseen(_iter_all_subclasses(cls))


def _iter_all_subclasses(cls):
    try:
        subs = cls.__subclasses__()
    except TypeError:  # fails only when cls is type
        subs = cls.__subclasses__(cls)
    for sub in subs:
        yield sub
        yield from iter_subclasses(sub)


# From Python 3.8 docs
def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in itertools.filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element
