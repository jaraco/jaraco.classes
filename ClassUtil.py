# -*- coding: UTF-8 -*-

""" ClassUtil.py
	Provides quick routines for obtaining the class names
of an object and its parent classes.
	
Copyright © 2004 Sandia National Laboratories  
"""

__author__ = 'Jason R. Coombs <jaraco@sandia.gov>'
__version__ = '$Rev: 3 $'[6:-2]
__svnauthor__ = '$Author: Jaraco $'[9:-2]
__date__ = '$Date: 04-06-23 12:18 $'[7:-2]

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
