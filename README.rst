pyquation
=========

A DSL for equations in Python.

Examples::

    >>> from pyquation import variable as x
    
    >>> f = 2*x + 1
    >>> f(1)
    3
    >>> f(2)
    5
    >>> f(3)
    7
