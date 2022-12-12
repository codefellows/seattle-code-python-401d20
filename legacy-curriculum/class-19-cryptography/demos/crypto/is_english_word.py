from english_words import word_list

candidates = [
    'a dark and stormy night',
    'n qnex naq fgbezl avtug',
    'j mjat jwm bcxavh wrpqc',
]


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for word in candidate_words:
        if word in word_list:
            print('english word', word)
            word_count += 1

    return word_count

for phrase in candidates:
    word_count = count_words(phrase)
    print(word_count / len(phrase.split()))
