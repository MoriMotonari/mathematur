Wahrscheinlichkeitsverteilung [#]_
==================================

Die Wahrscheinlichkeitsverteilung ist die Verteilung
der Ergebnisse eines Zufallsexperiments und ihren
Wahrscheinlichkeiten. Eine Verteilung funktioniert
nur wenn die Ergebnisse sortierbar sind. Z.B. die
Augen eines Würfels :math:`\{1, 2, 3, 4, 5, 6\}`
sind sortiert.

Der Erwartungswert:
    ist das im Durchschnitt zu erwartende Ergebnis.
    Es wird berechnet durch die Summe aller Ergebnisse,
    jeweils mit ihrer Wahrscheinlichkeit gewichtet.

    :math:`\mu = \sum_k k \cdot P(X = k)`

Die Varianz:
    ist die Summe aller quadrierter Differenzen
    zum Erwartungswert :math:`\mu` gewichtet
    nach der Wahrscheinlichkeit der Ergebnisse.

    :math:`\sigma^2 = \sum_k (k-\mu)^2 \cdot P(X = k)`

Die Standardabweichung:
    ist die Wurzel der Varianz. Sie verkörpert
    die durchschnittliche Abweichung von :math:`\mu`,
    die jedoch grössere Abstände mehr gewichtet durch
    das Quadrieren.

    :math:`\sigma = \sqrt{\sum_k (k-\mu)^2 \cdot P(X = k)}`

.. [#] Source: `Dr. Robert Aehle <http://www.lgr.ch/personen/lehrpersonen/?f=0&s=Aehle>`__
