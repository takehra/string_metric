"""
This module contains a function for calculating the Hamming distance between two strings.
"""

def hamming(string1: str, string2: str) -> int:
    """
    Calculate the Hamming distance between two strings.

    The Hamming distance is the number of positions at which the corresponding elements in the two strings are different.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        int: The Hamming distance between the two strings.

    Raises:
        TypeError: If either `string1` or `string2` is not of type string.
        ValueError: If the lengths of `string1` and `string2` are not equal.
    
    Complexit

    Examples:
        >>> hamming("cat", "hat")
        1
        >>> hamming("", "")
        0
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Arguments must always be of type string.")

    if len(string1) != len(string2):
        raise ValueError("In hamming distance, the lengths of the argument strings must match.")

    distance = 0

    for elm1, elm2 in zip(string1, string2):
        if elm1 != elm2:
            distance += 1

    assert 0 <= distance <= len(string1)

    return distance


if __name__ == "__main__":
    import doctest
    doctest.testmod()
