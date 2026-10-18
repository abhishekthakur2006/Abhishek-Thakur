import re


def largest_word(sentence):
    if sentence is None or sentence == "":
        return ""

    words = re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?", sentence)
    if not words:
        return ""

    longest = ""
    for word in words:
        cleaned = word.strip(".,!?;:\"'()[]{}")
        if len(cleaned) > len(longest):
            longest = cleaned
    return longest


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(largest_word(text))
