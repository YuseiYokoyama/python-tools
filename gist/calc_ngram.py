from collections import defaultdict

def calc_ngram(text, n):
    counter = defaultdict(int)
    if len(text) <= n:
        counter[text] += 1
        return counter
    i = 0
    while i + n < len(text):
        ngram = text[i:i+n]
        counter[ngram] += 1
        # for next
        i += 1
    return counter

