
import types

def makeSequence(el):
    if type( el ) in ( types.TupleType, types.ListType ):
        return el
    return [el,]

def flatten( l ):
    if filter( lambda x: type(x) in ( types.ListType, types.TupleType) , l ):
        result = []
        map( lambda el, li=result: li.extend(el), map( flatten, map( makeSequence, l ) ) )
        return tuple( result )
    else: return l

def allBases( c ):
    return flatten( tuple(map( allBases, c.__bases__ )) + c.__bases__ )

def allClasses( c ):
    return (c,)+allBases(c)
