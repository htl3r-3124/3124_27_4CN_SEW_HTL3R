"""
Dieses Modul beinhaltet eine Funktion zur McCarthy-91-Funktion
Beispiel:
>>> M(91)
91
"""

__author__ = "Nico Kliche"
__example__ = "SEW4/01/3"
__date__ = "25.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest
from time import time


def M(n: int) -> int:
    """
    :param n: Startzahl
    :return: Erste Zahl über 100 subtrahiert mit 10

    >>> M(91)
    91
    >>> M(1000)
    990
    """
    return n - 10 if n > 100 else M(M(n + 11))


def main() -> None:
    """
    Testet die McCarthy-91-Funktion
    Führt außerdem die Doctests aus.
    """
    doctest.testmod()

    t0 = time()
    try:
        m_list: list[int] = []
        m_dict: dict[int, int] = {}
        for i in range(200):
            m_list.append(M(i))
            m_dict[i] = M(i)
    except ValueError:
        pass
    t1 = time()
    print(f"Dauer: {t1 - t0}")


if __name__ == "__main__":
    main()
