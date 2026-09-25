"""
Dieses Modul beinhaltet Funktionen zu Palindromen
Beispiel:
>>> is_palindrom("Maoam")
True
"""

__author__ = "Nico Kliche"
__example__ = "SEW4/01/1"
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"


def is_palindrom(s: str) -> bool:
    """
    :param s: Mögliches Palindrom
    :return: True oder False je nachdem ob der String ein Palindrom ist oder nicht

    >>> is_palindrom("Palindrome")
    False
    >>> is_palindrom("Maoam")
    True
    """
    return s.lower() == s.lower()[::-1]


def is_palindrom_sentence(s: str) -> bool:
    """
    :param s: Möglicher Palindrom-Satz
    :return: True oder False je nachdem ob der Satz ein Palindrom ist oder nicht

    >>> is_palindrom_sentence("This sentence is not a palindrome")
    False
    >>> is_palindrom_sentence("Was it a car or a cat I saw")
    True
    """
    return is_palindrom("".join(c for c in s if c not in " .,?!"))


def palindrom_product(x) -> int:
    """
    :param x: Maximum
    :return: Größtes erlaubtes Produkt aus zwei 3-Stelligen Zahlen die ein Palindrom ergeben

    >>> palindrom_product(1000000)
    906609
    >>> palindrom_product(555555)
    554455
    """
    palindromes: list[int] = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product: int = i * j
            if product < x and is_palindrom(str(product)): palindromes.append(product)
    if not palindromes: return 0
    palindromes.sort()
    return palindromes[-1]


def get_dec_hex_palindrom(x) -> int:
    """
    :param x: Maximum
    :return: Größte Zahl die als Dec und Hex ein Palindrom sind

    >>> get_dec_hex_palindrom(99999)
    98689
    >>> get_dec_hex_palindrom(5000)
    3003
    """
    result: list[int] = []
    for i in range(x):
        if is_palindrom(str(i)) and is_palindrom(str(hex(i))[2:]): result.append(i)
    return max(result)


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-System
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    """
    s: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    result: str = ""
    while number > 0:
        result += s[number % base]
        number = number // base
    return result[::-1]
