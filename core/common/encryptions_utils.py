import hashlib


def hash_(string):
    """
    hashes a string.

    Args:
        string (str): a string.

    Returns:
        str: sha256 hash representation of the string.
    """
    return hashlib.sha256(string.encode("utf-8")).hexdigest()
