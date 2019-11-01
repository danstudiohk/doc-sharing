# -*- coding: utf-8 -*-
"""
Data Visualization
===================

>>> import matplotlib.pyplot as plt
>>> import seaborn as sns

.. image:: img/Anatomy_of_Matplotlib_Figure.png

Line Plot
----------

::
    
    x = []
    y = []
    plt.style.use(ggplot)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel = 'X', 
            ylabel = 'Y',
            title = 'Line Plot Y against X')
    ax.grid()
    plt.show()

"""