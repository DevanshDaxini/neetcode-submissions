from typing import List

def count_unique_words(words: List[str]) -> int:
    length = len(words)

    if length == 0:
        return 0

    set_words = set(words)
    no_dupe_words = list(set_words)

    return len(no_dupe_words)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
