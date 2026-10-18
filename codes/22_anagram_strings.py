def is_anagram(first, second):
    if first is None or second is None:
        return False

    cleaned_first = "".join(ch.lower() for ch in first if ch.isalnum())
    cleaned_second = "".join(ch.lower() for ch in second if ch.isalnum())

    if len(cleaned_first) != len(cleaned_second):
        return False

    return sorted(cleaned_first) == sorted(cleaned_second)
