# -*- coding: utf-8 -*-
"""
Functions
=========

If ... Else
------------

::

    a = 200
    b = 300

    # Normal form if-statement
    if b > a:               # True
        print("b is greater than a")
    elif a == b:            # False
        print("a and b are equal")
    else:                   # False
        print("a is greater than b")
    
    # One line if else statement, with 3 conditions
    print("A") if a > b else print("=") if a == b else print("B")
    
    # No content for if statement to avoid error.
    if b > a:
        pass 


While Loops
-----------

::

    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)
    else:
    print("i is no longer less than 6")


For Loops
---------

::

    for x in range(2, 30, 3):  # from 2 to 30 by step 3 
        print(x)
    else:
    print("Finally finished!")

def
--------

::

    def <name>(arg1, arg2, ..., argN, *, **):
        <statements>
        return <expression>

lambda
------

::

    lambda [arg1[,arg2,..., argN]]: expression


classes and objects
-------------------

::

    class className(base object):
        statements
        pass
    s


list comprehension
------------------



module
------

"""