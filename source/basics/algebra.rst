Algebra
=======

Polynomial long division
------------------------

:math:`\displaystyle \frac{f(x)}{g(x)}`

#. search biggest exponents in dividend
   and divisor, e.g. :math:`ax^n` and :math:`bx^m`

#. if :math:`n \geq m`:

   * add :math:`\displaystyle \frac{a}{b}x^{n-m}` to the result

   else:

   * you can't divide any further

   * add :math:`\displaystyle \frac{rest}{g(x)}` to the result

   * finished

#. subtract :math:`g(x) * \displaystyle \frac{a}{b}x^{n-m}` from :math:`f(x)`

#. repeat with result of 3.

Examples
^^^^^^^^

.. image:: ../_static/poldiv2.png

[#]_

.. image:: ../_static/poldiv1.png

[#]_

System of linear equations [#]_
-------------------------------

Solve with TI-84 Plus [#]_
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. ``2nd``, ``MATRIX``

#. navigate to ``EDIT`` with left/right arrows

#. choose the matrix to edit with the up/down arrows + ``ENTER`` or a number

#. set dimensions to :math:`X\times X+1` when you have :math:`X` variables

#. type in the coefficents of your equations
   in the last column write the RHS of your equations

#. ``2nd``, ``QUIT``

#. ``2nd``, ``MATRIX``

#. navigate to ``MATH`` with left/right arrows

#. choose ``rref(`` with ``ALPHA``, ``B`` or the up/down arrows + ``ENTER``

#. ``2nd``, ``MATRIX``

#. choose the matrix you edited with the up/down arrows + ``ENTER`` or a number

#. ``ENTER``

Solve by hand
^^^^^^^^^^^^^

#. take any equation of your system

#. isolate any of the variables in the equation

#. substitute it into the other equations

#. repeat until any variable's value is found

#. substitute back until you have the values of all variables

Examples
^^^^^^^^

.. math::
    \begin{alignedat}{7}
    3x &\ & + &\ &               2y &\ & - &\ & z &\ & = &\ & 1 \\
    2x &\ & - &\ &               2y &\ & + &\ & 4z &\ & = &\ & -2 \\
    -x &\ & + &\ & {\tfrac {1}{2}}y &\ & - &\ & z &\ & = &\ & 0 \\
    \end{alignedat}

Solution: :math:`x = 1, y = -2, z = -2`

.. [#] https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Polynomdivision_1.svg/2880px-Polynomdivision_1.svg.png

.. [#] https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Polynomdivision_3.svg/2880px-Polynomdivision_3.svg.png

.. [#] https://en.wikipedia.org/wiki/System_of_linear_equations

.. [#] https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-plus
