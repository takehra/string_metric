def levenshtein_distance(string1: str, string2: str) -> int:
    """
    Compute the Levenshtein distance between two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Both arguments must be strings.")

    if not string1:
        return len(string2)
    if not string2:
        return len(string1)

    distance_matrix: list[list[int]] = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        distance_matrix[i][0] = i

    for j in range(1, len(string2) + 1):
        distance_matrix[0][j] = j

    for j in range(1, len(string2) + 1):
        for i in range(1, len(string1) + 1):
            substitution_cost = 1 if string1[i-1] != string2[j-1] else 0

            distance_matrix[i][j] = min(
                # deletion
                distance_matrix[i-1][j] + 1,
                # insertion
                distance_matrix[i][j-1] + 1,
                # substitution
                distance_matrix[i-1][j-1] + substitution_cost
            )

    return distance_matrix[len(string1)][len(string2)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    levenshtein_distance("cat", "hat")
