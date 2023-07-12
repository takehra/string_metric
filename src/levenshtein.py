def levenshtein(string1: str, string2: str) -> int:
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Arguments must always be of type string.")
    return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
