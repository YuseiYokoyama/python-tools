import spacy
import ginza
from spacy.tokens import Token


#TODO looking is not good name
def get_looking(core_token):
    looking = []
    Token.set_extension("flg_looking", default=False)
    for a in core_token.ancestors:
        for t in ginza.bunsetu_span(a):
            t._.flg_looking = True
    for token in doc:
        if token._.flg_looking:
            looking.append(token)
    Token.remove_extension("flg_looking")
    return looking


if __name__ == '__main__':
    from pprint import pprint as pp
    from pprint import pformat as pf

    nlp = spacy.load("ja_ginza")
    text = "10日から調査として16時以降は、可能です。"
    doc = nlp(text)
    print('doc') # debug
    print(doc) # debug
    token = doc[5]
    looking = get_looking(token)
    print('looking') # debug
    pp(looking) # debug

    print('\33[32m' + 'end' + '\033[0m')

