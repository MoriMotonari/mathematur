Binomialverteilung [#]_
=======================

Die Binomialverteilung ist die Verteilung
eines Bernoulliexperiments (siehe :ref:`bernoulli`) mit :math:`n`
Versuchen und der Erfolgswahrscheinlichkeit :math:`p` .

Der Erwartungswert:
    ist das im Durchschnitt zu erwartende Ergebnis.
    Es wird berechnet durch die Summe aller Ergebnisse,
    jeweils mit ihrer Wahrscheinlichkeit gewichtet.

    :math:`\mu = n \cdot p`

Die Varianz:
    ist die Summe aller quadrierter Differenzen
    zum Erwartungswert :math:`\mu` gewichtet
    nach der Wahrscheinlichkeit der Ergebnisse.

    :math:`\sigma^2 = n \cdot p \cdot (1-p)`

Die Standardabweichung:
    ist die Wurzel der Varianz. Sie verkörpert
    die durchschnittliche Abweichung von :math:`\mu`,
    die jedoch grössere Abstände mehr gewichtet durch
    das Quadrieren.

    :math:`\sigma = \sqrt{n \cdot p \cdot (1-p)}`

Die Wahrscheinlichkeit:
    :math:`P(a \leq X \leq b) = \sum_{k=a}^b \binom{n}{k}p^k(1-p)^{n-k}`

    TI-84 Plus [#]_:

    * ``2nd``, ``DISTR``

    * ``A`` or navigate to ``binomcdf(`` with up/down arrows

    :math:`P(a \leq X \leq b) =` ``binomcdf(n, p, b) - binomcdf(n, p, a)``


.. [#] Source: `Dr. Robert Aehle <http://www.lgr.ch/personen/lehrpersonen/?f=0&s=Aehle>`__

.. [#] https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-plus
