


def is_isbn_or_key(word):

    return 'isbn' if len(word) == 13 and word.isdigit() else 'key'