Kombinatorik [#]_
=================

Permutation
-----------

Die Anzahl Möglichkeiten :math:`n` Objekte
zu sortieren.

.. math::
    n!

**Beispiel:** Sandro hat eine Farbstiftschachtel
mit 10 verschiedenfarbigen Stiften. In wie vielen
verschiedenen Reihenfolgen kann er sie ordnen?

:math:`10! = 3628800`

.. warning::
    Eine Permutation ist eine Variation ohne Wiederholung mit :math:`n = k`.
    Beachte :math:`(n-n)! = 0! = 1`.

Variation mit Wiederholung
--------------------------

Die Anzahl Möglichkeiten :math:`k`-mal ein
Objekt aus :math:`n` Objekten auszuwählen.

.. math::
    n^k

**Beispiel:** In einer Urne sind 5
verschiedenfarbige Murmeln. Wie viele
Möglichkeiten gibt es, dreimal eine Murmel
**mit** Zurücklegen zu ziehen?

:math:`5^3 = 125`

.. warning::
    Beachte, dass {blau-blau-grün} eine andere Variation ist als {blau-grün-blau}!

Variation ohne Wiederholung
---------------------------

Die Anzahl Möglichkeiten :math:`k`-mal ein
Objekt aus :math:`n+1-i` Objekten auszuwählen.
Wobei :math:`i` jeweils für den :math:`i`-ten
Zug steht.

.. math::
    \displaystyle \prod_{i=1}^k n+1-i = n * (n-1) * (n-2)\ *\ ...\ *\ (n-(k-1)) = \frac{n!}{(n-k)!}

**Beispiel:** In einer Urne sind 5
verschiedenfarbige Murmeln. Wie viele
Möglichkeiten gibt es, dreimal eine Murmel
**ohne** Zurücklegen zu ziehen?

:math:`\displaystyle \frac{5!}{(5-3)!} = 60`

.. warning::
    Beachte, dass {rot-blau-grün} eine andere Variation ist als {blau-rot-grün}!

Kombination ohne Wiederholung
-----------------------------

Die Anzahl Möglichkeiten aus :math:`n` Objekten
:math:`k` verschiedene Objekte auszuwählen.

.. math::
    \displaystyle \frac{n!}{(n-k)!k!} = \binom{n}{k}

**Beispiel:** In einer Urne sind 5
verschiedenfarbige Murmeln. Wie viele
Möglichkeiten gibt es, drei daraus
auszuwählen?

:math:`\displaystyle \binom{5}{3} = 10`

.. warning::
    Beachte, dass {rot-blau-grün} die gleiche Kombination ist als {blau-rot-grün}!

Kombination mit Wiederholung
----------------------------

Die Anzahl Möglichkeiten aus :math:`n` Objekten
:math:`k` Objekte auszuwählen. Es können dabei
Wiederholungen vorkommen.

.. math::
    \displaystyle \binom{n+k-1}{k} = \frac{(n+k-1)!}{(n-1)!k!}

**Beispiel:** Fritz hat 5 Wasserfarben und möchte
daraus alle ihm möglichen Farben mischen, wenn er
nur einen Teelöffel hat und eine Mischung aus jeweils
3 Löffeln Farbe bestehen muss. Wieviele Mischungen
kann er kreieren?

:math:`\displaystyle \binom{5+3-1}{3} = 840`

.. warning::
    Auch aus {blau-blau-blau} entsteht eine Farbe (mit Wiederholung)!

    {rot-gelb-rot} mischt das gleiche dunkelorange wie {gelb-rot-rot},
    ist also dieselbe Kombination!

.. [#] Source: `Dr. Robert Aehle <http://www.lgr.ch/personen/lehrpersonen/?f=0&s=Aehle>`__
