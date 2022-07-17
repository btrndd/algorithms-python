def is_palindrome_recursive(word, low_index, high_index):
    if (len(word) < 1):
        return False
    return word == reverse(word)


def reverse(word):
    if (len(word) <= 1):
        return word
    return word[-1] + reverse(word[:len(word) - 1])
