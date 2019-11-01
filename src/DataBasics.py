# -*- coding: utf-8 -*-
"""

Data Basics
=============
::

    # Check data type
    x = 5
    print(type(x))   # <class 'int'>

    # To Delete Variable
    del x

    dir()

Numeric
^^^^^^^^^^^^^^^^
- ``int``, ``long``, ``float``, ``complex``

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
    
    import math  
    math.floor(x)   # the greatest Integral <= x
    math.ceil(x)    # the least Integral >= x
    math.exp
    math.log
    math.sqrt

Datetime 
^^^^^^^^^^^^^^^^

::

    import datetime
    d = datetime.date(2002, 12, 31)
    today = datetime.date.today()
    timedelta
    ddmmyy = d.strftime("%d/%m/%y")


String
^^^^^^^^^^^^^^^^

::

    s1 = 'abc'
    s2 = 'def'
    s1.split(',')  # split by separator
    "#.join(s1)  # join by separator
    strip(x)
    replace(x) 
    lower(x)
    upper(x)
    capitalize(x)

Boolean 
^^^^^^^^^^^^^^^^
- ``True``,``False``

::

    s ="Hello World"

    print s.isalnum()		#False
    print s.isalpha()		#False
    print s.isdigit()		#False
    print s.istitle()		#True
    print s.isupper()		#False
    print s.islower()		#False
    print s.isspace()		#False



Operators
^^^^^^^^^^^^^^^^



List
^^^^^^^^^^^^^^^^
- mutable sequences
- list comprehension: [x for x in iterable]
- l = [obj1, obj2, obj3]

::

    # Create empty list 
    l = []   

    # indexing ~ list[i]
    l = [1, 2, 3]
    print(l[0])   # 1 

    # slicing ~ list[start:end:sep]
    print(l[0:2:1]) # [1, 2]
    print(l[1::1])  # [2, 3]


Turple
^^^^^^^^^^^^^^^^
- immutable sequences
- to store collections of heterogeneous data

::

    t = (obj1, obj2, obj3)
    t = ()    # empty turple



Range 
^^^^^^^^^
- immutable sequence of numbers
- for looping a specific number of times in for loops.

::

    #range(start, stop, step)
    list(range(0, 10, 1))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    11 in range(0, 20, 2)     # False

Set
^^^^^^^^^^^^^^^^
::

    s = {obj1, obj2, obj3}
    s = set() # empty set


Dictionary
^^^^^^^^^^^^^^^^
- mapping object
- d = {key1 : value1, key2 : value2}

::

    d = {}   # empty dict

    d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict(one=1, two=2, three=3)
    d[key]  #return value
    d.keys()
    d.values()

    d.pop()  # remove item by key
    d.popitem() # remove item by values


NumPy - ndarray
^^^^^^^^^^^^^^^^^
- multidimensional, homogeneous array

::

    l = [1, 2, 3, 4, 5, 6]
    arr = np.array(l) 




Pandas - series
^^^^^^^^^^^^^^^^^
- a dimenstional array with index

::

    S1 = pd.Series() # empty series
    S2 = pd.Series([1,2,3], index = ['a','b',c'])
    S2.values 
    S2.index 

Pandas - dataframe
^^^^^^^^^^^^^^^^^^^^^
- An efficient 2D container for potentially mixed-type time series or other labeled data series.












"""
