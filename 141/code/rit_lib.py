"""
$Id: rit_lib.py,v 3.2 2015/09/04 13:20:59 jeh Exp $

An alternative to the namedtuple construct in the Python collections module.
This module creates classes with a fixed set of slots

For historical reasons, this library is known as the "quick class" library.
There are however two ways to build a quick class in this framework:
1. Inherit the struct class defined here.
2. Create a class by calling the quickClass function.

The only differences between using a quick class and a normal class
definition are as follows.

1. A default constructor is provided that takes positional or keyword
   arguments to initialize the slots declared.
2. The methods __str__, __repr__, __eq__, and __ne__ are predefined.
3. The types of the class's slots (attributes) can optionally be defined
   (via the _slots class variable in a class declaration or additional
   arguments to the quickClass function) and checked at run time.

The differences between a class created through this package and one created
through collections.namedtuple are as follows.

1. Objects created via this library are not iterable.
2. The attributes in objects created by this library are writable.

NOTE: To disable type checking (for speed), add the following method
after and outside your class's definition. Substitute your class's name
for the name YOURCLASS

    YOURCLASS.__setattr__ = object.__setattr__

"""

# Reasons for doing this:

# Less code to define a class and no need for a maker function means it
# is far less error prone.

# Type checking makes debugging easier since execution halts at the
# source of the problem (the assignment violation) versus later on (when
# accessed/used as an unexpected type).

# Built in "to string" representation (__str__ method) also makes
# debugging easier.

# As with manually declaring classes with a __slots__ class variable,
# objects enforce their predefined slot attributes and those attributes
# are still mutable (unlike namedtuples).

REV = "$Revision: 3.2 $"

from inspect import isclass
from sys import stderr
from collections import OrderedDict

##########################################################################
#                                                                        #
# Abstract Base Class Section                                            #
#                                                                        #
##########################################################################

import abc # abstract base class library

def makeAbstractClass( className ):
    """ Create and return an abstract class.
        This is used for the run-time type checking that struct provides.

        For more details on abstract base classes, see ABCMeta in package abc.

        When this function returns, the created abstract class
        has as yet no 'concrete' classes that conform to it.
        Here is an example of how you use it:
            Master = makeAbstractClass( "Master" )
            ... Create classes C1, C2, and C3 using struct or quickClass.
            ... On the other hand, any of them could be previously defined
                types, too.
            Master.addClasses( C1, C2, C3 )
            C1, C2, and C3 are now subclasses of Master.
            This means that if a quick class says that a slot must be
            of type Master, then an instance of C1, C2, or C2 will work.
    """
    class AbstractClass( metaclass=abc.ABCMeta ):
        @classmethod
        def addClasses( self, *classes ):
            """ Establish the classes provided as arguments to this
                function as 'concrete' classes that conform to this
                abstract class.
            """
            for cls in classes:
                self.register( cls )
    AbstractClass.__name__ = className
    return AbstractClass

##########################################################################
#                                                                        #
# Definition of struct class -- does all the setup and checking      #
#                                                                        #
##########################################################################

NoneType = type( None )

class struct( object ):
    """ The base class for all classes created using this framework.
        Note that the methods contained herein apply to classes inheriting
        struct; it is not expected that classes declared as inheriting
        struct would define their own methods, much less redefine
        these.
        That being said, since struct's subclasses will not explicitly
        contain their own constructors, programmers of those subclasses must
        be familiar with the API for the constructor defined here.

        struct expects its subclasses to have one of the following
        two class variables defined:

        If __slots__ is defined, it is a tuple of names of class slots,
        or attributes, represented as strings. These names are assumed
        to be exactly the set of slots to be initialized, set, and
        otherwise accessed. (Python enforces this.) However, the slots
        can have any value; there is no type checking.
        Example:
            class Student( struct ):
                __slots__ = ( "age", "gpa" )

        If _slots is defined, it is a tuple of tuples. The inner
        tuples are all of length 2. The first value of each such
        pair is either a type or a tuple of types. The second
        value is the name of the slot, as in the __slots__ case above.
        It works just like the first case with __slots__, but now
        the values that may be assigned to the slots must be of
        (one of) the type(s) associated with it.
        Example:
            class Student( struct ):
                _slots = ( (int,"age"), ((str,float),"gpa") )

        The one exception is that, instead of a type one may use the string
        name of the class being built. This is the way one refers to the
        type one is building for structurally recursive types.
        Note that mutually recursive types are not (yet) supported.

        The class returned can be constructed using the provided name and
        either positional or keyword arguments. See the __init__ method
        for struct
    """

    # Initially the new class's slots may have some of its types
    # specified as strings. These need to be converted to real types.
    # The class-level boolean variable _typesScanned
    # indicates whether this class's type list has been scanned yet
    # for str's. It's done in the instance constructor __init__.
    #
    _typesScanned = False

    def __init__( self, *args, **kwargs ):
        """ Initialize a new instance of a subclass of struct. The
            constructor call argument list should contain a value for
            each attribute of the class, presented either in the same
            order as the _slots declaration (args), or with keyword names
            that match the slot names (kwargs). These two approaches may
            not be mixed; that is either args or kwargs must be empty.

            args: a sequence of values for each slot declared in the subclass
            kwargs: a dictionary of values for each slot declared in
                    the subclass. The keys in the dictionary match the
                    names of the slots.
        """
        # Save the id and name of the subclass being instantiated.
        thisClass = self.__class__
        className = thisClass.__name__
        if ( thisClass == struct ):
            raise TypeError( "struct itself may not be instantiated." )

        if not thisClass._typesScanned: # Do this upon FIRST instance creation.
            # If __slots__ but no _slots, convert using type 'object'.
            # or look for old, deprecated _types variable.
            #
            if "__slots__" in dir( thisClass ):
                if "_slots" in dir( thisClass ):
                    raise TypeError( "struct subclasses may not have " + \
                                     "a '_slots' attribute declared if\n" + \
                                     " the standard '__slots__' attribute " + \
                                     "is present." )
                slots = thisClass.__slots__
                if not ( isinstance( slots, tuple ) or \
                         isinstance( slots, list ) ):
                    slots = ( slots, )

                newSlots = []
                if "_types" in dir( thisClass ):
                    stderr.write( "struct warning: '_types' " + \
                                  "variable is deprecated. (class " + \
                                  className + ").\n" )
                    types = thisClass._types
                    if not ( isinstance( types, tuple ) or \
                             isinstance( types, list ) ):
                        types = ( types, )
                    if len( types ) != len( slots ):
                        raise TypeError(
                               "No. of slots differs from no. of types" )
                    for i in range( len( slots ) ):
                        newSlots.append( ( types[ i ], slots[ i ] ) )
                else:
                    for attrName in thisClass.__slots__:
                        newSlots.append( ( object, attrName ) )
                thisClass._slots = tuple( newSlots )

            if "_slots" not in dir( thisClass ):
                raise TypeError( "struct subclasses must have " + \
                                 "either a '_slots' or '__slots__' " + \
                                 "attribute declared." )

            # Do error checking and convert the _slots variable
            # to a dictionary mapping each variable name to a set
            # of types.
            #
            _normalizeSlotsConstruction( thisClass )

            # The above code is only exectuted the first time an object is
            # created from the new class.
            thisClass._typesScanned = True

        if len( kwargs ) != 0:
            # Make a copy of the slot dictionary so that it is easy to
            # check if each slot is given a value exactly once.
            #
            slots = thisClass._slots.copy()

            if len( args ) != 0:
                raise TypeError( "NamedTuples cannot be initialized with " +\
                                 "a combination of regular and " +\
                                 "keyword arguments" )
            else:
                for key in kwargs:
                    if key not in thisClass._slots:
                        raise AttributeError( "'" + className + "' object " +\
                                              "has no attribute named '" +\
                                              key + "'" )
                    else:
                        attrValue = kwargs[ key ]
                        setattr( self, key, attrValue )
                        del slots[ key ]
                if len( slots ) != 0:
                    raise TypeError( "Constructor call for " + className +\
                                     " did not get initialization values " +\
                                     "for " + str( slots.keys() ) )
        else:
            if len( args ) != len( thisClass._slots ):
                raise TypeError( "Constructor call for " + className +\
                                 " expected " + \
                                 str( len( thisClass._slots ) ) + \
                                 " arguments but got " + str( len( args ) ) )
            else:
                i = 0
                for key in thisClass._slots:
                    setattr( self, key, args[ i ] )
                    i += 1

    def __eq__( self, other ):
        """ (DO NOT call this function directly; access it via the '=='
             operator.)
            Answer False if other is not the same type as self, or if
            the values of the slots in the two objects are not all equal
            (through the use of the '!=' operator, i.e., __ne__).
            Answer True otherwise.
            Precondition: the object must not contain circular references.
                If it does, this method must be redefined in the subclass.
        """
        visited = set() # for pairs of ids already seen
        return struct._equal( self, other, visited )

    @staticmethod
    def _equal( o0, o1, visited ):
        id0 = id( o0 )
        id1 = id( o1 )
        if id0 == id1: return True
        if type( o0 ) != type( o1 ): return False
        if not isinstance( o0, struct ): return o0 == o1
        visited.add( ( id0, id1 ) )
        for slotName in o1.__class__._slots: # keys of dictionary
            s0 = getattr( o0, slotName )
            sid0 = id( s0 )
            s1 = getattr( o1, slotName )
            sid1 = id( s1 )
            if ( sid0, sid1 ) not in visited:
                visited.add( ( sid0, sid1 ) )
                if not struct._equal( s0, s1, visited ):
                    return False
        return True

    def __ne__( self, other ):
        """ (DO NOT call this function directly; access it via the '!='
             operator.)
            Answer not ( self == other ), i.e., not self.__eq__( other ).
        """
        return not ( self == other )

    def __str__( self ):
        """ (DO NOT call this function directly; access it via the str
             global function.)
            Return a string representation of the value of this object
            using its class's name followed by a listing the values of
            all of its slots.
            If the object contains multiple references involving only
            structs, the returned string will be degraded to avoid
            potential infinite recursion.
        """
        visited = set()
        return self._str_rep( set(), ": " )

    def __repr__( self ):
        """ (DO NOT call this function directly; access it via the repr
             global function.)
            Return a string that, if evaluated, would re-create this object.
            If the object contains multiple references involving only
            structs, the returned string will be degraded to avoid
            potential infinite recursion.
        """
        return self._str_rep( set(), "=" )

    def _str_rep( self, visited, sep ):
        """ Called by both __str__ and __repr__. Only difference is
            the characters separating each slot name from its value.
        """
        thisClass = self.__class__
        className = thisClass.__name__
        slots = tuple( thisClass._slots.keys() )
        if len( slots ) != 0:
            result = className + "( "
            lastSlot = slots[ -1 ]
            for slot in slots:
                obj = getattr( self, slot )
                objID = id( obj )
                if objID not in visited:
                    if isinstance( obj, struct ):
                        slotStr = obj._str_rep( visited | set([id(self)]), sep )
                    else:
                        slotStr = repr( obj )
                    result += slot + sep + slotStr
                else:
                    result += slot + sep + "..."
                if slot != lastSlot:
                    result += ", "
            result += " )"
        else:
            result = className + "()"
        return result

    def __setattr__( self, name, value ):
        """ This is a private function. Do NOT directly call it.
            It checks attribute (slot) references for type validity.
        """
        thisClass = self.__class__
        slots = thisClass._slots
        if name not in slots:
            raise AttributeError( repr( thisClass.__name__ ) + \
                         " object has no attribute " + repr( name ) )
        paramTypes = slots[ name ]
        # Even though paramTypes is a set we must iterate due to
        # need to check for subclass with isinstance().
        #
        ok = False
        for paramType in paramTypes:
            # print( "Checking if", value, "is a", paramType )
            if isinstance( value, paramType ):
                ok = True
                break
        if ok:
            object.__setattr__( self, name, value )
        else:
            raise TypeError( "Type of " + name + \
                             " may not be " + type( value ) .__name__ )

def _normalizeSlotsConstruction( cls ):
    """ The form of the _slots variable should be either
        TSet, str
        or
        ( (TSet,str), (TSet,str), ... )
        where TSet = T or ( T, T, ... )
        and
        T = str or type

        This function checks everything and converts the _slots
        variable into a dictionary.
    """
    # Error check: Make sure that _slots is a tuple.
    if type( cls._slots ) != tuple:
        raise TypeError( "_slots attribute must be a tuple" )

    slots = cls._slots

    # Fix: If only one slot, convert single entry to a tuple containing it.
    if len( slots ) == 2 and type( slots[ 1 ] ) == str: #singleton case
        slots = ( slots, )

    # Error check: Make sure that all the structures within are legal.
    for tspec in slots:
        if type( tspec ) != tuple:
            raise TypeError( "Improper _slots attribute" )
        if type( tspec[ 1 ] ) != str or ( not isclass( tspec[ 0 ] ) and \
                                          type( tspec[ 0 ] ) != str and \
                                          type( tspec[ 0 ] ) != tuple ):
            raise TypeError( "Improper _slots attribute" )
        if type( tspec[ 0 ] ) == tuple:
            for t in tspec[ 0 ]:
                if not isclass( t ) and type( t ) != str:
                    raise TypeError( "Improper type spec in _slots attribute" )

    # Create the dictionary, performing more validity checks along
    # the way.
    #
    slotd = OrderedDict()
    for tspec in slots:
        # Fix the type part of the pair.
        if isclass( tspec[ 0 ] ): # type to tuple containing type
            types = set( ( tspec[ 0 ], ) )
        elif type( tspec[ 0 ] ) == str: # string name of type to type
            if tspec[ 0 ] != cls.__name__:
                raise TypeError( "The type string name given was '" + \
                                 tspec[ 0 ] + "'. Only '" + \
                                 cls.__name__ + "' is allowed here." )
            types = set( ( cls, ) )
        else: # Must be a tuple of types due to previous checks
            types = set()
            for t in tspec[ 0 ]:
                if isclass( t ):
                    types.add( t )
                elif type( t ) == str:
                    if t != cls.__name__:
                        raise TypeError( "The type string name given was '" + \
                                         t + "'. Only '" + \
                                         cls.__name__ + "' is allowed here." )
                    types.add( cls )
                else:
                    raise TypeError( str( t ) + " is not a type" )
        # Check the variable name part of the pair
        if type( tspec[ 1 ] ) != str:
            raise TypeError( str( tspec[ 1 ] ) + " is not a string" )
        slotd[ tspec[ 1 ] ] = types

    # Put it back in the _slots class variable
    cls._slots = slotd

##########################################################################
#                                                                        #
# quickClass function -- creates an struct subclass                  #
#                                                                        #
##########################################################################


def quickClass( name, *slotDecls ):
    """ Return a new class that has the provided name and slots (attributes).
    
        (This is an alternative to the explicit class declaration using the
         base class struct.)

        slotDecls: a sequence of slot declarations
        Each slot declaration provided is a 2-tuple, with the slot's type
        or tuple of types first and the slot's name second.
        The one exception is that, instead of a type one may use the string
        name of the class being built. This is the way one refers to the
        type one is building for structurally recursive types.

        Note that mutually recursive types are not (yet) supported.

        The class returned can be constructed using the provided name and
        either positional or keyword arguments. See the __init__ method
        for struct
    """
    return type( name, ( struct, ), { '_slots': slotDecls } )
