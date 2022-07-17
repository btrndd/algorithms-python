def is_palindrome_iterative(word):
    if (len(word) < 1):
        return False
    if (len(word) == 1):
        return True
    for item in range(1, len(word)):
        if word[-item] != word[item - 1]:
            return False
    return True
