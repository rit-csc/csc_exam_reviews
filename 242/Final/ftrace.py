# Author: David Larsen <dcl9934@cs.rit.edu>
# Date: Mon, 08 Aug 2011
# License: BSD 2-Clause License


"""
Function decorator for tracing recursive calls.

Includes the @ftrace.ftrace decorator.
"""

def ftrace( function ):
    """
    Function decorator for tracing recursive calls.

    You can ftrace a function by decorating it with @ftrace at definition, eg:

        @ftrace
        def foo():
            ...

    Note that you can also use ftrace by decorating it directly:

        foo = ftrace(foo)

    Also, if you're using certain decorators, such as the magic @classmethod
    and @staticmethod, you should have them execute _after_ ftrace, like so:

        @staticmethod
        @ftrace
        def foo(): ...

    or

        foo = staticmethod( ftrace( foo ) )
    """

    # Actions on variables that begin with `ftrace.' mean to do so at the class
    # scope. This allows state, such as call depth, to be persistent through
    # different function calls. See examples.one() for an example.

    # Print the number of stack frames we've traced through.
    ftrace.PRINT_CALLDEPTH_NUM = True

    # Indent functions that have a deeper call depth.
    ftrace.PRINT_ASCII_ART = True

    ftrace.INDENTATION_STRING = "|  "
    if not hasattr( ftrace, "calldepth" ):
        ftrace.calldepth = 0

    def decoration( *args, **kwargs ):
        function_string = function.__name__ + "( " + str( args ) + " " + str( kwargs ) +  " )"
        _print_call_depth( ftrace.calldepth, function_string )

        ftrace.calldepth += 1
        retval = function( *args, **kwargs )
        ftrace.calldepth -= 1

        _print_call_depth( ftrace.calldepth, function_string + " returns: " + str(retval) )

        return retval

    # Preserve docstrings for the function we're decorating.
    decoration.__name__ = function.__name__
    decoration.__doc__ = function.__doc__

    return decoration

def _print_call_depth( calldepth, function_string ):
    """
    Generates the function string to be printed out.
    """

    calldepth_str = "{0:{width}{base}}".format(calldepth, width=5, base='d')

    if ftrace.PRINT_CALLDEPTH_NUM:
        indentation_string = calldepth_str + " "
    else:
        indentation_string = " "

    if ftrace.PRINT_ASCII_ART:
        indentation_string += ftrace.INDENTATION_STRING * calldepth

    print( indentation_string + function_string );
