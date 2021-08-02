from nltk.tokenize import WhitespaceTokenizer
import nltk
import random


def create_tokens(_corpus_f):
    _tokens = []
    tk = WhitespaceTokenizer()
    for line in _corpus_f:
        _tokens += tk.tokenize(line)

    return _tokens


def get_trigrams_freq(_trigrams):
    _freq = dict()
    for trigram in _trigrams:
        _freq.setdefault(f"{trigram[0]} {trigram[1]}", dict()).setdefault(trigram[2], 0)
        _freq[f"{trigram[0]} {trigram[1]}"][trigram[2]] += 1

    return _freq


def has_sentence_ending(word):
    return word[-1] in "?!."


def create_random_sentence(_freq):
    sentence = []
    phrase = random.choice(list(_freq.keys()))
    end = has_sentence_ending(phrase.split()[0])

    while end or phrase[0].islower():
        phrase = random.choice(list(_freq.keys()))
        end = has_sentence_ending(phrase.split()[0])

    sentence.extend(phrase.split())

    while len(sentence) < 5 or not end:
        last_two = f"{sentence[-2]} {sentence[-1]}"
        phrase = random.choices(list(_freq.get(last_two).keys()), _freq.get(last_two).values())[0]
        while end and phrase[0].islower():
            phrase = random.choices(list(_freq.get(last_two).keys()), _freq.get(last_two).values())[0]

        sentence.append(phrase)
        end = has_sentence_ending(phrase)

    return sentence


corpus_f = open(input(), "r", encoding="utf-8")
tokens = create_tokens(corpus_f)
trigrams = list(nltk.trigrams(tokens))
freq = get_trigrams_freq(trigrams)

for _i in range(10):
    print(" ".join(create_random_sentence(freq)))
