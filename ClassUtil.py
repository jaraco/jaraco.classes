__doc__ = """
ClassUtil.py provides quick routines for obtaining the class names
of an object and its parent classes
"""

import types

# makeSequence puts any non-sequence objects into a singleton list
def makeSequence(el):
    if type( el ) in ( types.TupleType, types.ListType ):
        return el
    return [el]

# flatten takes a list of lists and returns a single list with each element from the
#  sublists.  For example,
#  flatten( [a,b,[c,d,[e,f],g],h] ) == [a,b,c,d,e,f,g,h]
def flatten( l ):
    if filter( lambda x: type(x) in ( types.ListType, types.TupleType) , l ):
        result = []
        map( lambda el, li=result: li.extend(el), map( flatten, map( makeSequence, l ) ) )
        return tuple( result )
    else: return l

# all bases returns a tuple of all base classes the class c has as a parent.
def allBases( c ):
    return flatten( tuple(map( allBases, c.__bases__ )) + c.__bases__ )

# all classes returns a tuple of all classes to which c belongs.
def allClasses( c ):
    return (c,)+allBases(c)
