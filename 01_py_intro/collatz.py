"""
Dieses Modul beinhaltet Funktionen zur Collatz-Folge
Beispiel:
>>> collatz_sequence(19)
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
"""

__author__ = "Nico Kliche"
__example__ = "SEW4/01/Palindrom"
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"


def collatz(n: int) -> int:
    """
    :param n: Startzahl
    :return: Nächste Zahl in der Collatz-Folge

    >>> collatz(19)
    58
    >>> collatz(58)
    29
    """
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_sequence(number: int) -> list[int]:
    """
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    result: list[int] = [number]
    while number != 1:
        number = collatz(number)
        result.append(number)
    return result


def longest_collatz_sequence(n: int) -> tuple[int, int]:
    """
    :param n: Startzahl
    :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    x, y = 0, 0
    for i in range(1, n + 1):
        current: list[int] = collatz_sequence(i)
        if len(current) > y:
            x = i
            y = len(current)
    return x, y
