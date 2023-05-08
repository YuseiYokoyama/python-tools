from pprint import pprint as pp
from pprint import pformat as pf

import spacy

import katakotofreq as kkf

def print_doc(doc):
    print('print_doc') # debug
    for token in doc:
        if token._.kkf_bio == "b":
            print()
            print(token, end=" ")
        elif token._.kkf_bio == "i":
            print(token, end=" ")
    print()

def reproduct_counter(doc):
    s = set()
    for keyword, token_list in kkf.iter_keyword_detail(doc):
        s.add(keyword)
    return s

def check(counter, reproducted):
    if len(reproducted) != len(counter):
        return False
    for keyword in reproducted:
        if keyword not in counter:
            return False
    return True


TAB = "	"
if __name__ == '__main__':
    nlp = spacy.load("ja_ginza")
    # if you want detail of `doc`, exec console command `ginza < input.dat`
    text_list = [text.strip() for text in open("input.dat").readlines()]
    counter_list = []
    stopset = set(["ストップ"])
    for text in text_list:
        doc = nlp(text)
        counter = kkf.count_by_bunsetu_base(doc, stopset=stopset)
        print('counter', counter, TAB, text) # debug
        if not check(counter, reproduct_counter(doc)):
            raise RuntimeError
        counter_list.append(counter)
    sum_counter = kkf.sum_simply(counter_list)
    print('sum_counter') # debug
    print(sum_counter) # debug
    minsup = 1 # minimum support
    comb_list = kkf.freq_word_set_mining.run(counter_list, minsup)
    print('comb_list') # debug
    pp(comb_list) # debug

    print('\33[32m' + 'end' + '\033[0m')

