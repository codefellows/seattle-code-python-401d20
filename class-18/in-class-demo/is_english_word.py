import nltk
import ssl
import re

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


# Write a function that tells me how many words in a string are ALSO in one of my corpra
def count_words(text):
    # string.split() list of words in string by given character split
    # "hi hello" -> ["hi", "hello"]
    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        candidate = re.sub(r"[^A-Za-z]+", "", candidate)
        if candidate.lower() in word_list or candidate in name_list:
            word_count += 1

    return word_count


if __name__ == "__main__":
    text = "Hi Hello, Adam"
    print(count_words(text)/len(text.split()))
