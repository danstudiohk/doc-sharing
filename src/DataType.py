# -*- coding: utf-8 -*-
"""
Data Type
=============

Python bulit-in
---------------

Variables can store data of different types, and different types can do
different things. see `Python documentation`_.

.. _Python documentation:
   https://docs.python.org/3/library/stdtypes.html

::

    # Check data type:
    x = 5
    print(type(x))   # <class 'int'>

+ Text Type:	    ``str``
+ Mapping Type:	    ``dict``
+ Set Types:	    ``set``, ``frozenset``
+ Boolean Type:	    ``bool``
+ Binary Types:	    ``bytes``, ``bytearray``, ``memoryview``


Numeric: ``int``, ``float``, ``complex``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    x + y           # sum of x and y
    x - y           # difference of x and y
    x * y           # product of x and y
    x / y           # quotient of x and y
    x // y          # floored quotient of x and y
    x % y           # remainder of x / y
    abs(x)          # absolute value or magnitude of x
    int(x)          # x converted to integer
    float(x)        # x converted to floating point
    divmod(x,y)     # the pair (x // y, x % y)
    x ** y          # x to the power y; or pow(x, y)
    round(x[, n])   # round if >5 to greatest Integral
    math.floor(x)   # the greatest Integral <= x
    math.ceil(x)    # the least Integral >= x

Sequence: ``list``, ``tuple``, ``range``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    x in s                  # True if an item of s is equal to x, else False
    x not in s	            # False if an item of s is equal to x, else True
    s + t                   # the concatenation of s and t
    s * n                   # equivalent to adding s to itself n times
    s[i]                    # ith item of s, origin 0
    s[i:j]                  # slice of s from i to j
    s[i:j:k]                # slice of s from i to j with step k
    len(s)                  # length of s
    min(s)                  # smallest item of s
    max(s)                  # largest item of s
    s.index(x[, i[, j]])    # index of the first occurrence of x in s (at or after index i and before index j)
    s.count(x)              # total number of occurrences of x in s

Set
^^^^^^^^

Mapping: ``Dictionary``
^^^^^^^^^^^^^^^^^^^^^^^

Boolean
^^^^^^^^^^^^




NumPy
-----

:: 

    import numpy as np

ndarray 
^^^^^^^
``ndim`` ``shape`` ``dtype``

>>> list = [56, 8, 19, 14, 6, 71]
>>> arr = np.array(list) 
>>> print(arr.ndim) # number of dimensions
>>> print(arr.shape) # m*n
>>> print(arr.dtype) # data type

``zeros()``
``empty()``
``arange()``
``astype()``

>>> arr64 = arr.astype(np.int64)

``[]`` for slicing

>>> arr = np.arange(10)
>>> print(arr[0])
>>> print(arr[0:5])

``T`` for transposing 2D arrray

>>> 1d_arr = np.arange(10)
>>> 2d_arr = 1d_arr.reshape((2, 5))
>>> print(2d_arr.T)

``where()``

>>> arr = np.arange(10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.where(arr < 5, arr, 10*arr) #array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])


``sort()``

>>> arr = np.array([56, 8, 19, 14, 6, 71])
>>> print(arr.sort())

``random()``

>>> normal_samples = np.random.normal(size = 10)
>>> uniform_samples = np.random.uniform(size = 10)

Pandas
------

::

    import pandas as pd

Series
^^^^^^^^^^^^^^^^

DataFrame
^^^^^^^^^^^^^^^^
An efficient 2D container for potentially mixed-type time series or other
labeled data series.




"""
